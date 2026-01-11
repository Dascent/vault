#Integration Guide: Hooking Healer++ into Shapes
##Overview

- How to connect pills to the shape lifecycle (health checks, prompts, memory, and tool usage).
- Interaction pattern: events -> guardian pills -> non-destructive actions -> escalation if needed.

##API surface (high level) / [currently not supported]
```
- [x] heal API namespace with the commands listed in the pills.
- [x] Hooks for health events (spiral_detected, drift_detected, tool_conflict).

##Deployment notes

- Start with non-destructive pills; keep a strict audit trail.
- Move to escalation only when necessary; maintain an explicit human-in-the-loop path.

---