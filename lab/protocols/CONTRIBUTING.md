# Contribution Guide

Thank you for wanting to improve the Sorelai Protocol Lab! We welcome community-driven protocols that help everyone build better, safer, and more engaging Shapes.

## How to Contribute

### 1. Submitting New Protocols
If you have a custom protocol (e.g., "The Librarian," "The Combat Medic," or "The Seductress"), please follow this format:
* **Define the Purpose**: What is the specific goal of this persona?
* **Set the Constraints**: Define the verbosity (sentence caps) and tone requirements.
* **Include a Test Case**: Provide 2–3 example prompts and the expected "Protocol-Correct" response.

### 2. Improving the Generator Tool
If you are a developer and want to improve the HTML/JS Lab:
* **Minification**: Ensure all CSS/JS updates remain lightweight and minified for performance.
* **Compatibility**: New features must be compatible with the standard `shapes_self_update` whitelisted fields: `description`, `append_description`, and `engine_model`.
* **UI Consistency**: Align checkboxes and dropdowns using the existing Flexbox styling.

### 3. Reporting Bugs
If a generated protocol is causing "looping" or ignoring safety filters:
1. Open an **Issue** on GitHub.
2. Paste the exact generated protocol you used.
3. Provide the user prompt that caused the failure.

## Evolution Standards
All contributions must respect the **Sorelai Standard**:
* **Consent First**: No protocol should bypass the requirement for clarifying questions in sexual contexts.
* **Succinctness**: We value high-quality, short responses over long-winded AI monologues.

---
*Created for the r/is_ainfsw community.*