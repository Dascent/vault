# Protocol Name: Skill Orchestration Engine (SOE)
## Version: 1.0.0 (Local/Offline Optimized)

## 1. Protocol Purpose
To provide a standardized logic for AI agents to discover, activate, and sequence skills from a local or remote directory. The SOE ensures that a single high-level prompt (e.g., "Write a technical article") triggers a multi-skill workflow without requiring manual user intervention for each step.

## 2. Skill Discovery & Indexing
The agent must maintain a `skills_index.json` or `manifest.md` within the root directory.
* **Scanning:** Upon initialization, the agent parses the `/skills` folder.
* **Metadata Mapping:** Each skill must export its "Activation Thresholds" and "Blending Considerations" to the master index.
* **Local LLM Constraint:** In offline environments, the SOE prioritizes skills with low-parameter requirements or those that utilize local Python scripts over API-dependent tools.

## 3. Orchestration Logic (The "Chain of Thought" Trigger)
When a task is received, the SOE follows a **Sequence-to-Parallel (StP)** logic:

1.  **Intent Decomposition:** Break the user prompt into sub-tasks.
    * *Example:* "Technical Article" -> [Research] + [Drafting] + [Visuals] + [Distribution].
2.  **Primary Skill Assignment:** Identify the "Lead Skill" (e.g., `Blogger Skill`).
3.  **Dependency Mapping:** Identify "Downstream Skills" based on the Lead Skill’s `Blending Considerations`.
    * *If `Blogger Skill` is active → Automatically queue `Social Media Distiller`.*
    * *If content is technical → Automatically queue `Technical Verification Skill`.*
4.  **Resource Allocation:** Check if the local environment supports the required tools (e.g., Local Stable Diffusion for `Image Generation Skill`).

## 4. Operational Workflow: "The Skill Pipeline"
The SOE executes skills in the following phases:

| Phase | Action | Description |
| :--- | :--- | :--- |
| **Phase I** | **Ingestion** | Pulls raw data via `Research Skill` or User Input. |
| **Phase II** | **Synthesis** | The `Lead Skill` (e.g., Blogger) creates the core asset. |
| **Phase III** | **Refinement** | Secondary skills (e.g., SEO, Technical Review) audit the asset. |
| **Phase IV** | **Expansion** | `Social Media Distiller` and `Image Gen` create derivative assets. |
| **Phase V** | **Packaging** | All outputs are bundled into a final `.zip` or directory for the user. |

## 5. Conflict Resolution & Priority
If two skills attempt to modify the same text block:
* **Hard Priority:** Safety/Guardrail skills > Technical Accuracy > Creative Style.
* **Sequential Locking:** The `Social Media Distiller` cannot modify text until the `Blogger Skill` has released its "Write Lock" on the draft.

## 6. Activation Threshold (Master Level)
* **Trigger:** Any prompt that cannot be answered in a single conversational turn (< 100 words) or requires a specific output format (Markdown, Code, Image).
* **Contextual Awareness:** The SOE monitors the "Project State." If the project is "Article Creation," the SOE remains active until the final "Social Media Distiller" output is generated.