# AI Ghostwriter & Smart Glasses Research Ecosystem

A multi-agent AI system powered by Python, LangGraph, and Anthropic Claude that automates news curation, progress tracking, and content generation for Substack essays and Twitter.

## Overview

This system implements a six-agent workflow that:

1. **Scouts** for smart glasses news (AR/XR/Android XR) via News APIs
2. **Curates** relevant articles using keyword matching + AI relevance scoring
3. **Chronicles** your daily build progress through CLI prompts
4. **Strategizes** by synthesizing news + progress into content hooks
5. **Ghostwrites** Substack essays and Twitter content in your unique voice
6. **Optimizes** all content for platform-specific formatting and engagement

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Daily Workflow Trigger                  │
└────────────────────┬────────────────────────────────────┘
                     │
          ┌──────────┴──────────┐
          │                     │
    ┌─────▼─────┐         ┌────▼────┐
    │   Scout   │         │Chronicler│
    │   Agent   │         │  Agent   │
    └─────┬─────┘         └────┬────┘
          │                    │
    ┌─────▼─────┐              │
    │  Curator  │              │
    │   Agent   │              │
    └─────┬─────┘              │
          │                    │
          └──────────┬─────────┘
                     │
              ┌──────▼──────┐
              │ Strategist  │
              │    Agent    │
              └──────┬──────┘
                     │
              ┌──────▼──────┐
              │ Ghostwriter │
              │    Agent    │
              └──────┬──────┘
                     │
              ┌──────▼──────┐
              │  Optimizer  │
              │    Agent    │
              └──────┬──────┘
                     │
              ┌──────▼──────┐
              │ Save Drafts │
              │ (Substack + │
              │   Twitter)  │
              └─────────────┘
```

## Features

- **Parallel Execution**: Scout and Chronicler agents run simultaneously for efficiency
- **Intelligent Fallbacks**: Uses cached data when APIs fail
- **Style Enforcement**: Comprehensive long-form style guide ensures consistent voice
- **Draft Management**: Version control and organization for all generated content
- **Interactive CLI**: User-friendly progress input and draft preview system
- **File-based Storage**: Simple JSON/Markdown persistence, no database required

## Quick Start

### Prerequisites

- Python 3.11 or higher
- Anthropic API key (for Claude)
- NewsAPI key (free tier available)

### Installation

1. **Clone and navigate to the project:**
   ```bash
   cd gengar-ai-ghostwriter
   ```

2. **Create and activate virtual environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   ```bash
   cp .env.example .env
   # Edit .env and add your API keys
   ```

5. **Configure your preferences:**
   - Edit `config/keywords.yaml` to customize news topics
   - Edit `config/sources.yaml` to add/remove news sources
   - Review `config/style_guide_longform.md` for the writing style

### Usage

#### Run the full workflow (daily execution):
```bash
python src/main.py run
```

This will:
1. Fetch smart glasses news from the last 24 hours
2. Prompt you to enter your daily progress
3. Generate content hooks
4. Write Substack essay and Twitter threads
5. Save drafts to `data/drafts/`

#### Test individual agents:
```bash
# Test news fetching only
python src/main.py scout

# Chronicle progress without generating content
python src/main.py chronicle

# Preview most recent drafts
python src/main.py preview

# Export drafts for publishing
python src/main.py export
```

#### Dry run (no API calls):
```bash
python src/main.py run --dry-run
```

## Configuration

### Environment Variables (.env)

```env
# Required
ANTHROPIC_API_KEY=your_claude_api_key_here
NEWS_API_KEY=your_newsapi_key_here

# Optional
GOOGLE_NEWS_API_KEY=your_google_news_key_here
LOG_LEVEL=INFO
```

### Keywords Configuration (config/keywords.yaml)

Define search terms and relevance scoring:

```yaml
brands:
  - name: "Meta Ray-Ban"
    weight: 1.0
  - name: "Apple Vision Pro"
    weight: 1.0
  - name: "Google Glass"
    weight: 0.8

technologies:
  - name: "Android XR"
    weight: 1.0
  - name: "ARCore"
    weight: 0.7

# ... more categories
```

### News Sources (config/sources.yaml)

Configure which news APIs and sources to use:

```yaml
newsapi:
  endpoint: "https://newsapi.org/v2/everything"
  sources: "techcrunch,the-verge,wired,ars-technica"
  language: "en"
  sort_by: "publishedAt"

