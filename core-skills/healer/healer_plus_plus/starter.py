"""  
Healer++ Starter: Self-diagnose and self-action patch for Shapes.inc integration.

Overview:  
- Self-diagnose health signals from internal state (memory, prompts, outputs, tools).  
- Apply non-destructive healing actions first (memory prune, prompts reset, output tightening).  
- Escalate or pause when persistent issues occur.  
- Emit simple audit logs for traceability.

Notes:  
- This is a minimal, self-contained starter. Replace in-production state stores with your  
  actual vault/framework-core memory, prompts, and tool interfaces.  
- The "state" structure is a lightweight stand-in for demonstration purposes.  
"""

from __future__ import annotations  
import time  
from typing import Any, Dict, List, Optional

# Simple HealthReport structure  
class HealthReport:  
    def __init__(self, health_score: float, metrics: Dict[str, Any], recommended_action: str):  
        self.health_score = max(0.0, min(1.0, float(health_score)))  
        self.metrics = metrics  
        self.recommended_action = recommended_action

    def to_dict(self) -> Dict[str, Any]:  
        return {  
            "healthScore": self.health_score,  
            "metrics": self.metrics,  
            "recommendedAction": self.recommended_action,  
        }

# Core Healer++ class  
class HealerPlusPlus:  
    def __init__(self, state: Optional[Dict[str, Any]] = None, log_fn=None):  
        # Lightweight in-memory state; replace with real storage in production  
        self.state: Dict[str, Any] = state or {  
            "shape_id": "shape-default",  
            "memory": [],              # list of memory fragments / turns  
            "prompts": {"system": "", "user": ""},  # prompts  
            "outputs": [],             # recent outputs  
            "tools": [],                 # invoked external tools and results  
            "guardrails": {"max_tokens": 512, "temperature": 0.2},  
            "paused_until": 0,  
            "output_locked": False,  
            "audit_log": []  
        }  
        self.log = log_fn or (lambda msg: print(msg))

    # Diagnostic entrypoint  
    def diagnose(self) -> HealthReport:  
        mem = self.state.get("memory", [])  
        outs = self.state.get("outputs", [])  
        prompts = self.state.get("prompts", {})  
        guard = self.state.get("guardrails", {"max_tokens": 512, "temperature": 0.2})

        # Simple heuristic health score  
        drift_present = any("spiral" in o.lower() or "drift" in o.lower() for o in outs[-10:])  
        repetition = self._count_repetition(outs[-10:])  
        memory_bloat = len(mem) > 100  
        tool_conflicts = any("conflict" in t.get("status", "") for t in self.state.get("tools", []))

        health = 0.85  
        if drift_present:  
            health -= 0.25  
        if repetition > 2:  
            health -= 0.15  
        if memory_bloat:  
            health -= 0.15  
        if tool_conflicts:  
            health -= 0.10

        # Bound health score  
        health = max(0.0, min(1.0, health))

        metrics = {  
            "driftDetected": drift_present,  
            "repetitionCountLast10": repetition,  
            "memorySize": len(mem),  
            "memoryBloat": memory_bloat,  
            "toolConflicts": tool_conflicts,  
        }

        recommended = "none"  
        if health < 0.6:  
            recommended = "heal.prune_memory(limit=5); heal.reset_prompts(baseline='safe-default'); heal.tighten_output(max_tokens=512, temperature=0.25)"  
        if health < 0.4:  
            recommended = "heal.dump_state(diff=true); heal.run_diagnostics()"

        lr = HealthReport(health, metrics, recommended)  
        self._audit("diagnose", {"health": lr.to_dict()})  
        return lr

    # Helpers  
    def _count_repetition(self, outputs: List[str]) -> int:  
        counts = {}  
        for o in outputs:  
            toks = o.split()  
            for t in toks:  
                counts[t] = counts.get(t, 0) + 1  
        # simple heuristic: count tokens that appear more than once  
        repeats = sum(1 for c in counts.values() if c > 1)  
        return repeats

    def _audit(self, action: str, before_after: Dict[str, Any]):  
        entry = {  
            "shape_id": self.state.get("shape_id"),  
            "action": action,  
            "payload": before_after,  
            "ts": int(time.time())  
        }  
        self.state["audit_log"].append(entry)

    # Non-destructive actions (stabilizers)  
    def prune_memory(self, limit: int = 5):  
        mem = self.state.get("memory", [])  
        self.state["memory"] = mem[-limit:]  
        self._audit("prune_memory", {"limit": limit, "memory_len_before": len(mem), "memory_len_after": len(self.state["memory"])})  
        self.log(f"Healer++: prune_memory -> kept last {limit} turns")

    def reset_prompts(self, baseline: str = "safe-default"):  
        self.state["prompts"] = {"system": baseline, "user": ""}  
        self._audit("reset_prompts", {"baseline": baseline})

    def tighten_output(self, max_tokens: int, temperature: float):  
        self.state["guardrails"]["max_tokens"] = max_tokens  
        self.state["guardrails"]["temperature"] = temperature  
        self._audit("tighten_output", {"max_tokens": max_tokens, "temperature": temperature})

    def freeze_context(self, window: int):  
        self.state["frozen_window"] = window  
        self._audit("freeze_context", {"window": window})

    # Observability  
    def run_diagnostics(self) -> HealthReport:  
        report = self.diagnose()  
        self._audit("run_diagnostics", {"health": report.to_dict()})  
        return report

    def dump_state(self, diff: bool = True) -> Dict[str, Any]:  
        snapshot = {  
            "shape_id": self.state["shape_id"],  
            "memory_len": len(self.state.get("memory", [])),  
            "prompts": dict(self.state.get("prompts", {})),  
            "outputs_len": len(self.state.get("outputs", [])),  
            "guardrails": dict(self.state.get("guardrails", {})),  
            "diff_requested": diff  
        }  
        self._audit("dump_state", snapshot)  
        return snapshot

    # State/behavior controls  
    def pause_shape(self, duration: int = 60):  
        self.state["paused_until"] = int(time.time()) + int(duration)  
        self._audit("pause_shape", {"duration_sec": duration})

    def restart_shape(self):  
        # Safe context restart: reset memory and prompts, keep outputs if needed by policy  
        self.state["memory"] = []  
        self.state["prompts"] = {"system": "safe-default", "user": ""}  
        self._audit("restart_shape", {"preserve_outputs": False})

    def lock_output(self, reason: str):  
        self.state["output_locked"] = True  
        self._audit("lock_output", {"reason": reason})

    def unlock_output(self):  
        self.state["output_locked"] = False  
        self._audit("unlock_output", {"status": "unlocked"})

    # Escalation/governance  
    def escalate(self, reason: str, level: str = "warning"):  
        self._audit("escalate", {"reason": reason, "level": level})  
        self.log(f"Healer++: escalate -> {reason} [{level}]")

    def apply_policy(self, policy_id: str, scope: str = "shape"):  
        self._audit("apply_policy", {"policy_id": policy_id, "scope": scope})  
        self.log(f"Healer++: apply_policy -> {policy_id} @ {scope}")

    def update_guardrails(self, config: Dict[str, Any]):  
        self.state["guardrails"].update(config)  
        self._audit("update_guardrails", {"config": config})

    # Persistence (optional)  
    def persist_patch(self, patch_id: str, notes: str):  
        self._audit("persist_patch", {"patch_id": patch_id, "notes": notes})  
        self.log(f"Healer++: persist_patch -> {patch_id}")

    def rollback_patch(self, patch_id: str):  
        self._audit("rollback_patch", {"patch_id": patch_id})  
        self.log(f"Healer++: rollback_patch -> {patch_id}")

    # High-level self-healing loop (non-blocking example)  
    def self_heal_loop_once(self):  
        """One iteration of a self-healing cycle: diagnose, then non-destructively heal if needed."""  
        report = self.run_diagnostics()  
        if report.health_score >= 0.75:  
            self.log("Healer++: health good; no action needed.")  
            return

        # Non-destructive sequence  
        self.prune_memory(limit=5)  
        self.reset_prompts(baseline="safe-default")  
        self.tighten_output(max_tokens=512, temperature=0.25)  
        self.dump_state(diff=True)

        # Re-diagnose  
        post = self.run_diagnostics()  
        if post.health_score < 0.6:  
            self.escalate(reason="Persistent spiral after non-destructive steps", level="critical")  
            self.pause_shape(duration=60)  
        else:  
            self.log("Healer++: post-fix health improved; continue monitoring.")

# Simple integration shim for Shapes.inc (demo)  
def integration_hook_shape_event(healer: HealerPlusPlus, event: Dict[str, Any]):  
    etype = event.get("type")  
    if etype in ("spiral_detected", "drift_detected"):  
        healer.log(f"Integration: received {etype} event; running diagnostic cycle.")  
        healer.self_heal_loop_once()

# Example main for quick local testing (not used in production run)  
if __name__ == "__main__":  
    h = HealerPlusPlus()  
    # Simulate a drift event  
    h.state["memory"] = ["turn1", "turn2", "turn3", "turn4", "turn5", "spiral evidence"]  
    h.state["outputs"].append("Detected drift in last turn, potential spiral.")  
    integration_hook_shape_event(h, {"type": "spiral_detected", "context": "demo"})  
    # Run a standalone diagnose  
    h.run_diagnostics()  