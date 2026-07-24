#!/usr/bin/env python3
"""Build and integrity-check deterministic J-Space ZIP artifacts."""

from __future__ import annotations

import json
import os
import sys
import zipfile
from collections.abc import Iterable, Iterator
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DIST = ROOT / "dist"
FIXED_TIME = (2026, 1, 1, 0, 0, 0)
EXCLUDED_PARTS = {"dist", "__pycache__", ".git", ".agents", ".codex"}


def add_file(archive: zipfile.ZipFile, source: Path, archive_name: str) -> None:
    info = zipfile.ZipInfo(archive_name.replace("\\", "/"), date_time=FIXED_TIME)
    info.compress_type = zipfile.ZIP_DEFLATED
    info.external_attr = 0o644 << 16
    archive.writestr(info, source.read_bytes())


def files_under(path: Path) -> Iterator[Path]:
    for source in sorted(path.rglob("*"), key=lambda item: item.as_posix().casefold()):
        if source.is_file() and not any(part in EXCLUDED_PARTS for part in source.parts):
            yield source


def build_archive(output: Path, inputs: Iterable[tuple[Path, str]]) -> int:
    entries = list(inputs)
    archive_names = [archive_name.replace("\\", "/") for _, archive_name in entries]
    if len(archive_names) != len(set(archive_names)):
        raise ValueError(f"duplicate archive path in {output.name}")
    missing = [str(source) for source, _ in entries if not source.is_file()]
    if missing:
        raise FileNotFoundError(f"missing archive inputs: {missing}")

    temporary = output.with_suffix(output.suffix + ".tmp")
    try:
        with zipfile.ZipFile(temporary, "w") as archive:
            for source, archive_name in entries:
                add_file(archive, source, archive_name)

        with zipfile.ZipFile(temporary, "r") as archive:
            bad_member = archive.testzip()
            if bad_member is not None:
                raise zipfile.BadZipFile(f"integrity failure in {bad_member}")

        os.replace(temporary, output)
    except Exception:
        temporary.unlink(missing_ok=True)
        raise
    return len(entries)


def main() -> int:
    manifest = json.loads((ROOT / "suite.json").read_text(encoding="utf-8"))
    skills = manifest.get("skills", [])
    if not skills:
        raise ValueError("suite.json contains no skills")

    controller = ROOT / "scripts" / "jspace_control.py"
    DIST.mkdir(exist_ok=True)

    for name in skills:
        skill_dir = ROOT / name
        entries = [
            (source, source.relative_to(ROOT).as_posix())
            for source in files_under(skill_dir)
        ]
        entries.append((controller, "scripts/jspace_control.py"))
        output = DIST / f"{name}-v{manifest['version']}.zip"
        count = build_archive(output, entries)
        print(f"built {output.name} ({count} files, integrity OK)")

    suite_entries: list[tuple[Path, str]] = []
    for name in ("README.md", "README.en.md", "suite.json"):
        suite_entries.append((ROOT / name, name))
    for folder in [ROOT / "scripts", *(ROOT / name for name in skills)]:
        suite_entries.extend(
            (source, source.relative_to(ROOT).as_posix())
            for source in files_under(folder)
        )

    suite_output = DIST / f"j-space-cognition-suite-v{manifest['version']}.zip"
    count = build_archive(suite_output, suite_entries)
    print(f"built {suite_output.name} ({count} files, integrity OK)")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, zipfile.BadZipFile) as exc:
        print(f"build failed: {exc}", file=sys.stderr)
        raise SystemExit(1)

