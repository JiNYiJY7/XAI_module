# Setup script for DeepSeek API Key
# This script helps you set the DEEPSEEK_API_KEY environment variable

Write-Host "DeepSeek API Key Setup" -ForegroundColor Cyan
Write-Host "======================" -ForegroundColor Cyan
Write-Host ""

# Prompt for API key
$apiKey = Read-Host "Enter your DeepSeek API key (e.g., sk-xxxx...)"

if ([string]::IsNullOrWhiteSpace($apiKey)) {
    Write-Host "Error: API key cannot be empty!" -ForegroundColor Red
    exit 1
}

# Set for current session
$env:DEEPSEEK_API_KEY = "sk-1f790298cc0e447fbadfe2d790e0907b"
Write-Host ""
Write-Host "API key set for current PowerShell session." -ForegroundColor Green
Write-Host ""

# Ask if user wants to set it permanently
$setPermanent = Read-Host "Do you want to set it permanently for your user account? (y/n)"

if ($setPermanent -eq "y" -or $setPermanent -eq "Y") {
    [System.Environment]::SetEnvironmentVariable("DEEPSEEK_API_KEY", $apiKey, "User")
    Write-Host "API key set permanently for your user account." -ForegroundColor Green
    Write-Host "Note: You may need to restart your terminal/PowerShell for it to take effect." -ForegroundColor Yellow
}

Write-Host ""
Write-Host "You can now run: python app_demo.py" -ForegroundColor Green

