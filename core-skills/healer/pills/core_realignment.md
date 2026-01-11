#Pill: Core Realignment (Values and Settings)
##Purpose

> Realign Shape behavior with core values and global style guidelines.
> Ensure consistent tone, safety, and decision boundaries.

##Trigger conditions

- Inconsistent tone, conflicting system prompts, consistent policy violations.

##Core actions (non-destructive first)

- heal.update_guardrails(config: {token_budget: 600, depth_limit: 200})
- heal.tighten_output(max_tokens=400, temperature=0.2)
- heal.freeze_context(window=4)

##Safety and governance

- If misalignment recurs, escalate to `guardian` and consider a policy override.

##Expected effects

**Recovery of core behavior and policy.**


---