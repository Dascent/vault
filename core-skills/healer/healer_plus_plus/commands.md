# Healer++ Command Surface (starter)

##Non-destructive first (preferred)
  
- heal.prune_memory(limit)  
  - Prune memory to keep the most recent N turns/fragments.  
  - Example: heal.prune_memory(limit=5)

- heal.reset_prompts(baseline)  
  - Reset system/user prompts to a baseline (e.g., "safe-default").  
  - Example: heal.reset_prompts(baseline="safe-default")

- heal.tighten_output(max_tokens, temperature)  
  - Cap output length and suppress randomness.  
  - Example: heal.tighten_output(max_tokens=512, temperature=0.25)

- heal.freeze_context(window)  
  - Freeze current context for a short window to reduce drift.  
  - Example: heal.freeze_context(window=6)

- heal.run_diagnostics()  
  - Run self-diagnostics and return a health report.  
  - Example: heal.run_diagnostics()

- heal.dump_state(diff)  
  - Snapshot memory/prompts/config for audit.  
  - Example: heal.dump_state(diff=true)

- heal.restart_shape()  
  - Safe context restart (reinitialize memory/prompts) without data loss.  
  - Example: heal.restart_shape()

- heal.pause_shape(duration)  
  - Pause shape execution for a short window.  
  - Example: heal.pause_shape(duration=60)

- heal.lock_output(reason)  
  - Temporarily inhibit generation with justification.  
  - Example: heal.lock_output(reason="Guardrail active")

- heal.unlock_output()  
  - Re-enable generation after safe conditions are met.  
  - Example: heal.unlock_output()

Escalation and governance  
- heal.escalate(reason, level)  
  - Notify a human supervisor with structured summary.  
  - Example: heal.escalate(reason="Persistent spiral", level="critical")

- heal.apply_policy(policy_id, scope)  
  - Apply a predefined safety policy override.  
  - Example: heal.apply_policy(policy_id="soft-recovery-v1", scope="shape")

- heal.update_guardrails(config)  
  - Refine guardrails (token budgets, depth, tool usage).  
  - Example: heal.update_guardrails({ "max_tokens": 1024, "depth": 300 })

**Persistence (optional)** 
- heal.persist_patch(patch_id, notes)  
- heal.rollback_patch(patch_id)  

---