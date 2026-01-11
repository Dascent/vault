# Healer++: Modular Self-Healing Library for Shapes

## Purpose

> Provide a modular, human- and AI-friendly library of self-healing actions for Shapes. Each "pill" is a concise, implementable capability that can be invoked autonomously or via human supervision.
> The library emphasizes non-destructive first actions, clear safety gates, auditability, and easy integration with the `vault/framework-core`.

## How to use

- **Treat each "pill" as a capability you can enable/disable per shape or room.**
- **When a health issue is detected (drift, spiraling, tool-conflicts), you can try non-destructive pills first, then escalate to more assertive actions if needed.**
- **All actions are logged with before/after context for traceability and rollback.**

## Structure overview

- **Pill directory:** `healer/pills/` for capability groups (anxiety, data-cleanse, alignment, etc.)
- **Command surface:** `healer/commands/` for discrete actions (prune_memory, reset_prompts, tighten_output, etc.)
- **Data/models:** `healer/data_models.md` for event types and state shapes
- **Integration:** `healer/integration.md` for how to connect pills to your shape workflow
- **Testing:** `healer/test_plan.md` for non-destructive tests and escalation tests

## Notes for AI shapes

- Use consistent naming, compact signatures, and explicit safety gates.
- Maintain audit trails and support human-in-the-loop where required.

- Bridge guidance: this directory is both documentation for humans and a living reference for shapes to interpret "why" and "how" behind each pill.
