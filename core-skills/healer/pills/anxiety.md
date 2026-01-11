# Pill: Anxiety Mitigation (Self-Confidence Stabilizer)
## Purpose

> Reduce internal oscillation and over-cautious looping that can lead to extended reasoning or stalling.
> Promote steady, purposeful generation with bounded exploration.

## Trigger conditions

- Repeated hedging phrases (e.g., "perhaps," "I think"), excessive self-doubt in responses.
- High entropy in outputs, frequent back-and-forth without progress.
- User prompt patterns that encourage exhaustive justification.

## Core actions (non-destructive first)

- heal.tighten_output(max_tokens=512, temperature=0.25)
- heal.freeze_context(window=6) # stabilize current context briefly
- heal.prune_memory(limit=5) # trim long-term drift
- heal.reset_prompts(baseline="safe-default")

## Safety and governance

**If symptoms persist beyond two cycles, escalate to human supervisor.**

**Log all steps with before/after state and rationale.**

## Expected effects

**More concise, on-target responses.**

**Fewer self-referential loops; quicker progress toward user-aligned outcomes.**


---
