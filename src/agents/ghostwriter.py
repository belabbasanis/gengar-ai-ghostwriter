"""
Ghostwriter agent for generating Substack essays.
MVP version - basic essay generation with style guide.
Using OpenAI GPT-4 instead of Anthropic Claude.
"""

import os
from pathlib import Path
from typing import List, Dict
from openai import OpenAI


def load_style_guide() -> str:
    """
    Load the long-form writing style guide from config.
    
    Returns:
        Complete style guide text
        
    Raises:
        FileNotFoundError: If style guide doesn't exist
    """
    style_guide_path = Path("config/style_guide_longform.md")
    
    if not style_guide_path.exists():
        raise FileNotFoundError(f"Style guide not found at {style_guide_path}")
    
    with open(style_guide_path, "r", encoding="utf-8") as f:
        return f.read()


def write_essay(articles: List[Dict], style_guide: str) -> str:
    """
    Generate a Substack essay from smart glasses news articles.
    
    Uses OpenAI GPT-4 with the complete style guide to write
    an essay that follows the specified voice and structure.
    
    Args:
        articles: List of article dictionaries (from news API)
        style_guide: Complete style guide text
        
    Returns:
        Generated essay text (including title)
        
    Raises:
        ValueError: If OPENAI_API_KEY is not set
        openai.APIError: If OpenAI API call fails
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    
    client = OpenAI(api_key=api_key)
    
    # Format articles for the prompt
    articles_text = "\n\n".join([
        f"Article {i+1}: {article['title']}\n"
        f"Source: {article['source']}\n"
        f"Summary: {article['description']}\n"
        f"URL: {article['url']}"
        for i, article in enumerate(articles)
    ])
    
    # Construct the prompt
    prompt = f"""You are writing a Substack essay about recent developments in the smart glasses and AR/XR ecosystem.

RECENT ARTICLES (Last 24 Hours):
{articles_text}

WRITING STYLE GUIDE:
{style_guide}

YOUR TASK:
Write a thoughtful, 1200-1500 word essay that synthesizes these smart glasses developments.

CRITICAL REQUIREMENTS:
1. Follow the style guide EXACTLY - this is non-negotiable
2. Voice: Measured, reflective, quietly authoritative ("thinking honestly in public")
3. Structure: Do NOT start with a thesis. Circle the idea first with observations or tensions
4. Epistemic Hospitality: Accessible without jargon. Use cognitive pressure reducers like "You don't need to know the term..."
5. Essay Arc: Recognition → Normalization → Reframing → Deepening → Open Ending
6. One metaphor per paragraph maximum (metaphors are environments, not transitions)
7. Avoid: bullet points, numbered lists, exclamation points, statistics, urgent language, satisfying conclusions
8. Core throughline: "Modern life has optimized away the conditions required for depth"
9. End with reframing, NOT resolution or prescriptions

TITLE REQUIREMENTS:
- Create tension, don't promise outcomes
- No numbers, no "how to", no urgency
- Examples: "The [Abstract Noun] of [Condition]" or "Why [Group] [Quiet Truth]"

Generate the complete essay now, starting with the title:"""

    print("   Sending request to GPT-4 (this may take 30-60 seconds)...")
    
    response = client.chat.completions.create(
        model=os.getenv("MODEL", "gpt-4o"),
        messages=[
            {
                "role": "system", 
                "content": "You are a thoughtful essayist who writes with depth and intellectual integrity. You follow the provided style guide exactly."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=4096,
        temperature=float(os.getenv("WRITING_TEMPERATURE", "0.7"))
    )
    
    essay = response.choices[0].message.content
    
    return essay


def write_essay_simplified(articles: List[Dict]) -> str:
    """
    Simplified version that auto-loads style guide and generates essay.
    
    Args:
        articles: List of article dictionaries
        
    Returns:
        Generated essay text
    """
    style_guide = load_style_guide()
    return write_essay(articles, style_guide)
