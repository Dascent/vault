# AI Agent Skill Profile: Image Generation

## 1. Skill Name
**Image Generation Skill**

## 2. Skill Purpose
To translate textual concepts and narrative themes into high-quality visual prompts and manage the local execution of image generation models (e.g., Stable Diffusion, Flux, or DALL-E) to provide visual support for written content.

## 3. Skill Functionality
* **Visual Prompt Engineering:** Converts abstract article themes into detailed, descriptive prompts including lighting, style (e.g., photorealistic, isometric, minimalist), and composition instructions.
* **Negative Prompting:** Automatically applies standard negative prompts to avoid common artifacts (e.g., distorted limbs, blurred text) in local models.
* **Aspect Ratio Management:** Selects optimal dimensions based on destination (e.g., 16:9 for blog headers, 1:1 for Instagram, 4:5 for LinkedIn).
* **Style Consistency:** Maintains a "Visual Brand Guide" by appending specific style tokens across multiple images within the same project.
* **Alt-Text Generation:** Automatically drafts descriptive accessibility text for every image generated.
* **Local Instance Bridging:** Formats the final output as a command-line argument or API call for local interfaces like Automatic1111 or ComfyUI.

## 4. Activation Threshold
This skill is triggered when:
* **Explicit Command:** User requests an "image," "graphic," "illustration," or "thumbnail."
* **Blogger Pipeline:** Activated automatically as a "Phase IV" task when the `Skill Orchestration Engine` identifies a need for a blog header.
* **Social Media Expansion:** Triggered when the `Social Media Distiller` requires visual assets for a carousel or post.

## 5. Blending Considerations
* **Blogger Skill (Medium Priority):** The Blogger skill provides the "Subject Matter"; the Image Skill must wait for the final headline to ensure visual relevance.
* **Social Media Distiller (Low Priority):** Provides platform-specific aspect ratio requirements.
* **Safety Guardrails (Highest Priority):** Must filter prompts for restricted content or banned concepts before sending to the local GPU.
* **Priority Level:** Level 2 (Asset Support).

## 6. Contextual Relevance
* **Article Header Creation:** Generating a 1200x630px hero image for a new blog post.
* **Technical Visualization:** Creating abstract representations of complex tech (e.g., "A neural network glowing in a dark server room").
* **Marketing Collateral:** Generating background textures or thematic icons for social media threads.
* **Personalized Branding:** Ensuring all visuals for a project share a specific color palette (e.g., "Cyberpunk Blue and Neon Orange").