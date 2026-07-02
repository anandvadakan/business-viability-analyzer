"""
Pulls a few free, no-API-key market indicators via yfinance,
so the AI diagnosis can factor in current conditions.
"""
import yfinance as yf

TICKERS = {
    "usd_inr": "INR=X",
    "crude_oil": "CL=F",
    "nifty50": "^NSEI",
}

def get_market_snapshot() -> dict:
    snapshot = {}
    for label, ticker in TICKERS.items():
        try:
            t = yf.Ticker(ticker)
            hist = t.history(period="5d")
            if not hist.empty:
                latest = hist["Close"].iloc[-1]
                prev = hist["Close"].iloc[0]
                change_pct = ((latest - prev) / prev) * 100
                snapshot[label] = {
                    "latest": round(float(latest), 2),
                    "change_pct_5d": round(float(change_pct), 2),
                }
        except Exception as e:
            snapshot[label] = {"error": str(e)}
    return snapshot