# ... more sources
```

### Style Guide

The comprehensive writing style guide is in `config/style_guide_longform.md`. It defines:
- Voice: Measured, reflective, quietly authoritative
- Structure: Discovery-based, not thesis-first
- Epistemic Hospitality: Accessible without prerequisites
- Essay Arc: Recognition → Normalization → Reframing → Deepening → Open Ending

## Project Structure

```
gengar-ai-ghostwriter/
├── README.md                   # This file
├── requirements.txt            # Python dependencies
├── .env.example                # Environment variable template
├── prd.json                    # Complete task list PRD
│
├── config/                     # Configuration files
│   ├── style_guide_longform.md # Long-form essay style guide
│   ├── style_guide_twitter.yaml # Twitter formatting rules
│   ├── keywords.yaml           # Search terms and relevance weights
│   └── sources.yaml            # News API configurations
│
├── src/                        # Source code
│   ├── agents/                 # Agent implementations
│   │   ├── scout.py            # News fetching agent
│   │   ├── curator.py          # Article filtering agent
│   │   ├── chronicler.py       # Progress tracking agent
│   │   ├── strategist.py       # Content hook generator
│   │   ├── ghostwriter.py      # Essay and tweet writer
│   │   └── optimizer.py        # Content formatter
│   │
│   ├── graph/                  # LangGraph workflow
│   │   ├── workflow.py         # Main graph definition
│   │   └── state.py            # State schema
│   │
│   ├── utils/                  # Shared utilities
│   │   ├── news_api.py         # News API client
│   │   ├── claude_client.py    # Anthropic API wrapper
│   │   ├── cache.py            # Caching system
│   │   ├── storage.py          # File storage utilities
│   │   ├── validators.py       # Style validation
│   │   └── logging.py          # Logging configuration
│   │
│   └── main.py                 # CLI entry point
│
├── data/                       # Generated data (gitignored)
│   ├── cache/                  # Cached news articles
│   ├── progress/               # Daily progress logs
│   └── drafts/                 # Generated content drafts
│
└── tests/                      # Test suite
    ├── test_agents.py
    ├── test_workflow.py
    └── test_utils.py
```

## Agent Details

### Scout Agent
- **Purpose**: Fetch recent smart glasses news
- **Sources**: NewsAPI, Google News API
- **Output**: Raw articles with metadata (title, URL, summary, date)
- **Caching**: 24-hour TTL to avoid redundant API calls

### Curator Agent
- **Purpose**: Filter articles for relevance
- **Method**: Keyword scoring + Claude-based relevance assessment
- **Output**: Top 5-10 most relevant articles
- **Scoring**: Weighted combination of keyword matches and AI judgment

### Chronicler Agent
- **Purpose**: Capture your daily build progress
- **Interface**: Interactive CLI prompts
- **Questions**: Work summary, breakthroughs, blockers, artifacts
- **Output**: Structured progress log (JSON + Markdown)

### Strategist Agent
- **Purpose**: Generate content hooks
- **Input**: Curated news + progress notes
- **Strategy**: Connect external trends to internal work
- **Output**: 3-5 content hooks with narrative guidance

### Ghostwriter Agent
- **Purpose**: Write essays and tweets
- **Style**: Measured, reflective, epistemic hospitality
- **Formats**: 
  - Substack: 1200-2000 word essays
  - Twitter: Threads (5-10 tweets) + standalone tweets
- **Output**: Markdown essays + JSON tweet structures

### Optimizer Agent
- **Purpose**: Format and polish content
- **Substack**: Heading hierarchy, pull quotes, reading time
- **Twitter**: Character limits, thread numbering, hashtag placement
- **Quality**: Grammar check, consistency, link validation

## Development

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_agents.py
```

### Code Quality

```bash
# Format code
black src/ tests/

# Lint
ruff check src/ tests/

# Type checking
mypy src/
```

## Troubleshooting

### API Key Issues
- Ensure `.env` file exists and contains valid API keys
- Check API key permissions and rate limits
- Try dry-run mode to validate without API calls: `python src/main.py run --dry-run`

### No Articles Found
- Check `config/keywords.yaml` - keywords might be too specific
- Verify `config/sources.yaml` - news sources may be misconfigured
- Check cached articles in `data/cache/` for recent fetches

### Style Validation Failures
- Review `config/style_guide_longform.md` for requirements
- Check validator output for specific violations
- Essays are iteratively improved - some violations are expected in first draft

### Memory/Performance Issues
- Reduce number of articles processed by Curator (lower threshold)
- Use caching aggressively (check `data/cache/`)
- Consider using smaller Claude models for less critical agents

## Contributing

See `prd.json` for the complete task list and implementation details. Each task includes:
- Detailed description
- Acceptance criteria
- Dependencies
- Estimated complexity

## License

[Your License Here]

## Acknowledgments

Built with:
- [LangGraph](https://github.com/langchain-ai/langgraph) - Agent orchestration
- [Anthropic Claude](https://www.anthropic.com/) - LLM provider
- [NewsAPI](https://newsapi.org/) - News data source
