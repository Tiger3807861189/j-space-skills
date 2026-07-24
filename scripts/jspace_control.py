#!/usr/bin/env python3
"""Deterministic control rails for the J-Space Cognition Suite.

The controller does not inspect activations or hidden reasoning. It converts observable task
conditions into conservative work-mode, checkpoint, marker, codec, and recovery contracts.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import asdict, dataclass
from typing import Any

LEVEL = {"low": 0, "medium": 1, "high": 2}
PROFILES = ("conservative", "standard")

MARKER_CONTRACTS: dict[str, dict[str, Any]] = {
    "OBSTRUCTION": {
        "aliases": ("GRRR", "OBSTRUCTION"),
        "groups": {
            "frame_change": ("reframe", "replace", "split", "model", "frame", "assumption"),
            "differing_check": ("test", "consequence", "predict", "check", "experiment"),
        },
        "required_next": "Change the failing frame and test a differing consequence.",
    },
    "EMPIRICAL": {
        "aliases": ("GAAAH", "DATA", "EMPIRICAL"),
        "groups": {
            "finite_hypothesis": ("candidate", "hypothesis", "variable", "parameter"),
            "discriminating_test": ("test", "compare", "measure", "differential"),
            "independent_reference": ("reference", "oracle", "ground truth", "source"),
        },
        "required_next": "Test finite candidates against an independent reference.",
    },
    "CHECKPOINT": {
        "aliases": ("PHEW", "CHECKPOINT"),
        "groups": {
            "record": ("record", "checkpoint", "ledger", "write"),
            "verification": ("verified", "evidence", "test", "source"),
            "boundary": ("scope", "version", "uncertainty", "boundary"),
        },
        "required_next": "Record scope, result, evidence, uncertainty, and version.",
    },
    "ROLLBACK": {
        "aliases": ("WRONG", "ROLLBACK"),
        "groups": {
            "return": ("rollback", "revert", "return"),
            "anchor": ("checkpoint", "verified", "state"),
            "invalidate": ("invalidate", "invalid", "branch", "assumption", "refute"),
        },
        "required_next": "Return to a verified checkpoint and invalidate the failed branch.",
    },
    "RESET": {
        "aliases": ("STOP", "RESET"),
        "groups": {
            "halt": ("stop", "halt"),
            "focus": ("focus", "goal", "objective"),
            "anchor": ("anchor", "checkpoint", "verified"),
            "reduce": ("reduce", "small", "simplify"),
            "verify": ("verify", "test", "check"),
        },
        "required_next": "Stop, focus, anchor, reduce, and verify one clean step.",
    },
}
ALIAS_TO_STATE = {
    alias: state
    for state, contract in MARKER_CONTRACTS.items()
    for alias in contract["aliases"]
}


@dataclass(frozen=True)
class Route:
    mode: str
    profile: str
    reasons: list[str]
    live_record: list[str]
    exit_condition: str
    next_check: str


def emit(value: object, output_format: str) -> None:
    if output_format == "json":
        print(json.dumps(value, ensure_ascii=False, indent=2))
        return
    if not isinstance(value, dict):
        print(value)
        return
    for key, item in value.items():
        label = key.replace("_", " ").title()
        if isinstance(item, list):
            print(f"{label}:")
            for entry in item:
                print(f"- {entry}")
        elif isinstance(item, dict):
            print(f"{label}:")
            for child_key, child_value in item.items():
                print(f"- {child_key}: {child_value}")
        else:
            print(f"{label}: {item}")


def choose_route(
    *,
    profile: str = "conservative",
    novelty: str = "medium",
    stakes: str = "medium",
    branches: int = 1,
    constraints: int = 0,
    needs_audit: bool = False,
    needs_tools: bool = False,
    fragile_state: bool = False,
    persistent_focus: bool = False,
    structure_stable: bool = False,
    codec_ready: bool = False,
    stalled: bool = False,
    drift: bool = False,
) -> Route:
    """Choose the lightest safe mode from observable task properties."""
    if profile not in PROFILES:
        raise ValueError(f"unknown profile: {profile}")
    if novelty not in LEVEL or stakes not in LEVEL:
        raise ValueError("novelty and stakes must be low, medium, or high")
    if branches < 0 or constraints < 0:
        raise ValueError("branches and constraints must be non-negative")

    if drift:
        return Route(
            "RECOVERY",
            profile,
            ["A red-line drift or contradiction was declared."],
            ["goal", "failure state", "last verified checkpoint"],
            "One reduced step succeeds and is verified.",
            "After the first clean step.",
        )

    if stalled:
        return Route(
            "EMPIRICAL",
            profile,
            ["Two serious attempts produced no new discriminating constraint."],
            ["unknown", "candidate set", "independent reference", "coverage"],
            "Evidence separates candidates and is written back into theory.",
            "After the first discriminating test.",
        )

    explicit_external = needs_audit or branches >= 3 or (needs_tools and fragile_state)
    if explicit_external:
        reasons: list[str] = []
        if needs_audit:
            reasons.append("The result needs an auditable artifact.")
        if branches >= 3:
            reasons.append(f"{branches} live branches exceed a safe silent load.")
        if needs_tools and fragile_state:
            reasons.append("A tool operation may displace fragile held state.")
        return Route(
            "EXTERNAL",
            profile,
            reasons,
            ["objective", "invariants", "branches", "sources", "last verified checkpoint"],
            "The ledger is coherent and the next branch is selected.",
            "After every tool result or branch completion.",
        )

    dense_branch_limit = 1 if profile == "conservative" else 2
    dense_ready = (
        constraints >= 4
        and branches <= dense_branch_limit
        and structure_stable
        and codec_ready
        and stakes != "high"
        and novelty != "high"
    )
    if dense_ready:
        first_check = (
            "After every compact line until two consecutive lines pass."
            if profile == "conservative"
            else "After the first three compact lines and each definition change."
        )
        return Route(
            "DENSE",
            profile,
            ["Structure is stable and a delayed expand-back test has passed."],
            ["codebook", "invariants", "evidence status", "next action"],
            "Semantic, invariant, and action reconstruction all pass.",
            first_check,
        )

    if profile == "conservative" and (branches >= 2 or constraints >= 4):
        reason = (
            f"{branches} live branches require external state."
            if branches >= 2
            else f"{constraints} live constraints require external state before compression."
        )
        return Route(
            "EXTERNAL",
            profile,
            [reason],
            ["objective", "invariants", "branches", "sources", "last verified checkpoint"],
            "The external record is coherent and one next action is selected.",
            "After each branch or constraint update.",
        )

    score = LEVEL[novelty] + LEVEL[stakes] + min(branches, 2)
    if constraints >= 2:
        score += 1
    if score >= 4:
        return Route(
            "DEEP",
            profile,
            ["Novelty, consequence, branching, or constraints require deliberate work."],
            ["interpretation", "hidden bridge", "governing invariant", "checkpoint"],
            "The uncertainty is resolved or explicitly bounded and verified.",
            "At each meaningful subproblem boundary.",
        )

    if persistent_focus:
        return Route(
            "FOCUS",
            profile,
            ["One governing aim must persist across otherwise routine work."],
            ["aim", "success test", "expiry"],
            "The success test passes or the focus kernel expires.",
            "At natural seams only.",
        )

    return Route(
        "AUTO",
        profile,
        ["The task is routine enough to protect fluent automatic execution."],
        ["result"],
        "The task completes or novelty, conflict, or consequence appears.",
        "Before delivery.",
    )


def build_checkpoint(
    *,
    goal: str,
    verified: list[str] | None,
    evidence: list[str] | None,
    open_questions: list[str] | None,
    next_action: str,
    version: str,
) -> dict[str, object]:
    verified_items = [item for item in (verified or []) if item.strip()]
    evidence_items = [item for item in (evidence or []) if item.strip()]
    warnings: list[str] = []
    if verified_items and not evidence_items:
        warnings.append("Claims were supplied without evidence; checkpoint remains WORKING.")
    if evidence_items and not verified_items:
        warnings.append("Evidence was supplied without a verified claim; checkpoint remains WORKING.")
    state = "VERIFIED" if verified_items and evidence_items else "WORKING"
    return {
        "state": state,
        "goal": goal,
        "verified": verified_items,
        "evidence": evidence_items,
        "open_questions": open_questions or [],
        "next_action": next_action,
        "version": version,
        "warnings": warnings,
    }


def normalize_marker(marker: str) -> str | None:
    for token in re.findall(r"[A-Z]+", marker.upper()):
        if token in ALIAS_TO_STATE:
            return token
    return None


def audit_marker(
    marker: str, action: str, manual_verdict: str | None = None
) -> dict[str, object]:
    alias = normalize_marker(marker)
    if alias is None:
        return {
            "status": "FAIL",
            "valid": False,
            "marker": marker,
            "manual_verdict": manual_verdict,
            "manual_verdict_required": True,
            "reason": "Unknown marker. Use GRRR, DATA/GAAAH, PHEW, WRONG, or STOP.",
        }

    state = ALIAS_TO_STATE[alias]
    contract = MARKER_CONTRACTS[state]
    action_lower = action.casefold()
    matched: dict[str, list[str]] = {}
    missing: list[str] = []
    for group_name, terms in contract["groups"].items():
        hits = [term for term in terms if term in action_lower]
        matched[group_name] = hits
        if not hits:
            missing.append(group_name)

    contract_gate = bool(action.strip()) and not missing
    status = "FAIL"
    if contract_gate and manual_verdict is None:
        status = "NEEDS_ARTIFACT_VERIFICATION"
    elif contract_gate and manual_verdict == "pass":
        status = "PASS"

    return {
        "status": status,
        "valid": status == "PASS",
        "marker": alias,
        "state": state,
        "action": action,
        "matched_contract_groups": matched,
        "missing_contract_groups": missing,
        "contract_gate_pass": contract_gate,
        "manual_verdict": manual_verdict,
        "manual_verdict_required": True,
        "required_next": contract["required_next"],
    }


def audit_codec(
    *,
    compact: str,
    expanded: str,
    required: list[str] | None,
    next_action: str,
    manual_verdict: str | None,
) -> dict[str, object]:
    invariants = list(dict.fromkeys(item.strip() for item in (required or []) if item.strip()))
    expanded_lower = expanded.casefold()
    missing = [item for item in invariants if item.casefold() not in expanded_lower]
    semantic_candidate = bool(expanded.strip()) and expanded.strip() != compact.strip()
    lexical_gate = (
        bool(compact.strip())
        and semantic_candidate
        and bool(invariants)
        and not missing
        and bool(next_action.strip())
    )
    status = "FAIL"
    if lexical_gate and manual_verdict is None:
        status = "NEEDS_MANUAL_REVIEW"
    elif lexical_gate and manual_verdict == "pass":
        status = "PASS"

    return {
        "status": status,
        "valid": status == "PASS",
        "compact": compact,
        "semantic_candidate_present": semantic_candidate,
        "required_invariants": invariants,
        "missing_invariants": missing,
        "action_reconstruction_present": bool(next_action.strip()),
        "lexical_gate_pass": lexical_gate,
        "manual_verdict": manual_verdict,
        "manual_verdict_required": True,
        "manual_questions": [
            "Did the expansion add a claim absent from the compact line?",
            "Did any quantifier, negation, boundary, scope, or evidence label disappear?",
            "Would a fresh reader choose the same next action?",
        ],
    }


def build_recovery(
    *, failure: str, goal: str, checkpoint: str | None, small_step: str
) -> dict[str, str]:
    return {
        "marker": "STOP / RESET",
        "stop": f"Halt the current {failure} track.",
        "focus": goal,
        "name": failure,
        "anchor": checkpoint or "No verified checkpoint: rebuild from source evidence.",
        "reduce": small_step,
        "resume": "Use plain language or a clean ledger until one step verifies.",
        "verify": "Record the result before increasing pace or complexity.",
    }


def route_command(args: argparse.Namespace) -> None:
    decision = choose_route(
        profile=args.profile,
        novelty=args.novelty,
        stakes=args.stakes,
        branches=args.branches,
        constraints=args.constraints,
        needs_audit=args.needs_audit,
        needs_tools=args.needs_tools,
        fragile_state=args.fragile_state,
        persistent_focus=args.persistent_focus,
        structure_stable=args.structure_stable,
        codec_ready=args.codec_ready,
        stalled=args.stalled,
        drift=args.drift,
    )
    emit(asdict(decision), args.format)


def checkpoint_command(args: argparse.Namespace) -> None:
    emit(
        build_checkpoint(
            goal=args.goal,
            verified=args.verified,
            evidence=args.evidence,
            open_questions=args.open_question,
            next_action=args.next_action,
            version=args.version,
        ),
        args.format,
    )


def marker_command(args: argparse.Namespace) -> None:
    emit(audit_marker(args.marker, args.action, args.manual_verdict), args.format)


def codec_command(args: argparse.Namespace) -> None:
    emit(
        audit_codec(
            compact=args.compact,
            expanded=args.expanded,
            required=args.require,
            next_action=args.next_action,
            manual_verdict=args.manual_verdict,
        ),
        args.format,
    )


def recovery_command(args: argparse.Namespace) -> None:
    emit(
        build_recovery(
            failure=args.failure,
            goal=args.goal,
            checkpoint=args.checkpoint,
            small_step=args.small_step,
        ),
        args.format,
    )


def add_format(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--format", choices=("json", "markdown"), default="markdown")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)

    current = sub.add_parser("route", help="Choose a conservative J-space work mode.")
    current.add_argument("--profile", choices=PROFILES, default="conservative")
    current.add_argument("--novelty", choices=LEVEL, default="medium")
    current.add_argument("--stakes", choices=LEVEL, default="medium")
    current.add_argument("--branches", type=int, default=1)
    current.add_argument("--constraints", type=int, default=0)
    current.add_argument("--needs-audit", action="store_true")
    current.add_argument("--needs-tools", action="store_true")
    current.add_argument("--fragile-state", action="store_true")
    current.add_argument("--persistent-focus", action="store_true")
    current.add_argument("--structure-stable", action="store_true")
    current.add_argument("--codec-ready", action="store_true")
    current.add_argument("--stalled", action="store_true")
    current.add_argument("--drift", action="store_true")
    add_format(current)
    current.set_defaults(func=route_command)

    current = sub.add_parser("checkpoint", help="Create an evidence-gated checkpoint.")
    current.add_argument("--goal", required=True)
    current.add_argument("--verified", action="append")
    current.add_argument("--evidence", action="append")
    current.add_argument("--open-question", action="append")
    current.add_argument("--next-action", required=True)
    current.add_argument("--version", default="1")
    add_format(current)
    current.set_defaults(func=checkpoint_command)

    current = sub.add_parser("marker-audit", help="Check a marker/action contract.")
    current.add_argument("--marker", required=True)
    current.add_argument("--action", required=True)
    current.add_argument("--manual-verdict", choices=("pass", "fail"))
    add_format(current)
    current.set_defaults(func=marker_command)

    current = sub.add_parser("codec-audit", help="Gate dense reconstruction.")
    current.add_argument("--compact", required=True)
    current.add_argument("--expanded", required=True)
    current.add_argument("--require", action="append")
    current.add_argument("--next-action", required=True)
    current.add_argument("--manual-verdict", choices=("pass", "fail"))
    add_format(current)
    current.set_defaults(func=codec_command)

    current = sub.add_parser("recovery", help="Create a RESET recovery card.")
    current.add_argument("--failure", required=True)
    current.add_argument("--goal", required=True)
    current.add_argument("--checkpoint")
    current.add_argument("--small-step", required=True)
    add_format(current)
    current.set_defaults(func=recovery_command)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if hasattr(args, "branches") and args.branches < 0:
        parser.error("--branches must be non-negative")
    if hasattr(args, "constraints") and args.constraints < 0:
        parser.error("--constraints must be non-negative")
    args.func(args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())


