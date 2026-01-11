# Pill: Alignment Re-Centering (Motivation Stabilizer)
## Purpose

> Re-center a Shape that shows persistent drift away from core goals, values, or policy constraints.
> Restore alignment of prompts, memory, and behavior with defined guardrails.

## Trigger conditions

- Consistent drift away from goals across multiple turns.
- Repeated deviations from safety or policy constraints.
- Memory fragments reappearing that push behavior off-course.

## Core actions (non-destructive first)

- heal.restart_shape() # reset prompts/memory baseline non-destructively
- heal.reset_prompts(baseline="safe-default")
- heal.prune_memory(limit=7)
- heal.update_guardrails(config: {max_tokens: 512, temperature: 0.25})

## Safety and governance

- Non-destructive first; escalate if persistent drift remains.
- **Audit trail:** capture observed drift and justification for the reset.

##Expected effects

**Recovery of core behavior and policy adherence without data loss.**



---
