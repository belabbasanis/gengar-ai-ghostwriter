#!/usr/bin/env python3
"""
AI Ghostwriter MVP

Simplified version that demonstrates the core workflow:
1. Fetch smart glasses news from NewsAPI
2. Generate essay using Claude with style guide
3. Save draft to data/drafts/

Usage:
    python src/mvp.py
"""

import os
import sys
from datetime import datetime
from pathlib import Path
from dotenv import load_dotenv

# Add src to path for imports
sys.path.insert(0, str(Path(__file__).parent))

from utils.news_api import fetch_smart_glasses_news, format_articles_for_prompt
from agents.ghostwriter import write_essay_simplified


def check_environment():
    """Verify required environment variables are set."""
    missing = []
    
    if not os.getenv("ANTHROPIC_API_KEY"):
        missing.append("ANTHROPIC_API_KEY")
    if not os.getenv("NEWS_API_KEY"):
        missing.append("NEWS_API_KEY")
    
    if missing:
        print("❌ Missing required environment variables:")
        for var in missing:
            print(f"   - {var}")
        print("\nPlease create a .env file with these variables.")
        print("See README.md for instructions on obtaining API keys.")
        sys.exit(1)


def main():
    """Run the MVP workflow."""
    # Load environment variables
    load_dotenv()
    
    print("\n" + "="*60)
    print("🚀 AI GHOSTWRITER MVP - Smart Glasses Edition")
    print("="*60)
    
    # Check environment
    check_environment()
    
    try:
        # Step 1: Fetch news
        print("\n📰 STEP 1: Fetching smart glasses news")
        print("-" * 60)
        articles = fetch_smart_glasses_news(limit=10)
        
        if not articles:
            print("   ⚠️  No articles found in the last 24 hours.")
            print("   This might be normal on slow news days.")
            print("   Try expanding the search terms in src/utils/news_api.py")
            sys.exit(0)
        
        print(f"   ✅ Found {len(articles)} articles")
        print(f"\n   Recent headlines:")
        for i, article in enumerate(articles[:5], 1):
            print(f"   {i}. {article['title'][:70]}...")
        
        if len(articles) > 5:
            print(f"   ... and {len(articles) - 5} more")
        
        # Step 2: Generate essay
        print("\n✍️  STEP 2: Generating essay with Claude")
        print("-" * 60)
        print("   Loading writing style guide...")
        print("   Composing prompt with articles + style guide...")
        
        essay = write_essay_simplified(articles)
        
        # Step 3: Save draft
        print("\n💾 STEP 3: Saving draft")
        print("-" * 60)
        
        # Create output directory if it doesn't exist
        output_dir = Path("data/drafts")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
        output_file = output_dir / f"essay_{timestamp}.md"
        
        # Add metadata header to the essay
        metadata = f"""---
Generated: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
Articles: {len(articles)}
Model: {os.getenv('CLAUDE_MODEL', 'claude-3-5-sonnet-20241022')}
---

"""
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(metadata + essay)
        
        print(f"   ✅ Essay saved to: {output_file}")
        
        # Step 4: Statistics
        print("\n📊 STATISTICS")
        print("-" * 60)
        word_count = len(essay.split())
        char_count = len(essay)
        paragraph_count = len([p for p in essay.split("\n\n") if p.strip()])
        
        print(f"   Words: {word_count:,}")
        print(f"   Characters: {char_count:,}")
        print(f"   Paragraphs: {paragraph_count}")
        print(f"   Reading time: ~{word_count // 200} minutes")
        
        # Success message
        print("\n" + "="*60)
        print("✨ SUCCESS! Your essay is ready for review.")
        print("="*60)
        print(f"\nNext steps:")
        print(f"1. Review the draft: cat {output_file}")
        print(f"2. Edit as needed")
        print(f"3. Publish to Substack")
        print(f"\nTo generate another essay, run: python src/mvp.py")
        print()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user. Exiting...")
        sys.exit(0)
        
    except Exception as e:
        print(f"\n❌ ERROR: {type(e).__name__}")
        print(f"   {str(e)}")
        print("\nTroubleshooting:")
        print("- Check your API keys in .env file")
        print("- Verify internet connection")
        print("- Ensure config/style_guide_longform.md exists")
        sys.exit(1)


if __name__ == "__main__":
    main()
