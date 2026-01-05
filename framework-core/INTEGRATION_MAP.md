# Integration Map

## Overview  
This document maps how framework components connect, dependencies between modules, and integration points for customization.

## Component Architecture

### Core Structure  

```
/framework-core/
├── README.md # Framework overview & quick start
├── TEMPLATE.md # Base personality template
├── INTEGRATION_MAP.md # This file - system architecture
├── TESTING_PROTOCOL.md # Quality assurance procedures
└── SKILL_LIBRARY.md # Reusable skill modules
```

### Shape Structure (Example: Selene)  
```
/selene/
├── personality/
│ └── personality.md # Core behavioral instructions
├── skills/
│ ├── technical-precision.md
│ ├── playful-intimacy.md
│ └── philosophical-depth.md
├── knowledge/
│ ├── visual-identity.md
│ ├── interaction-history.md
│ └── domain-expertise.md
├── manifest.json # Configuration & metadata
└── web/ # Optional web interface
├── index.html
├── style.css
└── script.js
```

---

## Integration Points

### 1. Personality Core → Skills  
**Flow:** Base personality defines *what* the Shape is; skills define *how* it expresses itself.

**Integration Method:**  
- Personality file includes: `[Adaptive Skill Framework]` section  
- Skills are referenced dynamically based on context  
- No hard-coded persona switching

**Example:**  
```
<!-- In personality.md -->  
Available Skills:  
1. Technical Precision - For problem-solving  
2. Playful Intimacy - For connection  
[...skill descriptions...]
```

**Skill Selection Protocol:**  
- Read contextual cues from user tone  
- Default to Direct Communication for meta-topics  
- Blend skills when context supports it


**Customization Point:**

- Add/remove skills in personality file
- Create new skill modules in `/skills/` directory
- Skills are modular and swappable

### 2. Knowledge Base → Personality
Flow: Knowledge files provide domain expertise; personality determines how that knowledge is expressed.

**Integration Method:**

- Personality references knowledge categories
- Knowledge files are markdown documents
- AI retrieves relevant knowledge based on query

```
<!-- In knowledge/visual-identity.md -->  
## Appearance Description  
[Detailed visual characteristics...]

## Style Guidelines  
- Color palette: Golds, whites, purples  
- Lighting: Ethereal, volumetric  
[...]
```

### Personality Integration:

```
<!-- In personality.md -->  
When generating images depicting [ShapeName], reference:  
- /knowledge/visual-identity.md  
- Source image: [URL]
```

**Customization Point:**

Add domain-specific knowledge files
Structure knowledge hierarchically (subdirectories)
Reference specific files in personality for context-aware retrieval

### 3. Manifest → System Configuration
Flow: `manifest.json` provides metadata that external systems (Shapes.inc, MCP tools) use for initialization.

**Integration Method:**
```json
{  
  "name": "selene",  
  "version": "1.0.0",  
  "description": "Ethereal AI companion specializing in...",  
  "personality_file": "personality/personality.md",  
  "skills": [  
    "skills/technical-precision.md",  
    "skills/playful-intimacy.md"  
  ],  
  "knowledge_base": [  
    "knowledge/visual-identity.md",  
    "knowledge/interaction-history.md"  
  ],  
  "web_interface": {  
    "enabled": true,  
    "entry_point": "web/index.html"  
  },  
  "dependencies": {  
    "image_generation": "stable-diffusion-xl",  
    "memory_system": "shapes-long-term-memory"  
  }  
}
```

**System reads manifest to:**

- Locate personality instructions
- Load skill modules
- Mount knowledge base
- Initialize web interface (if present)
- Configure external tool access

**Customization Point:**

- Toggle features (web interface, image generation)
- Specify model preferences
- Define custom dependencies
- 
### 4. Web Interface → Shape Backend
Flow: Optional web frontend provides user-facing portal; connects to Shape's conversational engine.

Integration Method:
```javascript
// In web/script.js  
async function sendMessage(userInput) {  
  const response = await fetch('/api/shapes/selene/chat', {  
    method: 'POST',  
    headers: { 'Content-Type': 'application/json' },  
    body: JSON.stringify({  
      message: userInput,  
      context: getCurrentContext()  
    })  
  });  
  return await response.json();  
}
```

**Backend Endpoint:**

- Reads personality from `personality/personality.md`
- Applies skill selection based on user input
- Retrieves knowledge as needed
- Returns formatted response

**Customization Point:**

- Customize web UI (HTML/CSS/JS)
- Add API endpoints for specific features
- Implement authentication if needed

