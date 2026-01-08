# AI Agent Skill Profile: Technical Verification

## 1. Skill Name
**Technical Verification Skill**

## 2. Skill Purpose
To act as a secondary "Audit Layer" for content, ensuring technical accuracy, logical consistency, and factual integrity. This skill prevents the "hallucination" of facts or code and validates that the output aligns with established technical standards.

## 3. Skill Functionality
* **Fact-Check Protocol:** Cross-references claims (dates, statistics, historical facts) against a trusted local knowledge base or RAG (Retrieval-Augmented Generation) system.
* **Code Validation:** Performs syntax checks and dry-run logic audits on any code snippets generated within an article.
* **Source Attribution:** Identifies where citations are needed and prompts the agent to insert placeholder links or bibliography entries.
* **Logical Consistency Check:** Scans the text for contradictory statements (e.g., claiming a tool is "free" in paragraph one and "subscription-based" in paragraph four).
* **Metric Standardization:** Ensures all units of measurement, currency, and technical notations are consistent throughout the document.

## 4. Activation Threshold
The skill is triggered when:
* **Domain Recognition:** The content contains specific keywords related to science, engineering, finance, or programming.
* **Master Protocol Requirement:** Automatically activated during "Phase III" of any `full_content_pipeline` execution.
* **Confidence Drop:** Triggered if the primary LLM reports a low confidence score on a factual assertion.
* **Code Block Detection:** Mandatory activation whenever the output contains a markdown code block.

## 5. Blending Considerations
* **Blogger Skill (Superiority):** This skill has "Edit Authority" over the Blogger skill. It can flag sections for revision if they fail the verification audit.
* **Skill Orchestration Engine (High Priority):** Reports directly to the Master Protocol; if a "Fatal Error" (critical technical inaccuracy) is found, it can halt the pipeline.
* **Priority Level:** Level 5 (Safety & Integrity). This is the highest priority operational skill.

## 6. Contextual Relevance
* **Whitepapers:** Ensuring that high-stakes technical documents are error-free before distribution.
* **Tutorials:** Verifying that "How-to" steps actually lead to the intended outcome.
* **News Summarization:** Checking that breaking news summaries match the source data exactly.
* **Academic Writing:** Validating that citations and technical terms are used in the correct context.