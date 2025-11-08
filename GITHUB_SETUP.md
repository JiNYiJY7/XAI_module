# How to Push Code to GitHub

## Prerequisites

1. Install Git if you haven't already:
   - Download from: https://git-scm.com/download/win
   - Or use: `winget install Git.Git`

2. Make sure your API key is safe:
   - ✅ `config.py` is already in `.gitignore` (will NOT be pushed)
   - ✅ `config.py.example` will be pushed (template file without real key)

## Steps to Push to GitHub

### Step 1: Initialize Git Repository

```powershell
git init
```

### Step 2: Add All Files (except those in .gitignore)

```powershell
git add .
```

### Step 3: Check What Will Be Committed

```powershell
git status
```

**Important:** Make sure `config.py` is NOT listed (it should be ignored).

### Step 4: Create Initial Commit

```powershell
git commit -m "Initial commit: XAI MCQ Quiz System with 3-layer architecture"
```

### Step 5: Add Remote Repository

```powershell
git remote add origin https://github.com/JiNYiJY7/XAI_module.git
```

### Step 6: Push to GitHub

```powershell
git branch -M main
git push -u origin main
```

If you get authentication errors, you may need to:
- Use GitHub Personal Access Token instead of password
- Or set up SSH keys

## Verification

After pushing, check your repository at:
https://github.com/JiNYiJY7/XAI_module

**Make sure:**
- ✅ `config.py` is NOT in the repository
- ✅ `config.py.example` IS in the repository
- ✅ All source code files are present

## Security Note

🔒 **Your API key in `config.py` is safe** - it's in `.gitignore` and will never be pushed to GitHub.

## Quick Command Reference

```powershell
# Initialize repository
git init

# Add all files
git add .

# Check status (verify config.py is ignored)
git status

# Commit
git commit -m "Initial commit: XAI MCQ Quiz System"

# Add remote
git remote add origin https://github.com/JiNYiJY7/XAI_module.git

# Push to GitHub
git branch -M main
git push -u origin main
```

