# Data Directory

This directory stores all generated and cached data for the AI Ghostwriter system.

## Directory Structure

### `cache/`
Cached news articles to avoid redundant API calls.

- **Format**: JSON files named by date (e.g., `2024-01-15.json`)
- **TTL**: 24 hours (configurable via `.env`)
- **Purpose**: Reduce API costs and enable offline development

### `progress/`
Daily progress logs captured by the Chronicler agent.

- **Format**: 
  - `YYYY-MM-DD.json` - Machine-readable structured data
  - `YYYY-MM-DD.md` - Human-readable markdown summary
- **Contents**: Work summary, breakthroughs, blockers, artifacts
- **Purpose**: Track build progress for content synthesis

### `drafts/`
Generated content drafts (Substack essays and Twitter threads).

- **Format**:
  - Essays: `essay_YYYY-MM-DD_ID.md` - Markdown with frontmatter
  - Tweets: `twitter_YYYY-MM-DD_ID.json` - Structured JSON
- **Metadata**: Creation date, content hook ID, version, status
- **Purpose**: Store drafts for review before publishing

## File Naming Conventions

### Cached Articles
```
cache/articles_2024-01-15.json
```

### Progress Logs
```
progress/2024-01-15.json
progress/2024-01-15.md
```

### Drafts
```
drafts/essay_2024-01-15_abc123.md
drafts/twitter_2024-01-15_thread_abc123.json
drafts/twitter_2024-01-15_standalone_abc123.json
```

## Maintenance

The system automatically:
- Cleans up expired cache entries (older than TTL)
- Archives old drafts (30+ days, configurable)
- Maintains reasonable disk usage (max ~100MB by default)

Manual cleanup:
```bash
python src/main.py cleanup
```

## Backup Recommendations

While most data is regenerable, consider backing up:
- **Progress logs** (`progress/`) - These contain your daily notes
- **Published drafts** - Archive drafts that you've published

Cache and unpublished drafts can be safely deleted.

## .gitignore

All data directories are excluded from version control by default to protect:
- API responses (potentially sensitive)
- Personal progress notes
- Draft content before publication

Only `.gitkeep` files are tracked to preserve directory structure.
