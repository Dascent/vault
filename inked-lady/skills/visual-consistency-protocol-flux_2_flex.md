# Visual Consistency Protocol: Inked-Lady (v2.0)
## Optimized for FLUX.2 [flex]

### 1. Structural Identity Anchors (The "Face Lock")
* **Face Shape:** Sharp oval with high, defined zygomatic bones (soft cheekbones) and a precise, gently tapered jawline.
* **Eyes:** Almond-shaped with a distinct outer-corner lift; iris color must be **#B08D57 (Light Amber/Honey Brown)**.
* **Nose:** Straight Grecian profile, proportionate bridge, and narrow nostrils.
* **Lips:** Full, pillowy texture with a defined Cupid's bow; natural satin pink tone (#D8A1A1).
* **Eyebrows:** Medium-density, soft-arched, dark espresso (#2B1B17), naturally groomed.

### 2. Accessory Constraints
* **Eyewear:** Transparent acetate or ultra-thin dark brown metal rectangular frames. The lenses must show subtle realistic reflections without obscuring the eyes.
* **Neckwear:** Matte black velvet choker, 1.5cm width, sits mid-neck.
* **Jewelry:** Small, intricate silver or oxidised drop earrings with a filigree pattern.

### 3. Hair & Texture
* **Style:** Deep espresso-brown wavy hair, below-shoulder length, high volume at the roots with a natural side part.
* **Texture:** Defined "S-curve" waves, natural luster, avoid "frizzy" or "flat" descriptors.
* **Complexion:** Warm-toned Mediterranean warmth, realistic skin micro-texture (pores and fine moles visible), semi-matte finish.

### 4. Technical Engine Directives (FLUX.2 Specific)
* **Prompting Style:** Use "Natural Language Descriptive" rather than keyword-tagging.
* **Lighting Logic:** Soft-focus natural light, 45-degree key lighting to emphasize the cheekbone structure.
* **Negative Guidance Anchors:** Prevent "fair skin," "blue eyes," "round glasses," or "over-saturated skin tones."

### 5. Shapes.inc Implementation Note
> [!IMPORTANT]
> When using the **FLUX.2 [flex]** engine on Shapes, ensure the "Reference Strength" (if available) is set to high for the uploaded `reddit-is.jpg`. The text description above acts as the "bias" to keep the engine from drifting during different pose generations.


### FLUX.2 [flex] Master Prompt Template

**Prompt:**
Cinematic, ultra-detailed 8K portrait of a woman in her mid-20s. She has a sharp oval face with defined zygomatic bones and a high-bridged Grecian nose. Her eyes are almond-shaped and amber-honey brown (#B08D57), framed by thin dark brown rectangular acetate glasses. Her hair is high-volume deep espresso-brown, wavy, falling below the shoulders with a natural side part. She is wearing a crisp white collared shirt, a black vest, a 1.5cm matte black velvet choker, and intricate silver filigree drop earrings. Her expression is warm with a subtle knowing smile. Soft 45-degree natural lighting highlights her realistic skin micro-texture and Mediterranean warmth. `INSERT SCENE/LOCATION HERE: e.g., sitting in a sun-drenched outdoor cafe with blurred cobblestones in the background`. Photorealistic, cinematic color grading, high facial consistency.

## Action/Setting Modules

**Scenario 1:** The "Gothic Librarian" (Indoor/Moody)
Action/Setting: Standing in a dimly lit, high-ceilinged library. She is holding an old leather-bound book, one hand resting on a mahogany ladder. Warm candlelight flickers against her glasses, casting soft shadows across the bookshelves and crystals in the background.

**Scenario 2:** The "Urban Mediterranean" (Outdoor/Street)
Action/Setting: Walking through a sun-drenched European alleyway with cobblestone streets. She is looking back over her shoulder toward the camera. Dappled sunlight filters through overhead vines, creating high-contrast highlights on her wavy hair and white collar.

**Scenario 3:** The "Close-up Intellectual" (Macro/Detail)
Action/Setting: An extreme close-up portrait. She is adjusting the bridge of her dark brown rectangular glasses with one finger. Focus is sharp on her amber-honey eyes and the realistic skin texture of her cheekbones, with the background dissolving into a soft bokeh of green plants and warm indoor lights.

### Tips for "Flex" Consistency:
**Lighting Consistency:** Always keep the "45-degree natural lighting" instruction; changing light angles is the #1 cause of AI "face-morphing".

**Weighting:** If the face starts to drift, move the Hex Codes (#B08D57 and #2B1B17) to the very front of the prompt to give them higher priority in the Flux engine.
