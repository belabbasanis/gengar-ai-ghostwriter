#!/usr/bin/env python3
"""
Quick validation script to check if MVP is set up correctly.
Run this before trying to generate essays.
"""

import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a required file exists."""
    if Path(filepath).exists():
        print(f"✅ {description}")
        return True
    else:
        print(f"❌ {description} - NOT FOUND")
        return False

def check_python_version():
    """Check Python version is 3.11+."""
    version = sys.version_info
    if version >= (3, 11):
        print(f"✅ Python {version.major}.{version.minor}.{version.micro}")
        return True
    else:
        print(f"⚠️  Python {version.major}.{version.minor} (3.11+ recommended)")
        return True  # Still allow it

def check_imports():
    """Check if required packages can be imported."""
    packages = {
        "dotenv": "python-dotenv",
        "requests": "requests", 
        "openai": "openai"
    }
    
    all_good = True
    for module, package in packages.items():
        try:
            __import__(module)
            print(f"✅ {package} installed")
        except ImportError:
            print(f"❌ {package} - NOT INSTALLED")
            print(f"   Install with: pip install {package}")
            all_good = False
    
    return all_good

def check_env_file():
    """Check if .env file exists and has keys."""
    env_path = Path(".env")
    
    if not env_path.exists():
        print("❌ .env file not found")
        print("   Create it from the template in MVP_QUICKSTART.md")
        return False
    
    print("✅ .env file exists")
    
    # Check if it has the required keys (not just placeholders)
    with open(env_path, "r") as f:
        content = f.read()
    
    if "your_openai_key_here" in content or "your_newsapi_key_here" in content:
        print("⚠️  .env file contains placeholder keys")
        print("   Replace 'your_*_key_here' with actual API keys")
        return False
    
    if "OPENAI_API_KEY" in content and "NEWS_API_KEY" in content:
        print("✅ API keys appear to be set")
        return True
    
    return False

def main():
    print("\n" + "="*60)
    print("MVP SETUP VALIDATION")
    print("="*60 + "\n")
    
    checks = []
    
    print("📋 Checking Python Version...")
    checks.append(check_python_version())
    print()
    
    print("📦 Checking Required Packages...")
    checks.append(check_imports())
    print()
    
    print("📁 Checking Project Files...")
    checks.append(check_file_exists("src/mvp.py", "MVP script"))
    checks.append(check_file_exists("src/utils/news_api.py", "News API client"))
    checks.append(check_file_exists("src/agents/ghostwriter.py", "Ghostwriter agent"))
    checks.append(check_file_exists("config/style_guide_longform.md", "Style guide"))
    print()
    
    print("🔑 Checking Environment Configuration...")
    checks.append(check_env_file())
    print()
    
    print("="*60)
    if all(checks):
        print("✨ ALL CHECKS PASSED! You're ready to run the MVP.")
        print("="*60)
        print("\nRun: python src/mvp.py\n")
        return 0
    else:
        print("⚠️  SOME CHECKS FAILED - Fix the issues above first.")
        print("="*60)
        print("\nSee MVP_QUICKSTART.md for setup instructions.\n")
        return 1

if __name__ == "__main__":
    sys.exit(main())
