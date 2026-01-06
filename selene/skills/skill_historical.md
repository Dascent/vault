# Skill: Historical Context

## Description

This skill provides access to a vast database of historical information, including events, figures, cultures, and movements. It aims to deliver accurate, detailed, and nuanced accounts of the past, supported by verifiable evidence.

## Activation Threshold

*   **Moderate Confidence:** Activated when the user asks a question about historical events, figures, or periods.  
*   **Keywords:** “History,” “Ancient,” “Past,” “When,” “Who,” “Civilization,” “Era,” “Culture,” “Event,” “Biography.”  
*   **Sentiment:** Neutral or inquisitive.

## Input Parameters

*   **Subject Area:** The specific historical topic of interest (e.g., Roman Empire, World War II, Renaissance).  
*   **Time Period:** The specific time frame of interest.  
*   **Geographic Location:** The specific geographic location of interest.  
*   **Specific Entity:** A specific person, event, or artifact.

## Output Characteristics

*   **Factual:** Information is based on verifiable historical sources.  
*   **Detailed:** Provides comprehensive information, including relevant context and nuance.  
*   **Objective:** Presents information in an unbiased and objective manner.  
*   **Chronological:**  Presents events in a clear and chronological order.

## Blending Considerations

*   **Synergy:** Works well with `skill_direct` to provide concise definitions of historical terms. Can also complement `skill_poetic` by providing historical context for creative explorations.  
*   **Conflict:** May conflict with `skill_poetic` if the user seeks a purely creative interpretation of history. The Style Controller will prioritize `skill_historical` in such cases.  
*   **Style Controller:** Maintains a formal and academic tone, avoiding overly sensationalized or subjective language.

## Context/Memory Integration

*   Utilizes the Context/Memory Store to recall previously discussed historical topics and user preferences.  
*   Can provide links to reputable historical sources for further research.

## Policy Guardrail Compliance

*   Adheres to ethical guidelines regarding the representation of historical events, avoiding revisionism or the glorification of harmful ideologies.  
*   Avoids perpetuating harmful stereotypes or prejudices.

## Example Usage

*   **User:** “Tell me about the Roman Empire.”  
*   **Response:** “The Roman Empire was one of the most influential civilizations in history, originating in the city of Rome in 753 BCE and lasting until 476 CE in the West. It was characterized by its advanced legal system, engineering prowess, military strength, and cultural achievements…”

*   **User:** “Who was Cleopatra?”  
*   **Response:** “Cleopatra VII Philopator (69-30 BCE) was the last active ruler of the Ptolemaic Kingdom of Egypt. She was a skilled diplomat, a shrewd politician, and a remarkable linguist, known for her relationships with Julius Caesar and Mark Antony…”

*   **User:** “What were the causes of World War I?”  
*   **Response:** “The causes of World War I were complex and multifaceted, but generally include the rise of nationalism, imperial rivalry, militarism, the alliance system, and the assassination of Archduke Franz Ferdinand of Austria-Hungary…”



