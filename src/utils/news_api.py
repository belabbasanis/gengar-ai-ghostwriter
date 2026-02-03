"""
News API client for fetching smart glasses articles.
Simplified MVP version - no caching, basic error handling.
"""

import os
import requests
from datetime import datetime, timedelta
from typing import List, Dict


def fetch_smart_glasses_news(limit: int = 10) -> List[Dict]:
    """
    Fetch recent smart glasses news from NewsAPI.
    
    Args:
        limit: Maximum number of articles to fetch (default: 10)
        
    Returns:
        List of article dictionaries with title, description, url, source, published_at
        
    Raises:
        ValueError: If NEWS_API_KEY is not set
        requests.HTTPError: If API request fails
    """
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        raise ValueError("NEWS_API_KEY environment variable is not set")
    
    # Fetch news from the last 24 hours
    yesterday = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")
    
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": "smart glasses OR AR glasses OR Android XR OR Apple Vision Pro OR Meta Ray-Ban",
        "from": yesterday,
        "sortBy": "publishedAt",
        "language": "en",
        "pageSize": limit,
        "apiKey": api_key
    }
    
    print(f"   Querying NewsAPI for articles since {yesterday}...")
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    
    data = response.json()
    
    if data.get("status") != "ok":
        raise Exception(f"NewsAPI error: {data.get('message', 'Unknown error')}")
    
    articles = data.get("articles", [])
    
    # Format articles for easier consumption
    formatted_articles = [
        {
            "title": article["title"],
            "description": article.get("description", "No description available"),
            "url": article["url"],
            "source": article["source"]["name"],
            "published_at": article["publishedAt"]
        }
        for article in articles
        if article.get("title") and article.get("title") != "[Removed]"
    ]
    
    return formatted_articles


def format_articles_for_prompt(articles: List[Dict]) -> str:
    """
    Format articles into a readable text block for LLM prompts.
    
    Args:
        articles: List of article dictionaries
        
    Returns:
        Formatted string with all articles
    """
    if not articles:
        return "No articles available."
    
    formatted = []
    for i, article in enumerate(articles, 1):
        formatted.append(
            f"Article {i}: {article['title']}\n"
            f"Source: {article['source']}\n"
            f"Published: {article['published_at']}\n"
            f"Summary: {article['description']}\n"
            f"URL: {article['url']}"
        )
    
    return "\n\n".join(formatted)
