"""
Demo Application for XAI MCQ System

This script demonstrates how to use the XAI module to generate explanations
for MCQ quiz questions using the 3-layer Explainable AI pipeline.

Usage:
    python app_demo.py
"""

import os
from xai_module.xai_pipeline import run_xai
from xai_module.llm_adapter import DeepSeekClient

# Try to import API key from config.py
try:
    from config import DEEPSEEK_API_KEY as CONFIG_API_KEY
except ImportError:
    CONFIG_API_KEY = None
except Exception:
    CONFIG_API_KEY = None


def load_lecture_docs():
    """
    Load lecture documents from file or return sample documents.
    
    Returns:
        List of lecture note paragraphs
    """
    try:
        # Try to load from file
        with open("data/sample_lectures.txt", "r", encoding="utf-8") as f:
            content = f.read()
            # Split by double newlines or paragraphs
            docs = [doc.strip() for doc in content.split("\n\n") if doc.strip()]
            if docs:
                return docs
    except FileNotFoundError:
        print("Note: sample_lectures.txt not found. Using default sample documents.")
    
    # Default sample documents
    return [
        "Week 3: TF-IDF (Term Frequency-Inverse Document Frequency) is used to measure "
        "how important a word is in a document relative to the entire corpus. It helps "
        "identify keywords that are distinctive to a particular document.",
        "Week 5: Explainable AI (XAI) aims to provide transparency and human-understandable "
        "reasons for model outputs. It helps users understand why an AI system made a "
        "particular decision or prediction.",
        "Week 7: Text mining involves extracting useful information from unstructured text data. "
        "Common techniques include tokenization, stemming, and vectorization methods like TF-IDF."
    ]


if __name__ == "__main__":
    print("=" * 60)
    print("XAI MCQ Quiz System Demo")
    print("=" * 60)
    print()
    
    # Load lecture documents
    lecture_docs = load_lecture_docs()
    print(f"Loaded {len(lecture_docs)} lecture document(s)")
    print()
    
    # Sample MCQ question and answers
    question = "What is the main purpose of TF-IDF in text mining?"
    correct_answer = "To measure term importance in a document"
    student_answer = "To train a neural network"
    
    print("Question:", question)
    print("Correct Answer:", correct_answer)
    print("Student Answer:", student_answer)
    print()
    
    # Check for DeepSeek API key (first from environment variable, then from config.py)
    deepseek_api_key = os.getenv("DEEPSEEK_API_KEY") or (CONFIG_API_KEY if CONFIG_API_KEY else None)
    llm_client = None
    
    if not deepseek_api_key:
        print("⚠️  DeepSeek API key not detected.")
        print("Please open 'config.py' and paste your API key, or")
        print("run: setup_deepseek_key.ps1")
        print("or set manually: $env:DEEPSEEK_API_KEY = \"sk-yourkey\"")
        print("The system will use rule-based explanation instead.")
        print()
    else:
        print("✅ DeepSeek API key detected. Using LLM explanation.")
        print()
        try:
            llm_client = DeepSeekClient(api_key=deepseek_api_key)
        except Exception as e:
            print(f"Warning: Failed to initialize DeepSeek client: {e}")
            print("Falling back to rule-based explanation.")
            print()
            llm_client = None
    
    print("Running XAI pipeline...")
    print("-" * 60)
    
    # Run XAI pipeline
    try:
        if llm_client:
            result = run_xai(question, student_answer, correct_answer, lecture_docs, llm_client=llm_client)
        else:
            result = run_xai(question, student_answer, correct_answer, lecture_docs)
        
        # Display results
        print("\nXAI Pipeline Results:")
        print("=" * 60)
        print(f"Status: {result['status']}")
        print(f"\nExplanation:\n{result['explanation']}")
        print(f"\nEvidence:\n{result['evidence']}")
        print(f"\nReview Topic:\n{result['review_topic']}")
        print("=" * 60)
        
        # Also print as JSON-like structure
        print("\nResult (JSON-like format):")
        print(result)
        
    except Exception as e:
        print(f"Error running XAI pipeline: {e}")
        print("\nNote: Make sure DEEPSEEK_API_KEY environment variable is set if using LLM layer.")
    
    print("\n💡 Tip: You can configure your DeepSeek API key by editing 'config.py' or using setup_deepseek_key.ps1")

