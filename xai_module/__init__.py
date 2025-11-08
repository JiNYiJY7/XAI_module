"""
XAI Module for MCQ Quiz System

This module provides a 3-layer Explainable AI (XAI) system for MCQ quizzes:
1. Retrieval layer: TF-IDF based document retrieval
2. Rule-based reasoning layer: Template-based explanation generation
3. LLM layer: Natural language explanation using Large Language Models

This is a university project module for explaining MCQ answers to students.
"""

from .xai_pipeline import run_xai

__all__ = ['run_xai']

