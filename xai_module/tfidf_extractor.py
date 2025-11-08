"""
TF-IDF Extractor Module

This module provides document retrieval functionality using TF-IDF (Term Frequency-Inverse Document Frequency).
It extracts the most relevant lecture snippets given a question text.

# pip install scikit-learn
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


def get_relevant_snippet(question_text: str, lecture_docs: list[str], top_k: int = 1) -> list[str]:
    """
    Given a question, return the most relevant lecture snippet(s).
    
    Args:
        question_text: The MCQ question text
        lecture_docs: List of lecture note paragraphs/documents
        top_k: Number of top relevant snippets to return (default: 1)
    
    Returns:
        List of relevant lecture snippets, ordered by relevance (most relevant first)
    """
    if not lecture_docs:
        return []
    
    if not question_text.strip():
        return lecture_docs[:top_k]
    
    # Combine question and documents for TF-IDF vectorization
    all_docs = [question_text] + lecture_docs
    
    # Create TF-IDF vectorizer
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True, max_features=1000)
    
    try:
        # Fit and transform all documents
        tfidf_matrix = vectorizer.fit_transform(all_docs)
        
        # Extract question vector (first row) and document vectors (remaining rows)
        question_vector = tfidf_matrix[0:1]
        doc_vectors = tfidf_matrix[1:]
        
        # Calculate cosine similarity between question and each document
        similarities = cosine_similarity(question_vector, doc_vectors)[0]
        
        # Get indices of top_k most similar documents
        top_indices = np.argsort(similarities)[::-1][:top_k]
        
        # Return the most relevant snippets
        relevant_snippets = [lecture_docs[i] for i in top_indices if similarities[i] > 0]
        
        # If no similarities found, return first k documents
        if not relevant_snippets:
            return lecture_docs[:top_k]
        
        return relevant_snippets
    
    except Exception as e:
        # Fallback: return first k documents if TF-IDF fails
        print(f"Warning: TF-IDF extraction failed: {e}. Returning first {top_k} documents.")
        return lecture_docs[:top_k]

