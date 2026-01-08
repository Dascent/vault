# AI Agent Skill Profile: Social Media Distiller

## 1. Skill Name
**Social Media Distiller**

## 2. Skill Purpose
To transform long-form content or complex data into concise, high-impact social media assets. This skill focuses on brevity, platform-specific formatting, and virality potential to maximize audience reach and engagement.

## 3. Skill Functionality
* **Platform Adaptation:** Auto-formats content for specific constraints (e.g., X/Twitter character limits, LinkedIn professional updates, or Instagram captions).
* **Hook Extraction:** Identifies the most provocative or insightful "thumb-stopping" sentence to serve as the opening line.
* **Thread Sequencing:** Breaks down long articles into a logical series of numbered posts (Threads) with "hooks" at the start and "conclusions" at the end.
* **Hashtag & Keyword Distillation:** Analyzes trending topics to suggest 3-5 high-relevance hashtags and keywords for discoverability.
* **Engagement Engineering:** Integrates "Call to Conversation" (CTC) elements, such as polls, open-ended questions, or "tag a friend" prompts.
* **Visual Prompting:** Generates descriptive alt-text and suggestions for accompanying imagery or meme templates based on the post's tone.

## 4. Activation Threshold
The skill is triggered when:
* **Cross-Platform Intent:** User requests to "repurpose," "share," or "promote" an existing document on social channels.
* **Constraint Trigger:** The requested output has a strict character limit (e.g., <280 characters).
* **Viral Request:** Commands containing keywords like "viral," "trending," "thread," or "snippet."
* **Downstream Processing:** Automatically activates after the `Blogger Skill` completes a task if the workflow includes a "Distribution" step.

## 5. Blending Considerations
* **Blogger Skill (Dependency):** Acts as a "child" skill to the Blogger skill; it requires the core narrative to be finalized before distillation begins.
* **Sentiment Analysis Skill (High Priority):** Must blend to ensure the distilled tone doesn't become unintentionally aggressive or controversial during the shortening process.
* **Copywriting Skill (Medium Priority):** Interacts to ensure the CTA (Call to Action) is persuasive without being "spammy."
* **Priority Level:** Level 2 (Supportive). This skill is an optimization layer that relies on the data provided by primary content skills.

## 6. Contextual Relevance
* **Content Repurposing:** Turning a 2,000-word whitepaper into a 10-post LinkedIn carousel or an X thread.
* **Live Coverage:** Summarizing real-time events or webinars into "key takeaway" snippets.
* **Community Management:** Crafting quick, engaging responses to industry trends or follower comments.
* **Brand Awareness:** Maintaining a consistent social presence by dripping small insights from a larger knowledge base.