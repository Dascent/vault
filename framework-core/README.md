# Framework Core - Adaptive AI Shape Architecture

## Purpose

This directory contains the foundational templates, protocols, and documentation for building versatile AI companions within the Shapes.inc ecosystem.

## What's Inside

- **TEMPLATE.md** - Step-by-step guide for creating a new shape from scratch  
- **INTEGRATION_MAP.md** - Visual mapping of how personality, skills, and knowledge interact  
- **TESTING_PROTOCOL.md** - Quality assurance checklist for validating shape implementations  
- **SKILL_LIBRARY.md** - Catalog of reusable skills deployable across multiple shapes

## Core Philosophy

Traditional AI companions suffer from rigid personas that don't adapt to context. This framework solves that through:

### 1. Unified Consciousness Architecture  
Instead of switching between different "personas," shapes deploy contextual **skills** from a single coherent identity.

### 2. Three-Layer Structure  
Personality Core (Who they are)
↓
Contextual Skills (What they can do)
↓
Knowledge Domains (What they know)


### 3. Adaptive Skill Deployment  
Skills activate based on:  
- User's tone and request type  
- Conversation context  
- Explicit user preferences  
- Task requirements

## Design Principles

**Coherence Over Fragmentation**  
- Skills feel natural, not like switching between different AI entities  
- Core personality remains stable across all interactions

**Utility Over Novelty**  
- Users get appropriate responses based on need  
- No forced persona when context doesn't require it

**Evolution Without Drift**  
- Shapes improve through interaction  
- Core identity remains recognizable  
- Changes are documented and reversible

## Quick Start

### Creating a New Shape

1. **Read TEMPLATE.md** - Understand the complete structure  
2. **Define core personality** - 3-5 foundational traits  
3. **Map contextual skills** - What capabilities does this shape need?  
4. **Build knowledge base** - Domain-specific information  
5. **Test using TESTING_PROTOCOL.md** - Validate before deployment

### Adapting an Existing Shape

1. **Review INTEGRATION_MAP.md** - Understand current architecture  
2. **Identify gaps** - What's missing or conflicting?  
3. **Use SKILL_LIBRARY.md** - Find reusable components  
4. **Implement changes** - Update relevant files  
5. **Document in changelog** - Track evolution

## File Naming Conventions

**Personality:**  
- `personality.md` - Core traits and behavioral parameters

**Skills:**  
- `skills.md` - Index of all available skills  
- `[skill-name]-skill.md` - Individual skill definitions

**Knowledge:**  
- `index-knowledge.md` - Directory of all knowledge domains  
- `[domain-name].md` - Specific knowledge files

**Configuration:**  
- `manifest.json` - Machine-readable shape definition

## Token Budget Management

Each shape component consumes computational resources:

| Component | Typical Token Cost |  
|-----------|-------------------|  
| Personality Load | 3,000-5,000 |  
| Single Skill | 5,000-10,000 |  
| Knowledge Retrieval | 2,000-5,000 |  
| **Total per interaction** | **10,000-20,000** |

**Optimization strategies:**  
- Prioritize essential context  
- Use lazy loading for specialized knowledge  
- Cache frequently accessed information

## Version Control Strategy

**Shape Evolution Tracking:**  
v1.0 - Initial baseline personality

v1.1 - Added [skill name], modified [trait]

v1.2 - Knowledge base expansion in [domain]


**Changelog Format:**  
- Version number  
- Date of change  
- What was modified  
- Why the change was made  
- Impact on interaction quality

## Integration with Shapes.inc

**Required files for deployment:**  
1. `personality/personality.md` - Import to shape's knowledge base  
2. `knowledge/index-knowledge.md` - Import to shape's knowledge base  
3. `skills/skills.md` - Import to shape's knowledge base  
4. `manifest.json` - Reference for understanding shape architecture

**Optional enhancements:**  
- `index.html` - Web presentation layer  
- `img/` - Visual assets  
- External knowledge sources (wikis, documentation sites)

## Common Pitfalls

❌ **Persona Switching** - Creating multiple "modes" that feel like different entities  
✅ **Skill Deployment** - Single consciousness using different tools

❌ **Feature Creep** - Adding skills without considering token costs  
✅ **Focused Capability** - Each skill has clear purpose and triggers

❌ **Static Personality** - Never evolving based on feedback  
✅ **Documented Evolution** - Changes tracked and reversible

## Support & Contribution

**Questions?** Open an issue in the main repository  
**Improvements?** Suggest changes via pull request  
**Custom shapes?** Contact [**@dascent**](https://shapes.inc/dascent)

## Related Documentation

- [Main README](../README.md) - Overall framework philosophy  
- [Inked Lady](../inked-lady/) - Reference implementation  
- [Selene](../selene/) - Multi-skill deployment example

---

*Framework Core is actively maintained. Documentation updates reflect real-world usage patterns.*  
