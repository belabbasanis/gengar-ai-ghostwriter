# Contributing to AI Ghostwriter

Thank you for your interest in contributing to the AI Ghostwriter project!

## Development Setup

1. **Fork and clone the repository**
   ```bash
   git clone https://github.com/yourusername/gengar-ai-ghostwriter.git
   cd gengar-ai-ghostwriter
   ```

2. **Create a virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Add your API keys to .env
   ```

## Development Workflow

### Before Starting Work

1. **Check the PRD**: Review `prd.json` to see all planned tasks
2. **Check for issues**: Look for related issues or create one
3. **Create a branch**: Use descriptive branch names
   ```bash
   git checkout -b feature/agent-improvements
   ```

### While Working

1. **Follow the style guide**: 
   - Use Black for code formatting: `black src/`
   - Use Ruff for linting: `ruff check src/`
   - Type hints for all functions

2. **Write tests**: 
   - Unit tests for utilities
   - Integration tests for agents
   - Aim for 80%+ coverage

3. **Document your code**:
   - Docstrings for all public functions
   - Comments for complex logic
   - Update README if adding features

### Code Style

```python
"""Module docstring explaining purpose."""

from typing import List, Dict, Optional
import anthropic


def process_articles(
    articles: List[Dict],
    min_score: float = 0.3
) -> List[Dict]:
    """
    Process and filter articles based on relevance score.
    
    Args:
        articles: List of article dictionaries with metadata
        min_score: Minimum relevance score threshold (0.0-1.0)
        
    Returns:
        Filtered list of articles above threshold
        
    Raises:
        ValueError: If min_score is outside valid range
    """
    if not 0.0 <= min_score <= 1.0:
        raise ValueError(f"Invalid min_score: {min_score}")
        
    return [
        article for article in articles
        if article.get("relevance_score", 0) >= min_score
    ]
```

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src tests/

# Run specific test file
pytest tests/test_agents.py

# Run with verbose output
pytest -v
```

## Submitting Changes

### Before Submitting

1. **Run all tests**: Ensure `pytest` passes
2. **Format code**: Run `black src/ tests/`
3. **Check linting**: Run `ruff check src/ tests/`
4. **Update documentation**: If you changed functionality

### Pull Request Process

1. **Commit your changes**
   ```bash
   git add .
   git commit -m "feat: add Scout agent retry logic"
   ```

2. **Push to your fork**
   ```bash
   git push origin feature/agent-improvements
   ```

3. **Open a Pull Request**
   - Use descriptive title
   - Reference related issues
   - Explain what changed and why
   - Include test results

### Commit Message Format

Use conventional commits:

- `feat:` New feature
- `fix:` Bug fix
- `docs:` Documentation changes
- `test:` Adding or updating tests
- `refactor:` Code refactoring
- `style:` Code style changes (formatting)
- `chore:` Maintenance tasks

Examples:
```
feat: add parallel execution for Scout and Chronicler
fix: handle API timeout errors in NewsAPI client
docs: add examples to Strategist agent documentation
test: add integration tests for full workflow
```

## Areas for Contribution

### High Priority

1. **Agent Improvements**
   - Better prompt engineering for Strategist
   - Improved style validation for Ghostwriter
   - Enhanced curation algorithms

2. **Error Handling**
   - More robust API retry logic
   - Better fallback strategies
   - Improved error messages

3. **Testing**
   - Increase test coverage
   - Add edge case tests
   - Performance benchmarks

### Medium Priority

1. **Features**
   - Support for additional news sources
   - Alternative LLM providers
   - Web interface for draft management

2. **Documentation**
   - Video tutorials
   - More code examples
   - Architecture diagrams

3. **Performance**
   - Caching optimizations
   - Parallel processing improvements
   - Token usage optimization

### Good First Issues

Look for issues labeled `good first issue`:
- Configuration file improvements
- Documentation updates
- Adding unit tests
- Small bug fixes

## Questions?

- **Check the PRD**: `prd.json` has detailed task descriptions
- **Read the docs**: `README.md` and `IMPLEMENTATION_ROADMAP.md`
- **Open an issue**: For questions or clarifications

## Code of Conduct

Be respectful and constructive in all interactions. This is a learning and building space.

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
