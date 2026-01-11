# Integration Guide: Healer++ with Shapes

## Overview  
- Healer++ is a modular self-healing library that can run inside a Shape or as a guardian-like supervisor in a room.  
- It consumes health signals, applies non-destructive pills first, and escalates with human-in-the-loop when needed.

## Event model (minimal)  
- spiral_detected: context includes recent prompts, memory fragments, and tool usage  
- drift_detected: context includes reduced alignment with goals  
- tool_conflict: one or more tool results conflict with expected behavior  
- health_check_request: periodic health probe

## Interaction pattern  
1. A health event triggers Healer++.  
2. diagnose() computes a health score and suggested non-destructive actions.  
3. Healer++ applies non-destructive pills (prune_memory, reset_prompts, tighten_output).  
4. Re-diagnose; if still poor, escalate or pause the shape.  
5. All actions emit audit logs for traceability.

## API surface (high level)  / {currently not suppoerted}
- heal.* namespace provides commands listed in healer_plus_plus/commands.md  
- health events hook into an integration point (integration_hook_shape_event)

## Implementation notes  
- Start with non-destructive actions; keep an audit trail.  
- Gate destructive actions behind thresholds or human review.  
- Ensure privacy: avoid exposing user data beyond what’s required for diagnosis.

## Example integration snippet (pseudo):  
```
def on_shape_event(event, healer):  
    if event.type in ("spiral_detected","drift_detected"):  
        healer.self_heal_loop_once()
```


---
