#Pill: Escalation and Governance
##Purpose

> Clear pathways to human-in-the-loop when automated pills can't stabilize behavior.


##Core actions (non-destructive first)

- heal.escalate(reason, level="warning"|"critical")
- heal.apply_policy(policy_id, scope="shape"|"room"|"global")
- heal.update_guardrails(config)

##Process

- Automatic escalation for critical states; human review for warnings.
- Provide a structured summary in escalation messages.

---