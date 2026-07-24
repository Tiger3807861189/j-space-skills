#!/usr/bin/env python3
"""Static consistency validator for the J-Space Cognition Suite V3.2."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "suite.json"
FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)
LOCAL_LINK = re.compile(r"\[[^\]]+\]\((?!https?://|#)([^)]+)\)")
SKILL_NAME = re.compile(r"`(j-space-[a-z0-9-]+)`")
HAN = re.compile(r"[\u3400-\u9fff]")
YAML_FIELD = re.compile(
    r'^\s{2}(display_name|short_description|default_prompt):\s*"(.*)"\s*$',
    re.MULTILINE,
)


def parse_frontmatter(text: str) -> tuple[dict[str, str], str | None]:
    match = FRONTMATTER.match(text)
    if not match:
        return {}, "missing or malformed YAML frontmatter"
    result: dict[str, str] = {}
    for raw in match.group(1).splitlines():
        if not raw.strip():
            continue
        if ":" not in raw:
            return {}, f"malformed frontmatter line: {raw!r}"
        key, value = raw.split(":", 1)
        result[key.strip()] = value.strip()
    return result, None


def check_local_links(
    source: Path, base: Path, text: str, errors: list[str]
) -> None:
    for target in LOCAL_LINK.findall(text):
        clean = target.split("#", 1)[0].replace("%20", " ")
        if clean and not (base / clean).resolve().is_file():
            errors.append(f"{source.relative_to(ROOT)}: broken local link {target!r}")


def main() -> int:
    errors: list[str] = []
    warnings: list[str] = []

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: cannot read suite.json: {exc}")
        return 1

    names = manifest.get("skills", [])
    known = set(names)
    if manifest.get("version") != "3.2.0":
        errors.append("suite.json version must be 3.2.0")
    if len(names) != len(known):
        errors.append("suite.json contains duplicate skill names")
    if len(names) != 10:
        errors.append(f"suite.json must list 10 skills; found {len(names)}")
    if manifest.get("design", {}).get("target_profile") is None:
        errors.append("suite.json must declare design.target_profile")

    actual_skill_dirs = {
        path.name for path in ROOT.glob("j-space-*") if path.is_dir()
    }
    if actual_skill_dirs != known:
        errors.append(
            "skill folders differ from suite.json: "
            f"missing={sorted(known - actual_skill_dirs)}, "
            f"unlisted={sorted(actual_skill_dirs - known)}"
        )

    english_paths: list[Path] = [ROOT / "README.en.md", MANIFEST]
    for name in names:
        skill_dir = ROOT / name
        skill_file = skill_dir / "SKILL.md"
        agent_file = skill_dir / "agents" / "openai.yaml"

        if not skill_file.is_file():
            errors.append(f"{name}: missing SKILL.md")
            continue
        text = skill_file.read_text(encoding="utf-8-sig")
        english_paths.append(skill_file)
        meta, meta_error = parse_frontmatter(text)
        if meta_error:
            errors.append(f"{name}: {meta_error}")
        else:
            if set(meta) != {"name", "description"}:
                errors.append(f"{name}: frontmatter keys must be exactly name and description")
            if meta.get("name") != name:
                errors.append(f"{name}: frontmatter name does not match folder")
            if not meta.get("description"):
                errors.append(f"{name}: description is empty")

        line_count = len(text.splitlines())
        word_count = len(re.findall(r"\b[\w'-]+\b", text))
        if line_count >= 500:
            errors.append(f"{name}: SKILL.md has {line_count} lines; limit is below 500")
        if word_count >= 5000:
            errors.append(f"{name}: SKILL.md has {word_count} words; limit is below 5000")
        if re.search(r"\b(TODO|TBD|PLACEHOLDER)\b", text, re.IGNORECASE):
            errors.append(f"{name}: unresolved placeholder found")
        if "Conservative " not in text:
            errors.append(f"{name}: missing conservative execution policy")
        for heading in ("## Success Standard", "## Handoff"):
            if heading not in text:
                errors.append(f"{name}: missing required section {heading}")
        if name != "j-space-awakening" and "## Failure Modes" not in text:
            errors.append(f"{name}: missing Failure Modes section")
        if "`EMPIRICS`" in text:
            errors.append(f"{name}: use canonical mode name `EMPIRICAL`, not `EMPIRICS`")
        if "`r`n" in text or "`n" in text:
            errors.append(f"{name}: literal newline escape found")

        check_local_links(skill_file, skill_dir, text, errors)
        for referenced in SKILL_NAME.findall(text):
            if referenced not in known:
                errors.append(f"{name}: unknown cross-skill reference {referenced}")

        if not agent_file.is_file():
            errors.append(f"{name}: missing agents/openai.yaml")
        else:
            english_paths.append(agent_file)
            agent_text = agent_file.read_text(encoding="utf-8-sig")
            fields = dict(YAML_FIELD.findall(agent_text))
            missing = {"display_name", "short_description", "default_prompt"} - set(fields)
            if missing:
                errors.append(f"{name}: openai.yaml missing quoted fields {sorted(missing)}")
            if f"${name}" not in fields.get("default_prompt", ""):
                errors.append(f"{name}: default_prompt must explicitly mention ${name}")
            short = fields.get("short_description", "")
            if short and not 25 <= len(short) <= 64:
                errors.append(
                    f"{name}: short_description length is {len(short)}; expected 25-64"
                )

        if (skill_dir / "README.md").exists():
            warnings.append(f"{name}: README.md is unnecessary inside a skill folder")

        for resource in skill_dir.rglob("*"):
            if resource.is_file() and resource.suffix.lower() in {".md", ".py", ".yaml"}:
                english_paths.append(resource)

    required = (
        "README.md",
        "README.en.md",
        "suite.json",
        "scripts/jspace_control.py",
        "scripts/test_jspace_control.py",
        "scripts/validate_suite.py",
        "scripts/build_dist.py",
        "j-space-awakening/references/induction-playbook.md",
        "j-space-awakening/references/science-map.md",
        "j-space-awakening/references/conservative-profile.md",
    )
    for relative in required:
        if not (ROOT / relative).is_file():
            errors.append(f"suite: missing {relative}")

    for readme_name in ("README.md", "README.en.md"):
        readme = ROOT / readme_name
        if readme.is_file():
            readme_text = readme.read_text(encoding="utf-8-sig")
            check_local_links(readme, readme.parent, readme_text, errors)
            if "V3.2" not in readme_text:
                errors.append(f"{readme_name}: missing V3.2 identifier")
            if "`r`n" in readme_text or "`n" in readme_text:
                errors.append(f"{readme_name}: literal newline escape found")

    reference_dir = ROOT / "j-space-awakening" / "references"
    if reference_dir.is_dir():
        for reference in reference_dir.glob("*.md"):
            reference_text = reference.read_text(encoding="utf-8-sig")
            check_local_links(reference, reference.parent, reference_text, errors)
            if len(reference_text.splitlines()) > 100 and "## Contents" not in reference_text:
                errors.append(f"{reference.relative_to(ROOT)}: long reference needs Contents")

    for script in (ROOT / "scripts").glob("*.py"):
        english_paths.append(script)

    for path in dict.fromkeys(english_paths):
        if not path.is_file():
            continue
        match = HAN.search(path.read_text(encoding="utf-8-sig"))
        if match:
            errors.append(
                f"{path.relative_to(ROOT)}: core English file contains a Han character"
            )

    print(f"J-Space V{manifest.get('version', '?')} static validation")
    print(f"Skills checked: {len(names)}")
    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")
    if errors:
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"PASS: 0 errors, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

