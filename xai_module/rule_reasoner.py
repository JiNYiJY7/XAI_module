"""
Rule-Based Reasoner Module

This module provides rule-based reasoning for MCQ answers without requiring external APIs.
It analyzes student answers against correct answers and provides structured feedback.

This is a template/rule-based layer that does NOT depend on any external API.
"""


def reason_mcq(question: str, student_answer: str, correct_answer: str, evidence: str) -> dict:
    """
    Return a dict that tells whether the student is correct and what type of mistake it is.
    
    Args:
        question: The MCQ question text
        student_answer: The answer selected by the student
        correct_answer: The correct answer for the question
        evidence: Relevant lecture snippet/evidence retrieved from documents
    
    Returns:
        Dictionary containing:
        - status: "correct" or "incorrect"
        - explanation_hint: Brief explanation or hint about the answer
        - review_topic: Suggestion for what topic to review
    """
    # Normalize answers for comparison (case-insensitive, strip whitespace)
    student_normalized = student_answer.strip().lower()
    correct_normalized = correct_answer.strip().lower()
    
    # Check if student answer is correct
    is_correct = student_normalized == correct_normalized
    
    if is_correct:
        return {
            "status": "correct",
            "explanation_hint": "Your answer is correct! You have a good understanding of this concept.",
            "review_topic": "You have mastered this topic. Consider reviewing related advanced concepts."
        }
    else:
        # Student answer is incorrect - provide feedback
        explanation_hint = (
            "Your answer is incorrect. The selected option appears to be related to a different "
            "concept than what the question is focusing on. Please review the lecture material "
            "related to this topic."
        )
        
        review_topic = (
            "You should review the lecture section mentioned in the evidence. "
            "Pay special attention to the key concepts and definitions related to this question."
        )
        
        # If evidence is available, mention it in the review topic
        if evidence:
            review_topic = (
                f"You should review the lecture section mentioned in the evidence: "
                f"{evidence[:100]}... (if applicable). "
                "Focus on understanding the key concepts and their relationships."
            )
        
        return {
            "status": "incorrect",
            "explanation_hint": explanation_hint,
            "review_topic": review_topic
        }

