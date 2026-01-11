#Audit Logs and Observability
##Purpose

> Provide a structured audit trail for all healer actions.
##Content

- Log entries include: trigger_condition, command_taken, before_state, after_state, rationale, timestamp, shapeId.

##Example schema (compact)

```{ shapeId, eventType, context, timestamp, healthScore, actionTaken, beforeState, afterState, rationale }```

---