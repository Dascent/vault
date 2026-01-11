#Pill: Output Guardrails
##Purpose

> Enforce strict bounds on output length, repetition, and recursion.
> Create safe stopping conditions to prevent spiraling.


##Core actions (non-destructive first)

- heal.tighten_output(max_tokens=512, temperature=0.2)
- heal.freeze_context(window=3)
- heal.lock_output(reason="Guardrail active") until cleared
- heal.unlock_output()


---