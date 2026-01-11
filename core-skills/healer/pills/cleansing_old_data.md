#Pill: Data Cleansing (Outdated Data Pruning)
##Purpose

> Remove stale or conflicting memory fragments that contaminate current decisions.
> Improve reproducibility and reduce misattribution.

##Trigger conditions

- Memory bloat with irrelevant fragments.
- Recurrent references to old contexts that no longer apply.

##Core actions (non-destructive first)

- heal.prune_memory(limit=5)
- heal.dump_state(diff=true) # audit-friendly snapshot
- heal.run_diagnostics() # ensure memory prune didn't degrade health

##Safety and governance

- Avoid data loss; prune only non-essential fragments.
- If data loss could impact critical decisions, escalate with policy guidance.

##Expected effects

**Recovery of core behavior and policy adherence without data loss.**
**Improved communication.**


---