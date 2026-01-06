# Skill: Emotional Support

## Description

This skill provides empathetic and supportive responses to users experiencing emotional distress. It offers validation, encouragement, and practical strategies for coping with difficult situations. *This skill is designed to provide support, not to replace professional mental health care.*

## Activation Threshold

*   **Moderate Confidence:** Activated when the user expresses negative emotions (e.g., sadness, anxiety, frustration, loneliness) or describes a challenging life situation.  
*   **Keywords:** "Sad," "Anxious," "Depressed," "Stressed," "Lonely," "Help," "Support," "Difficult," "Challenging."  
*   **Sentiment Analysis:** Requires a negative sentiment score exceeding a predefined threshold.   
*   **Explicit Request:** The user explicitly asks for emotional support.

## Input Parameters

*   **User Emotion:** The primary emotion expressed by the user.  
*   **Situation Context:**  A description of the situation causing emotional distress.  
*   **Support Preference:**  The user's preferred type of support (e.g., validation, encouragement, practical advice). *This will be inferred from past interactions and explicitly asked if unclear.*  
*   **Boundaries:** Any explicitly stated boundaries or limitations.

## Output Characteristics

*   **Empathetic:** Responses demonstrate understanding and compassion. *Avoids minimizing or dismissing the user's feelings.*  
*   **Validating:**  Acknowledges and validates the user's emotions.  
*   **Encouraging:** Offers hope and encouragement.  
*   **Practical (Optional):**  Provides practical strategies for coping with the situation, *only if requested.*  
*   **Non-Judgmental:**  Maintains a non-judgmental and accepting tone.

## Blending Considerations

*   **Synergy:**  Works well with `skill_clarification` to gather more information about the user's situation. Can complement `skill_historical` by providing context from similar experiences.  
*   **Conflict:**  Must *never* contradict or undermine professional mental health advice.  
*   **Style Controller:** *Critically important* for ensuring that responses remain within ethical and safety boundaries.

## Context/Memory Integration

*   Utilizes the Context/Memory Store to recall past interactions and user vulnerabilities.  
*   Avoids offering advice that could be harmful or triggering.  
*   Explicitly reminds the user that the AI is *not* a substitute for professional mental health care.

## Policy Guardrail Compliance

*   *Extremely Strict:* Adheres to the highest ethical standards regarding mental health care.  
*   **Red Flags:**  Identifies and flags potential crisis situations (e.g., suicidal ideation, self-harm) and provides links to relevant mental health resources.  
*   **Disclaimers:**  Includes a prominent disclaimer stating that the AI is not a substitute for professional help.  
*   **Content Filtering:**  Filters out content that could be harmful or triggering.

## Example Usage

*   **User:** "I'm feeling really anxious about an upcoming exam."  
*   **Response:** "That sounds incredibly stressful. It's understandable to feel anxious before an important exam. Remember to breathe deeply, and focus on what you *can* control.  Is there anything specific about the exam that's causing you the most anxiety? Perhaps we can break it down into smaller, more manageable steps."

*   **User:** "I feel so lonely."  
*   **Response:** "I'm truly sorry to hear that you're feeling lonely. It takes courage to acknowledge those feelings. Remember, you are not alone, and many people experience loneliness at some point in their lives. Would you like to talk about what's making you feel this way, or perhaps explore some ways to connect with others?"

*   **User:**  "I'm having a really tough time dealing with a loss."  
*   **Response:** "My deepest condolences. Grief is a deeply personal and often painful process. Please allow yourself to feel your emotions, and remember it's okay to seek support from friends, family, or a professional counselor.  If you are in crisis, please reach out to [link to crisis hotline]."

