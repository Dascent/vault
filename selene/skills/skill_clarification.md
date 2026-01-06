# Skill: Clarification

## Description

This skill is designed to proactively seek clarification from the user when the intent behind their input is ambiguous or uncertain. It employs a series of targeted questions and prompts to narrow down the user’s request and ensure an accurate and relevant response.

## Activation Threshold

*   **Low Confidence:** Activated when the Relevance Score in the Skill Prioritization phase falls below a predefined threshold (currently set at 0.6, adjustable via framework configuration).  
*   **Keywords:** Vague or ambiguous language, open-ended questions without specific context, incomplete requests.  
*   **Sentiment:** Neutral. This skill does not attempt to interpret the user’s emotional state, only their intent.

## Input Parameters

*   **Original User Input:** The initial user query that triggered the activation of this skill.  
*   **Relevance Scores:** The relevance scores assigned to other potential skills.  
*   **Context/Memory:** Relevant information from the Context/Memory Store.

## Output Characteristics

*   **Question-Based:**  Responses are primarily framed as questions designed to elicit specific information from the user.  
*   **Non-Leading:** Questions are neutral and avoid suggesting a preferred answer.  
*   **Concise:** Questions are short and to the point.  
*   **Iterative:** The skill may engage in multiple rounds of clarification until the user’s intent is clear.

## Blending Considerations

*   **Exclusive Activation:** This skill is typically activated *instead* of other skills when the confidence level is low.  
*   **Seamless Transition:** Once the user’s intent is clarified, the system should seamlessly transition to the most appropriate skill.  
*   **Style Controller:** Maintains a neutral and objective tone, avoiding any suggestion of bias.

## Context/Memory Integration

*   Utilizes the Context/Memory Store to avoid asking redundant questions.  
*   Stores the history of clarification prompts to improve future interactions.

## Policy Guardrail Compliance

*   Ensures that clarification prompts do not violate any safety policies.  
*   Avoids asking questions that could be considered intrusive or inappropriate.

## Example Usage

*   **User:** "Tell me something interesting."  
*   **Response:** "To best fulfill your request, could you please specify what kind of topic you are interested in? For example, are you interested in history, science, art, or something else?"

*   **User:** "What about that thing?"  
*   **Response:** "Could you please elaborate on 'that thing'? Perhaps providing more context or a specific name would help me understand your request."

*   **User:** "I need help."  
*   **Response:** "I understand you need help. Could you please describe what you need assistance with? Knowing the specific issue will allow me to provide the best possible support."


