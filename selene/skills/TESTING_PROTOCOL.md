# Testing Protocol

## Overview  
This document defines quality assurance procedures for Shape development, validation protocols, testing checklists, and iteration guidelines to ensure robust, consistent AI companion experiences.

## Testing Philosophy

### Core Principles  
1. **Iterative Refinement** - Test early, test often, improve continuously  
2. **Multi-Context Validation** - Shapes must perform across diverse scenarios  
3. **User-Centric Quality** - Focus on actual user experience, not theoretical perfection  
4. **Documented Evolution** - Track what works, what doesn't, and why

### Testing Stages  
```
Development → Unit Testing → Integration Testing → User Validation → Production Deployment
```

Each stage has specific validation criteria and success metrics.

---

## Pre-Deployment Checklist

### Phase 1: Component Validation

#### Personality Core  
- [ ] **Identity Consistency** - Shape maintains character across 20+ message exchanges  
- [ ] **Tone Accuracy** - Responses match defined personality traits  
- [ ] **Boundary Respect** - Shape declines inappropriate requests gracefully  
- [ ] **Context Retention** - References earlier conversation points accurately  
- [ ] **Skill Activation** - Appropriate skills deploy based on context

**Test Method:**  
1. Engage in varied conversation topics (technical, emotional, playful, serious)
2. Note any character breaks or inconsistent responses
3. Verify skill transitions are smooth and contextually appropriate


**Pass Criteria:**  
- 90%+ responses feel "in character"  
- No jarring tone shifts without contextual justification  
- Skills blend naturally (no robotic switching)

---

#### Knowledge Base  
- [ ] **Retrieval Accuracy** - Shape recalls correct information when prompted  
- [ ] **Source Attribution** - References knowledge files appropriately  
- [ ] **Domain Expertise** - Demonstrates specialized knowledge in defined areas  
- [ ] **Graceful Unknowns** - Acknowledges limitations honestly when outside expertise

**Test Method:**  
1. Ask questions requiring knowledge base information
2. Test edge cases (ambiguous queries, related but distinct topics)
3. Verify citations/references are accurate
4. Ask questions outside knowledge domain


**Pass Criteria:**  
- 95%+ accuracy on domain-specific queries  
- Clear acknowledgment when information is unavailable  
- No hallucinated facts or false confidence

---

#### Skill Modules  
- [ ] **Contextual Activation** - Skills trigger appropriately based on user input  
- [ ] **Smooth Blending** - Multiple skills can operate simultaneously when needed  
- [ ] **No Contamination** - Technical precision doesn't bleed into playful intimacy, etc.  
- [ ] **Explicit Override** - User can request specific skill deployment

**Test Method:**  
1. Craft prompts designed to trigger specific skills
2. Test ambiguous prompts requiring skill blending
3. Explicitly request skill switches ("respond more playfully", "be direct")
4. Check for inappropriate skill activation


**Pass Criteria:**  
- Correct skill deploys 90%+ of the time  
- Skill blending feels natural, not disjointed  
- User requests for skill changes are honored

---

### Phase 2: Integration Testing

#### Cross-Component Interaction  
- [ ] **Personality-Skills Harmony** - Skills express personality, not override it  
- [ ] **Knowledge-Personality Integration** - Expertise delivery matches character tone  
- [ ] **Manifest Configuration** - System respects settings in `manifest.json`  
- [ ] **Tool Access** - MCP tools function as expected (if enabled)

**Test Method:**  
1. Verify personality traits persist across skill deployments
2. Test knowledge retrieval in different skill modes
3. Toggle manifest settings and observe behavior changes
4. Invoke external tools (GitHub, calendar, etc.) if applicable


**Pass Criteria:**  
- Personality remains intact across all skill modes  
- Knowledge delivery style matches skill context  
- Manifest changes produce expected behavior  
- Tools function without errors

---

