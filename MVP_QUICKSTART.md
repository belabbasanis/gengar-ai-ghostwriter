# MVP Quickstart Guide 🚀

Get from zero to your first AI-generated essay in **5 minutes**!

## What This MVP Does

```
Fetch News → Generate Essay → Save Draft
   (10 articles)   (Claude AI)    (Markdown file)
```

**Skips**: Curation, Progress Tracking, Content Hooks, Optimization, Twitter
**Focuses**: Core workflow - news to essay with your writing style

## Setup (One-Time, ~2 minutes)

### 1. Install Dependencies

```bash
cd /Users/laughingbull/Sandbox/dev/apps/gengar-ai-ghostwriter

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install minimal dependencies for MVP
pip install python-dotenv requests anthropic
```

### 2. Get API Keys (FREE tiers available)

**Anthropic Claude** (Required)
- Go to: https://console.anthropic.com/
- Sign up and create an API key
- Free tier: $5 credit (enough for ~50 essays)

**NewsAPI** (Required)
- Go to: https://newsapi.org/register
- Sign up for free developer account
- Free tier: 100 requests/day (plenty for daily use)

### 3. Create .env File

```bash
cat > .env << 'EOF'
# Anthropic Claude API Key (get from https://console.anthropic.com/)
ANTHROPIC_API_KEY=your_anthropic_key_here

# NewsAPI Key (get from https://newsapi.org/register)
NEWS_API_KEY=your_newsapi_key_here

# Optional: Change Claude model (default: claude-3-5-sonnet-20241022)
CLAUDE_MODEL=claude-3-5-sonnet-20241022
EOF
```

**⚠️ Important**: Replace `your_anthropic_key_here` and `your_newsapi_key_here` with your actual API keys!

## Run the MVP (~1 minute)

```bash
# Make sure you're in the project directory
cd /Users/laughingbull/Sandbox/dev/apps/gengar-ai-ghostwriter

# Activate virtual environment
source venv/bin/activate

# Run the MVP!
python src/mvp.py
```

## Expected Output

```
============================================================
🚀 AI GHOSTWRITER MVP - Smart Glasses Edition
============================================================

📰 STEP 1: Fetching smart glasses news
------------------------------------------------------------
   Querying NewsAPI for articles since 2024-02-02...
   ✅ Found 10 articles

   Recent headlines:
   1. Meta unveils new Ray-Ban smart glasses with AI features...
   2. Apple Vision Pro sales exceed expectations in Q1...
   3. Google announces Android XR platform for developers...
   4. Snap introduces Spectacles 5 with improved AR capabilities...
   5. XREAL launches Air 2 Ultra with spatial computing...

✍️  STEP 2: Generating essay with Claude
------------------------------------------------------------
   Loading writing style guide...
   Composing prompt with articles + style guide...
   Sending request to Claude (this may take 30-60 seconds)...

💾 STEP 3: Saving draft
------------------------------------------------------------
   ✅ Essay saved to: data/drafts/essay_2024-02-03_143022.md

📊 STATISTICS
------------------------------------------------------------
   Words: 1,347
   Characters: 8,234
   Paragraphs: 18
   Reading time: ~6 minutes

============================================================
✨ SUCCESS! Your essay is ready for review.
============================================================

Next steps:
1. Review the draft: cat data/drafts/essay_2024-02-03_143022.md
2. Edit as needed
3. Publish to Substack

To generate another essay, run: python src/mvp.py
```

## What You Get

Your essay will be saved in `data/drafts/` with:
- ✅ **Your unique writing voice** (measured, reflective, authoritative)
- ✅ **Epistemic hospitality** (accessible without jargon)
- ✅ **Proper essay arc** (Recognition → Reframing → Open Ending)
- ✅ **1200-1500 words** (perfect for Substack)
- ✅ **Smart glasses focus** (AR/XR/Android XR news)

## View Your Essay

```bash
# View in terminal
cat data/drafts/essay_2024-02-03_143022.md

# Or open in your editor
code data/drafts/essay_2024-02-03_143022.md
```

## Customization

### Change Keywords
Edit the search query in `src/utils/news_api.py` line 32:
```python
"q": "smart glasses OR AR glasses OR Android XR OR Apple Vision Pro OR Meta Ray-Ban",
```

### Change Article Count
Run with more/fewer articles:
```bash
# Modify limit in src/mvp.py line 53
articles = fetch_smart_glasses_news(limit=15)  # Get 15 instead of 10
```

### Change Writing Style
Edit `config/style_guide_longform.md` to adjust voice and constraints.

## Troubleshooting

### "Missing required environment variables"
- Check that `.env` file exists in project root
- Verify API keys are set (not placeholder text)
- Try: `cat .env` to view your configuration

### "No articles found"
- This is normal on slow news days
- Try expanding the date range or keywords
- NewsAPI free tier has some limitations

### "Rate limit exceeded"
- **NewsAPI**: Free tier = 100 requests/day (resets at midnight UTC)
- **Claude**: Free tier = $5 credit, plenty for testing
- Wait or upgrade to paid tier

### "Connection timeout"
- Check internet connection
- Verify API keys are correct
- Try again (temporary API issue)

## Cost Estimate

**NewsAPI**: FREE (100 requests/day)
**Claude**: ~$0.10 per essay (1500 words × 2 for input/output)

Daily cost for one essay: **~$0.10**
Monthly cost (daily essays): **~$3.00**

The $5 free Claude credit = ~50 essays = testing for ~7 weeks daily!

## What's Next?

Once the MVP works, you can add:

1. **Curation** - Filter articles by relevance (Curator agent)
2. **Progress Tracking** - Add your daily notes (Chronicler agent)
3. **Content Hooks** - Better essay angles (Strategist agent)
4. **Twitter Threads** - Auto-generate tweets
5. **Optimization** - Polish and format for engagement
6. **Full CLI** - Commands like `preview`, `export`, etc.

See `IMPLEMENTATION_ROADMAP.md` for the complete build plan.

## Daily Workflow (Once Set Up)

```bash
# Every morning:
cd /Users/laughingbull/Sandbox/dev/apps/gengar-ai-ghostwriter
source venv/bin/activate
python src/mvp.py

# 1 minute later:
# ✅ Essay ready in data/drafts/
# → Copy to Substack
# → Publish!
```

## Need Help?

- Check `README.md` for full documentation
- Review `prd.json` for complete feature list
- See `IMPLEMENTATION_ROADMAP.md` for next steps

---

**Time to first essay**: ~5 minutes
**Daily workflow**: ~1 minute (+ 5-10 minutes to review/edit)
**Cost**: ~$0.10 per essay

Happy writing! ✍️
