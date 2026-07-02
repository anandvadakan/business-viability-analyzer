from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from kpi_calculator import calculate_kpis
from market_data import get_market_snapshot
from ai_analyzer import generate_diagnosis

app = FastAPI(title="Business Viability Analyzer")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class BusinessInput(BaseModel):
    monthly_revenue: float
    monthly_cogs: float
    monthly_opex: float
    cash_on_hand: float = 0
    customer_count: int = 0
    cac: float = 0
    avg_customer_lifetime_months: float = 12

@app.post("/analyze")
def analyze(data: BusinessInput):
    business_input = data.dict()
    kpis = calculate_kpis(business_input)
    market = get_market_snapshot()
    diagnosis = generate_diagnosis(business_input, kpis, market)
    return {
        "kpis": kpis,
        "market": market,
        "diagnosis": diagnosis,
    }

@app.get("/market")
def market():
    return get_market_snapshot()
