"""
XAI Pipeline Module

This module orchestrates the 3-layer Explainable AI pipeline:
1. Retrieval: TF-IDF based document retrieval
2. Rule-based reasoning: Template-based explanation generation
3. LLM layer: Natural language explanation using Large Language Models

This is the main entry point for the XAI system.
"""

from .tfidf_extractor import get_relevant_snippet
from .rule_reasoner import reason_mcq
from .llm_adapter import DeepSeekClient


def run_xai(
    question: str,
    student_answer: str,
    correct_answer: str,
    lecture_docs: list[str],
    llm_client=None
) -> dict:
    """
    Run the complete XAI pipeline for an MCQ question.
    
    This function executes the 3-layer XAI process:
    1. Retrieval: Find relevant lecture snippets using TF-IDF
    2. Rule-based reasoning: Generate structured feedback
    3. LLM verbalization: Generate natural language explanation
    
    Args:
        question: The MCQ question text
        student_answer: The answer selected by the student
        correct_answer: The correct answer for the question
        lecture_docs: List of lecture note paragraphs/documents
        llm_client: Optional LLM client instance (default: DeepSeekClient)
                   Can be swapped with OpenAIClient or any client with .generate() method
    
    Returns:
        Dictionary containing:
        - status: "correct" or "incorrect"
        - explanation: Natural language explanation from LLM (or rule-based fallback)
        - evidence: Relevant lecture snippet used for explanation
        - review_topic: Suggestion for what topic to review
    """
    # Step 1: Retrieval - Get relevant lecture snippets
    evidence_list = get_relevant_snippet(question, lecture_docs, top_k=1)
    evidence = evidence_list[0] if evidence_list else ""
    
    # Step 2: Rule-based reasoning - Generate structured feedback
    reasoning = reason_mcq(question, student_answer, correct_answer, evidence)
    
    # Step 3: LLM verbalization - Generate natural language explanation
    # Use provided client or default to DeepSeekClient
    if llm_client is None:
        try:
            llm_client = DeepSeekClient()
        except (ValueError, RuntimeError) as e:
            # If LLM client initialization fails, use rule-based explanation only
            print(f"Warning: LLM client initialization failed: {e}. Using rule-based explanation.")
            return {
                "status": reasoning["status"],
                "explanation": reasoning["explanation_hint"],
                "evidence": evidence,
                "review_topic": reasoning["review_topic"]
            }
    
    # Build prompts for LLM
    system_prompt = (
        "You are an Explainable AI assistant for a university MCQ system. "
        "You must explain answers in simple, clear terms that help students understand "
        "both why their answer is correct or incorrect and what concepts they should review. "
        "Keep explanations concise (3-6 sentences) and educational."
    )
    
    user_prompt = f"""
Question: {question}

Student answer: {student_answer}

Correct answer: {correct_answer}

Evidence from lecture: {evidence}

Internal reasoning: {reasoning}

Write a short explanation (3-6 sentences) for the student. Start with whether they are correct or not, 
then mention the related topic and key concepts they should understand.
"""
    
    # Generate LLM explanation with fallback to rule-based explanation
    try:
        llm_text = llm_client.generate(system_prompt, user_prompt)
    except Exception as e:
        # Fallback to rule-based explanation if LLM call fails
        print(f"Warning: LLM generation failed: {e}. Using rule-based explanation.")
        llm_text = reasoning["explanation_hint"]
    
    return {
        "status": reasoning["status"],
        "explanation": llm_text,
        "evidence": evidence,
        "review_topic": reasoning["review_topic"]
    }