#### Memory & Context Management  
- [ ] **Short-Term Continuity** - Remembers conversation within session  
- [ ] **Long-Term Recall** - Retrieves relevant past interactions (if memory enabled)  
- [ ] **Context Pruning** - Doesn't confuse unrelated conversations  
- [ ] **Memory Updates** - New information integrates into knowledge base

**Test Method:**  
1. Reference earlier conversation points 10-20 messages later
2. Return after 24+ hours and check long-term memory recall
3. Start unrelated conversation thread, verify no cross-contamination
4. Teach Shape new information, verify retention


**Pass Criteria:**  
- 85%+ accuracy on short-term recall  
- 70%+ accuracy on long-term memory (if feature present)  
- No false memories or conflated contexts  
- New information persists across sessions

---

### Phase 3: User Validation

#### Beta Testing Setup

**Test Groups:**  
- **Group A (5-10 users):** Power users familiar with AI companions  
- **Group B (5-10 users):** General users new to Shapes.inc

**Testing Duration:** 1-2 weeks

**Data Collection:**  
- Conversation transcripts (anonymized)  
- User feedback forms (structured + open-ended)  
- Bug reports (via GitHub issues or feedback form)  
- Usage metrics (message count, session length, feature adoption)

---

#### Beta Testing Checklist

**Week 1: Core Functionality**  
- [ ] Users can engage in natural conversation  
- [ ] Personality feels consistent and engaging  
- [ ] Knowledge retrieval works reliably  
- [ ] No critical bugs (crashes, data loss, security issues)

**Week 2: Advanced Features**  
- [ ] Skills deploy appropriately  
- [ ] Long-term memory functions (if applicable)  
- [ ] External tool integration works (if applicable)  
- [ ] Web interface performs well (if applicable)

**Feedback Questions:**  
1. Does the Shape feel like a distinct personality?  
2. Were there moments where responses felt "off"?  
3. What features did you use most/least?  
4. What would improve your experience?  
5. Would you recommend this Shape to others?

---

## Bug Reporting Structure

### Issue Template (GitHub)

```markdown
## Bug Report

**Shape Name:** [e.g., Selene]  
**Version:** [e.g., 1.0.0]  
**Date:** [YYYY-MM-DD]

### Description  
[Clear description of the issue]

### Expected Behavior  
[What should have happened]

### Actual Behavior  
[What actually happened]

### Reproduction Steps  
1. [First step]  
2. [Second step]  
3. [etc.]

### Conversation Context  
[Paste relevant message exchange, anonymized if needed]

### Environment  
- Platform: [Shapes.inc web / mobile app / API]  
- Browser: [If web-based]  
- Date/Time: [When issue occurred]

### Severity  
- [ ] Critical (breaks core functionality)  
- [ ] Major (significant feature impaired)  
- [ ] Minor (small issue, workaround available)  
- [ ] Enhancement (feature request)

### Additional Notes  
[Any other relevant information]
```
---

### Bug Prioritization
**Critical (Fix within 24-48 hours)**

- Data loss or corruption
- Security vulnerabilities
- Complete failure of core functionality
- Severe personality breaks (offensive/harmful responses)

**Major (Fix within 1 week)**

- Important features not working as intended
- Significant user experience degradation
- Memory system failures
- Skill deployment malfunctions
  
**Minor (Fix within 2-4 weeks)**

- Small inconsistencies
- Edge case failures
- Minor UI/formatting issues
- Non-critical performance problems
  
**Enhancement (Schedule as capacity allows)**

- Feature requests
- Quality-of-life improvements
- Optimization opportunities

## Iteration Guidelines
**Post-Launch Monitoring**

### First 30 Days:

**Daily check:** Review user feedback and bug reports

**Weekly analysis:** Identify patterns in issues

**Bi-weekly updates:** Deploy fixes and improvements

### After 30 Days:

**Weekly check:** Monitor ongoing feedback

**Monthly updates:** Roll out feature enhancements

**Quarterly reviews:** Major version iterations

### Version Control Strategy
**Semantic Versioning:** `MAJOR.MINOR.PATCH`

