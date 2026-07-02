# Business Viability Analyzer

Computes core unit economics (gross margin, net margin, burn rate, runway, LTV:CAC),
pulls live market indicators (USD/INR, crude oil, Nifty 50), and generates an AI-written
diagnosis of where money is leaking and what to change — using Claude.

## Setup

1. `cd backend`
2. `python -m venv venv && source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
3. `pip install -r ../requirements.txt`
4. Copy `.env.example` to `.env` and add your Groq API key
5. `uvicorn main:app --reload --port 8000`
6. Open `frontend/index.html` in your browser (just double-click it)
7. Fill in the numbers, click Analyze

## Stack
- FastAPI backend
- yfinance for live market data (no API key needed)
- Claude API (Sonnet) for the written diagnosis
- Plain HTML/JS frontend — no build step
