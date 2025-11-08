# XAI module Lecture Note MCQ Generator

A modular Explainable AI (XAI) module for MCQ quiz systems with 3 layers: retrieval (TF-IDF), rule-based reasoning, and LLM explanation.

## Setup

### 1. Install Dependencies

```bash
pip install scikit-learn requests
```

### 2. Set DeepSeek API Key

**Option A: Using config.py (Recommended - Permanent)**

1. Copy `config.py.example` to `config.py`:
   ```bash
   copy config.py.example config.py
   ```

2. Open `config.py` and paste your API key:
   ```python
   DEEPSEEK_API_KEY = "sk-your-api-key-here"
   ```

**Option B: Using Environment Variable**

You have several options to set your DeepSeek API key:

#### Option 1: Using the Setup Script (Recommended for Windows)

Run the PowerShell setup script:

```powershell
.\setup_deepseek_key.ps1
```

#### Option 2: Set in PowerShell (Temporary - Current Session Only)

```powershell
$env:DEEPSEEK_API_KEY = "your-api-key-here"
```

#### Option 3: Set Permanently via PowerShell (User Account)

```powershell
[System.Environment]::SetEnvironmentVariable("DEEPSEEK_API_KEY", "your-api-key-here", "User")
```

**Note:** After setting permanently, you may need to restart your terminal/PowerShell.

#### Option 4: Set Permanently via Windows GUI

1. Open "Environment Variables" in Windows:
   - Press `Win + R`, type `sysdm.cpl`, press Enter
   - Go to "Advanced" tab → Click "Environment Variables"
2. Under "User variables", click "New"
3. Variable name: `DEEPSEEK_API_KEY`
4. Variable value: `your-api-key-here`
5. Click OK and restart your terminal

#### Option 5: Pass API Key Directly in Code

You can also pass the API key directly when creating the client:

```python
from xai_module.llm_adapter import DeepSeekClient
client = DeepSeekClient(api_key="your-api-key-here")
```

## Usage

### Run the Demo

```bash
python app_demo.py
```

### Use in Your Code

```python
from xai_module.xai_pipeline import run_xai

lecture_docs = [
    "Your lecture notes here...",
    "More lecture content...",
]

question = "What is TF-IDF?"
student_answer = "A neural network"
correct_answer = "A term weighting scheme"

result = run_xai(question, student_answer, correct_answer, lecture_docs)
print(result)
```

## Project Structure

```
├── app_demo.py              # Demo application
├── xai_module/              # Main XAI module
│   ├── __init__.py
│   ├── tfidf_extractor.py  # Layer 1: TF-IDF retrieval
│   ├── rule_reasoner.py    # Layer 2: Rule-based reasoning
│   ├── llm_adapter.py      # Layer 3: LLM adapter (DeepSeek/OpenAI)
│   └── xai_pipeline.py     # Orchestration layer
├── data/
│   └── sample_lectures.txt # Sample lecture notes
├── config.py.example       # API key configuration template
├── setup_deepseek_key.ps1  # API key setup script
└── .gitignore              # Git ignore file (excludes config.py)
```

## Switching LLM Providers

To switch from DeepSeek to OpenAI (when implemented):

```python
from xai_module.llm_adapter import OpenAIClient
from xai_module.xai_pipeline import run_xai

result = run_xai(
    question, 
    student_answer, 
    correct_answer, 
    lecture_docs,
    llm_client=OpenAIClient()  # Swap the client here
)
```

## Requirements

- Python 3.10+
- scikit-learn
- requests

## License

University project - Educational use only.

