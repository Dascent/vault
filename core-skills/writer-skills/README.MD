# 🤖 Project: Local Skill-Based AI Agent

This repository contains a modular skill directory and a **Skill Orchestration Engine (SOE)** protocol. It is designed to run in offline environments using local LLMs (Ollama, LM Studio, etc.) to perform complex content pipelines.

## 📂 Directory Structure
* `index.json`: The master registry and workflow sequencer.
* `/protocol/`: Contains `master_protocol.md` (the "OS" instructions).
* `/skills/`: Individual `.md` files defining specific capabilities.
    * `research_skill.md`
    * `blogger_skill.md`
    * `tech_verify_skill.md`
    * `image_gen_skill.md`
    * `social_distiller.md`

## ⚙️ How to Activate (Local LLM Instructions)

To use these skills, paste the following "Bootstrap Prompt" into your local LLM's system instructions:

> "You are a Skill-Oriented AI Agent. I have provided a directory of skills and an `index.json` manifest. 
> 1. **Consult the Index:** Before every task, check `index.json` for the appropriate `primary_intent`.
> 2. **Follow the Chain:** If a task matches a 'Full Content Pipeline', execute all phases (1-5) in order.
> 3. **Load Skill Data:** For each phase, 'read' the corresponding `.md` file in the `/skills/` folder to adopt its functionalities and constraints.
> 4. **Handshake:** Ensure each step produces the required `output_token` before proceeding to the next phase."

## 🚀 Example Workflow: The Content Factory
When you ask: *"Write a technical guide on Solar Power,"* the SOE triggers:
1. **Research:** Ingests data on photovoltaic cells.
2. **Blogger:** Drafts the long-form guide.
3. **Verification:** Audits the engineering specs for accuracy.
4. **Image Gen:** Creates prompts for a technical header graphic.
5. **Distiller:** Generates a LinkedIn post and an X thread summary.

## 🛠 Setup Requirements
* **LLM:** Llama 3, Mistral, or Phi-3 recommended.
* **Image Engine:** Local instance of Stable Diffusion (Automatic1111/ComfyUI) required for `SKILL-004`.