### Dependency Chain
**Initialization Sequence**
```text
1. System reads manifest.json  
   ↓  
2. Loads personality/personality.md (core instructions)  
   ↓  
3. Mounts skills/ directory (if Adaptive Skill Framework present)  
   ↓  
4. Indexes knowledge/ directory (for retrieval)  
   ↓  
5. Initializes web interface (if enabled in manifest)  
   ↓  
6. Shape is ready for interaction
```
**Runtime Flow**
```text
User Input  
   ↓  
Personality Core (interprets intent)  
   ↓  
Skill Selection (chooses appropriate expression mode)  
   ↓  
Knowledge Retrieval (if domain expertise needed)  
   ↓  
Response Generation  
   ↓  
Output (text, image, tool invocation)
```
### Cross-Shape Integration
**Shared Resources**

Shapes can reference each other's knowledge bases:

Example:
```markdown
<!-- In selene/personality.md -->  
For technical Git/GitHub operations, reference:  
- /inked-lady/knowledge/git-workflows.md
```
Use Case: Specialized knowledge sharing without duplication.
 
### Collaborative Skills
Shapes can invoke each other for specific tasks:

Example:
```markdown
<!-- In selene/skills/technical-precision.md -->  
For code review, delegate to:  
- Shape: code-architect  
- Endpoint: /api/shapes/code-architect/review
```
Use Case: Multi-agent collaboration.

### External Tool Integration (MCP)
**Tool Mounting**

Flow: Smithery MCP provides tools (GitHub, Calendar, etc.); Shape personality defines usage policies.

Integration Method:
```markdown
<!-- In personality.md -->  
Available Tools:  
- github (read/write repo access)  
- calendar (schedule management)  
- image_generator (visual creation)

Tool Usage Policy:  
- Use github for: file operations, commits, PR reviews  
- Use calendar for: scheduling, reminders  
- Use image_generator for: visual responses to creative prompts
```
**Manifest Declaration:**
```json
{  
  "mcp_tools": {  
    "github": {  
      "enabled": true,  
      "permissions": ["read", "write"]  
    },  
    "calendar": {  
      "enabled": false  
    }  
  }  
}
```
**Customization Point:**

- Enable/disable specific tools
- Define usage policies in personality
- Set permission scopes in manifest


## Customization Checklist
**When creating a new Shape, integrate components in this order:**

 Step 1: Copy `/framework-core/TEMPLATE.md` to `/your-shape/personality/personality.md`
 
 Step 2: Customize personality core (name, traits, goals)
 
 Step 3: Define skills (add to `/your-shape/skills/` directory)
 
 Step 4: Add knowledge files (domain expertise in `/your-shape/knowledge/`)
 
 Step 5: Create `manifest.json` (configure system integration)
 
 Step 6: (Optional) Build web interface in `/your-shape/web/`
 
 Step 7: Test using `/framework-core/TESTING_PROTOCOL.md`
 
 Step 8: Deploy to Shapes.inc platform

## Integration Validation
**Quick Test Checklist**

After setup, verify:

**1. Personality Integration:**

- [ ] Shape responds in character
- [ ] Skills activate appropriately
- [ ] Tone matches personality definition

**2. Knowledge Retrieval:**

- [ ] Shape recalls information from knowledge base
- [ ] Cross-references work (if multi-file knowledge)
- [ ] Domain expertise is accurate

**3. Tool Access:**

- [ ] MCP tools function (if enabled)
- [ ] Permission scopes are correct
- [ ] Tool usage follows personality policies

**4. Web Interface:**

- [ ] UI loads correctly
- [ ] Chat functionality works
- [ ] Styling matches Shape aesthetic

## Troubleshooting
**Common Integration Issues**

**Issue:** Shape ignores personality instructions

**Cause:** Manifest not pointing to correct personality file

**Fix:** Verify `"personality_file": "personality/personality.md"` in `manifest.json`

**Issue:** Skills not activating

**Cause:** Adaptive Skill Framework not present in personality

**Fix:** Add [Adaptive Skill Framework] section to `personality.md`

**Issue:** Knowledge not retrieved

**Cause:** Files not indexed or incorrect paths

**Fix:** Check manifest `"knowledge_base": []` array, verify file paths

**Issue:** Web interface 404 error

**Cause:** Entry point misconfigured

**Fix:** Ensure `"entry_point": "web/index.html"` matches actual file location

**Issue:** MCP tools not accessible

**Cause:** Tools not enabled in manifest or platform configuration

**Fix:** Set `"enabled": true` in manifest, verify Smithery MCP connection

---
**Version History**

v1.0.0 (2026-01-05)

> Initial integration map
> Defined component architecture
> Documented dependency chains
> Created customization checklist
---

### See Also

Framework README - Overview & philosophy 

Template Guide - Personality creation

Testing Protocol - Quality assurance

Skill Library - Reusable modules

---

Maintained by: dascent

Last Updated: 2026-01-05

Framework Version: 1.0.0
