"""
LLM Adapter Module

This module provides an adapter pattern for different LLM providers (DeepSeek, OpenAI).
It allows easy swapping between different LLM APIs while maintaining the same interface.

Both DeepSeekClient and OpenAIClient implement the same .generate() method signature.
"""

import os
import requests


class DeepSeekClient:
    """
    DeepSeek API client for generating explanations using DeepSeek's chat completion API.
    
    This is the currently active LLM provider. Use DEEPSEEK_API_KEY environment variable
    or pass api_key directly to the constructor.
    """
    
    def __init__(self, api_key: str | None = None, base_url: str = "https://api.deepseek.com"):
        """
        Initialize DeepSeek client.
        
        Args:
            api_key: DeepSeek API key. If None, reads from DEEPSEEK_API_KEY env var
            base_url: Base URL for DeepSeek API (default: https://api.deepseek.com)
        """
        self.api_key = api_key or os.getenv("DEEPSEEK_API_KEY")
        self.base_url = base_url.rstrip('/')
        
        if not self.api_key:
            raise ValueError(
                "DeepSeek API key not provided. Set DEEPSEEK_API_KEY environment variable "
                "or pass api_key to constructor."
            )
    
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """
        Call DeepSeek chat/completions endpoint and return the model's text.
        
        Args:
            system_prompt: System message/prompt for the LLM
            user_prompt: User message/prompt for the LLM
        
        Returns:
            Generated text response from the LLM
        
        Raises:
            requests.HTTPError: If the API request fails
            ValueError: If the API response is malformed
        """
        url = f"{self.base_url}/chat/completions"
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        
        # Request body - easy to modify if DeepSeek API structure changes
        payload = {
            "model": "deepseek-chat",
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            "temperature": 0.7,
            "max_tokens": 500
        }
        
        try:
            resp = requests.post(url, json=payload, headers=headers, timeout=30)
            resp.raise_for_status()
            data = resp.json()
            
            # Extract response text - adjust if DeepSeek response structure differs
            if "choices" in data and len(data["choices"]) > 0:
                return data["choices"][0]["message"]["content"]
            else:
                raise ValueError(f"Unexpected API response structure: {data}")
                
        except requests.exceptions.RequestException as e:
            raise RuntimeError(f"Failed to call DeepSeek API: {e}")


class OpenAIClient:
    """
    OpenAI API client placeholder for future migration.
    
    This class maintains the same interface as DeepSeekClient (.generate method)
    so it can be swapped easily in the pipeline.
    
    TODO: Implement actual OpenAI API calls when migrating.
    """
    
    def __init__(self, api_key: str | None = None, base_url: str = "https://api.openai.com/v1"):
        """
        Initialize OpenAI client.
        
        Args:
            api_key: OpenAI API key. If None, reads from OPENAI_API_KEY env var
            base_url: Base URL for OpenAI API (default: https://api.openai.com/v1)
        """
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.base_url = base_url.rstrip('/')
        
        if not self.api_key:
            raise ValueError(
                "OpenAI API key not provided. Set OPENAI_API_KEY environment variable "
                "or pass api_key to constructor."
            )
    
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """
        Call OpenAI chat/completions endpoint and return the model's text.
        
        Args:
            system_prompt: System message/prompt for the LLM
            user_prompt: User message/prompt for the LLM
        
        Returns:
            Generated text response from the LLM
        
        Note:
            This is a placeholder implementation. Replace with actual OpenAI API calls.
        """
        # TODO: Replace with actual OpenAI API call
        # Example structure (not implemented):
        # url = f"{self.base_url}/chat/completions"
        # headers = {
        #     "Authorization": f"Bearer {self.api_key}",
        #     "Content-Type": "application/json"
        # }
        # payload = {
        #     "model": "gpt-3.5-turbo",
        #     "messages": [
        #         {"role": "system", "content": system_prompt},
        #         {"role": "user", "content": user_prompt}
        #     ]
        # }
        # resp = requests.post(url, json=payload, headers=headers)
        # return resp.json()["choices"][0]["message"]["content"]
        
        return "OpenAI client not yet implemented. Please use DeepSeekClient for now."

