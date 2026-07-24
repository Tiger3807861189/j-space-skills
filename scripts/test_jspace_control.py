#!/usr/bin/env python3
"""Unit tests for the deterministic J-Space controller."""

from __future__ import annotations

import unittest

from jspace_control import audit_codec, audit_marker, build_checkpoint, choose_route


class RouteTests(unittest.TestCase):
    def test_recovery_has_priority(self) -> None:
        route = choose_route(drift=True, stalled=True, constraints=8)
        self.assertEqual(route.mode, "RECOVERY")

    def test_stall_routes_to_empirical(self) -> None:
        self.assertEqual(choose_route(stalled=True).mode, "EMPIRICAL")

    def test_conservative_overload_externalizes(self) -> None:
        route = choose_route(profile="conservative", constraints=4)
        self.assertEqual(route.mode, "EXTERNAL")

    def test_dense_requires_both_readiness_flags(self) -> None:
        incomplete = choose_route(
            profile="conservative", constraints=5, structure_stable=True
        )
        ready = choose_route(
            profile="conservative",
            novelty="medium",
            stakes="medium",
            constraints=5,
            structure_stable=True,
            codec_ready=True,
        )
        self.assertNotEqual(incomplete.mode, "DENSE")
        self.assertEqual(ready.mode, "DENSE")

    def test_high_stakes_does_not_enter_dense(self) -> None:
        route = choose_route(
            profile="conservative",
            stakes="high",
            constraints=5,
            structure_stable=True,
            codec_ready=True,
        )
        self.assertEqual(route.mode, "EXTERNAL")


class CheckpointTests(unittest.TestCase):
    def test_claim_without_evidence_is_working(self) -> None:
        checkpoint = build_checkpoint(
            goal="g",
            verified=["claim"],
            evidence=None,
            open_questions=None,
            next_action="test",
            version="1",
        )
        self.assertEqual(checkpoint["state"], "WORKING")
        self.assertTrue(checkpoint["warnings"])

    def test_claim_with_evidence_is_verified(self) -> None:
        checkpoint = build_checkpoint(
            goal="g",
            verified=["claim"],
            evidence=["test A"],
            open_questions=None,
            next_action="continue",
            version="2",
        )
        self.assertEqual(checkpoint["state"], "VERIFIED")


class MarkerTests(unittest.TestCase):
    def test_single_keyword_does_not_pass(self) -> None:
        result = audit_marker("PHEW", "record it", "pass")
        self.assertFalse(result["valid"])

    def test_complete_checkpoint_contract_passes(self) -> None:
        result = audit_marker(
            "PHEW / CHECKPOINT",
            "record verified evidence, scope, uncertainty, and version in the ledger",
            "pass",
        )
        self.assertTrue(result["valid"])

    def test_complete_terms_still_need_artifact_verification(self) -> None:
        result = audit_marker(
            "PHEW",
            "record verified evidence, scope, and version in the checkpoint ledger",
        )
        self.assertEqual(result["status"], "NEEDS_ARTIFACT_VERIFICATION")
        self.assertFalse(result["valid"])
    def test_empirical_name_is_canonical(self) -> None:
        result = audit_marker(
            "DATA",
            "compare finite candidates with a test against an independent reference",
            "pass",
        )
        self.assertEqual(result["state"], "EMPIRICAL")
        self.assertTrue(result["valid"])


class CodecTests(unittest.TestCase):
    def test_manual_review_is_required(self) -> None:
        result = audit_codec(
            compact="I -> B",
            expanded="The invariant implies the boundary.",
            required=["invariant", "boundary"],
            next_action="test boundary",
            manual_verdict=None,
        )
        self.assertEqual(result["status"], "NEEDS_MANUAL_REVIEW")
        self.assertFalse(result["valid"])

    def test_manual_pass_after_lexical_gate(self) -> None:
        result = audit_codec(
            compact="I -> B",
            expanded="The invariant implies the boundary.",
            required=["invariant", "boundary"],
            next_action="test boundary",
            manual_verdict="pass",
        )
        self.assertTrue(result["valid"])

    def test_missing_invariant_fails(self) -> None:
        result = audit_codec(
            compact="I -> B",
            expanded="The boundary holds.",
            required=["invariant", "boundary"],
            next_action="test boundary",
            manual_verdict="pass",
        )
        self.assertEqual(result["status"], "FAIL")


if __name__ == "__main__":
    unittest.main()