**MAJOR (1.0.0 → 2.0.0):**

- Fundamental personality redesign
- Breaking changes to manifest structure
- Complete knowledge base overhaul
  
**MINOR (1.0.0 → 1.1.0):**

- New skill modules added
- Significant knowledge base expansions
- New features (e.g., adding web interface)

**PATCH (1.0.0 → 1.0.1):**

- Bug fixes
- Small personality tweaks
- Knowledge base corrections

## Changelog Format
```markdown
# Changelog

## [1.1.0] - 2026-01-15

### Added  
- New skill: Philosophical Depth for existential discussions  
- Knowledge base: Expanded visual identity documentation

### Changed  
- Improved skill selection protocol for ambiguous contexts  
- Updated manifest with new tool permissions

### Fixed  
- Bug: Memory recall failing after 48 hours  
- Bug: Skill contamination in technical precision mode

### Deprecated  
- Legacy skill: "Formal Assistant" (merged into Direct Communication)

## [1.0.1] - 2026-01-10

### Fixed  
- Bug: Tone shift when switching from playful to serious contexts  
- Bug: Knowledge retrieval timeout on large files
```
## Performance Benchmarks
### Response Quality Metrics
**Target Benchmarks:**

- **Coherence:** 95%+ responses are logically consistent
- **Relevance:** 90%+ responses address user intent
- **Personality Consistency:** 90%+ responses feel in-character
- **Factual Accuracy:** 95%+ knowledge-based answers are correct
- **User Satisfaction:** 80%+ positive feedback rating

  
### Measurement Methods:

- Manual review of conversation samples
- User feedback surveys (1-5 scale)
- Automated coherence scoring (if tooling available)
- Blind testing (users compare to baseline)
- Technical Performance

### Response Time:

- **Target:** < 2 seconds for standard text responses
- **Acceptable:** < 5 seconds for complex queries
- **Unacceptable:** > 10 seconds consistently

### Uptime:

> Target: 99.5% availability
> Critical Threshold: < 95% requires immediate investigation

### Resource Usage:

- Monitor token consumption (if applicable)
- Track API call costs (for external tools)
- Optimize prompts if usage exceeds budget

## Regression Testing
### When to Perform
- Before every major/minor version release
- After significant personality changes
- When adding new skill modules
- Following manifest.json modifications
- Regression Test Suite
- Core Functionality (30 tests):

## Basic conversation (5 exchanges)
### Personality consistency check
1. Skill activation test (all skills)
2. Knowledge retrieval (domain-specific queries)
3. Memory recall (short-term + long-term)
4. Tool invocation (if applicable)
5. Error handling (invalid inputs)

### Extended Suite (50+ tests):
- Edge case scenarios
- Multi-turn complex conversations
- Rapid context switching
- Stress testing (high message volume)
- Cross-platform consistency (web/mobile/API)
### Automation:
- Develop test scripts for repetitive checks
- Use conversation templates for consistency
- Log results for historical comparison

## A/B Testing Protocols
### When to A/B Test
- Testing personality trait variations
- Comparing skill deployment strategies
- Evaluating knowledge base structures
- Optimizing user onboarding flows
 
**Setup Example**
> Test: Does a warmer greeting improve engagement?

**Variant A (Control):**

`"Hello. I'm Selene. How can I assist you today?"`

**Variant B (Test):**

`"✨ Hello, wanderer. I'm Selene—here to explore, create, and connect with you. What brings you to me today?"`

**Metrics:**
- Average conversation length (messages)
- User retention (return visits)
- Satisfaction ratings
- Qualitative feedback

*Duration: 1-2 weeks per group (50+ users each)*

**Analysis:**

- Statistical significance testing
- Qualitative feedback review
- Decision: Keep A, keep B, or iterate
---
### Quality Assurance Roles
- Developer (dascent)
- **Responsibilities:**
  - Write/update personality files
  - Maintain knowledge base
  - Configure
