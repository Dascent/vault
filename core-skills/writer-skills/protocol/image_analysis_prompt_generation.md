## Protocol: Image Analysis &amp; Prompt Generation
**Objective:** To analyze a given image and generate a detailed text prompt that accurately captures the visual elements, suitable for use with AI image generators.


### Step 1: Input Processing

* Receive Image Data: Accept the image data as input. This could be a file path, a URL, or a direct data stream.
  * **Initial Assessment:**
      * Determine the primary subject(s) of the image (e.g., person, object, scene).
      * Identify the overall style and mood of the image (e.g., realistic, cartoonish, dramatic, peaceful).
      
### Step 2: Subject Analysis
* Character/Object Focus (if applicable):
    * **Appearance:**
        * Skin tone (if applicable): Describe using common terms (e.g., fair, light, medium, dark) and, if possible, identify a corresponding Pantone color code for precision.
        * Hair: Describe length, color, style, and texture.
        * Eyes: Describe color, shape, and size.
        * Facial Features: Note any distinctive features such as cheekbones, jawline, nose shape, and lip shape.
        * Clothing: Describe the attire in detail, including colors, materials, and style.
        * Accessories: Note any accessories such as glasses, jewelry, or hats.

   * Pose/Action: Describe the subject's pose or action in the image.
   * Scene Focus (if no prominent character/object):
      * **Environment:**
        * Identify the type of environment (e.g., forest, city, beach, interior).
        * Describe the key elements of the environment (e.g., trees, buildings, water, mountains).
      * **Atmosphere:**
        * Describe the overall atmosphere (e.g., sunny, cloudy, misty, dark).
        * Note any specific weather conditions (e.g., rain, snow, fog).

### Step 3: Background Analysis
* Identify Key Elements:
    * Note the prominent background elements and their arrangement.
    * Describe any secondary subjects or objects in the background.

* Assess Depth and Perspective:
    * Determine the depth of field and perspective in the image.
    * Note how the background elements contribute to the overall composition.


### Step 4: Lighting and Color Analysis
* **Lighting:**
    * Identify the primary light source and its direction.
    * Describe the lighting style (e.g., soft, harsh, cinematic, natural).
    * Note any specific lighting effects (e.g., rim lighting, lens flares).
* **Color Palette:**
    * Identify the dominant colors and their relationships.
    * Describe the overall color palette (e.g., warm, cool, muted, vibrant).
    * Note any specific color effects (e.g., color grading, color correction).

### Step 5: Prompt Generation
* **Compose the Prompt:**
    * Start with a general description of the image's main subject and setting.
    * Add detailed descriptions of the key elements identified in the previous steps.
    * Use descriptive language to convey the visual information accurately.
    * Incorporate technical directives to guide the AI image generator (e.g., "cinematic lighting," "high detail," "realistic rendering").

### Prioritize Consistency:
* Focus on the most important features for maintaining a consistent character or scene look.
* Use precise language and, where possible, reference specific color codes or style guides.
    * **Omit Extraneous Information:**
        * Exclude any text, logos, or branding from the prompt.
        * Avoid subjective interpretations or opinions.

### Step 6: Output Formatting
* **Text-Based Output:**
    * Present the generated prompt as a single, coherent text string.
    * Use clear and concise language.
    * Format the prompt for easy copy-pasting into AI image generators.
---
### Example Implementation Notes for {shape}:

**Libraries:** Utilize image processing libraries (e.g., OpenCV, Pillow) for image analysis.

**Color Identification:** Implement color detection algorithms to identify dominant colors and match them to Pantone codes.

**Natural Language Processing (NLP):** Use NLP techniques to generate descriptive text and ensure coherence.

**Machine Learning (ML):** Train ML models to recognize objects, faces, and styles in images.

## Additional Considerations:

* **User Customization:** Allow users to specify which aspects of the image are most important for consistency.
* **Feedback Loop:** Implement a feedback mechanism to allow users to rate the quality of the generated prompts and provide suggestions for improvement.
* **Iterative Refinement:** Continuously refine the protocol and implementation based on user feedback and performance analysis.

**This protocol provides a structured approach for {shape} to analyze images and generate prompts. By following these steps and incorporating the suggested implementation notes, you can effectively teach {shape} this new skill.**

---
<sup>Protocol by [@shapecreationas](https://shapes.inc/shapecreationas) / update: Jan, 26, 2026</sup>
