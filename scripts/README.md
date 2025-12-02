# Daily ArXiv Paper Tracker

Automated script to fetch and summarize latest ArXiv papers, updating GitHub profile README.

## Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Set your DeepSeek API key:

```bash
export DEEPSEEK_API_KEY="your-api-key-here"
```

Or create a `.env` file (for local testing):
```
DEEPSEEK_API_KEY=your-api-key-here
```

## Usage

Run manually:

```bash
python3 scripts/daily_arxiv.py
```

## Automation

This script is designed to run via GitHub Actions (see `.github/workflows/daily-papers.yml`).

**Important**: Add your `DEEPSEEK_API_KEY` as a GitHub Secret:
1. Go to your repository Settings → Secrets and variables → Actions
2. Click "New repository secret"
3. Name: `DEEPSEEK_API_KEY`
4. Value: Your DeepSeek API key

## Features

- Fetches latest papers from ArXiv API
- Translates full summaries to Chinese using DeepSeek API (high-quality, preserves technical terms)
- Updates both `README.md` and `README_CN.md` automatically

