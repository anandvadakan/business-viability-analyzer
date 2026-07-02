"""
Core unit-economics and viability calculations.
No external calls here — pure math, easy to unit test.
"""

def calculate_kpis(data: dict) -> dict:
    revenue = data["monthly_revenue"]
    cogs = data["monthly_cogs"]
    opex = data["monthly_opex"]
    cash_on_hand = data.get("cash_on_hand", 0)
    customers = data.get("customer_count", 0)
    cac = data.get("cac", 0)
    avg_customer_lifetime_months = data.get("avg_customer_lifetime_months", 12)

    gross_profit = revenue - cogs
    gross_margin_pct = (gross_profit / revenue * 100) if revenue else 0

    net_profit = gross_profit - opex
    net_margin_pct = (net_profit / revenue * 100) if revenue else 0

    burn_rate = -net_profit if net_profit < 0 else 0
    runway_months = (cash_on_hand / burn_rate) if burn_rate > 0 else None

    arpu = (revenue / customers) if customers else 0
    ltv = arpu * avg_customer_lifetime_months
    ltv_cac_ratio = (ltv / cac) if cac else None

    breakeven_revenue = opex + cogs  # revenue needed to hit zero net profit at current cost ratios
    opex_pct_of_revenue = (opex / revenue * 100) if revenue else 0
    cogs_pct_of_revenue = (cogs / revenue * 100) if revenue else 0

    return {
        "gross_profit": round(gross_profit, 2),
        "gross_margin_pct": round(gross_margin_pct, 2),
        "net_profit": round(net_profit, 2),
        "net_margin_pct": round(net_margin_pct, 2),
        "burn_rate": round(burn_rate, 2),
        "runway_months": round(runway_months, 1) if runway_months else None,
        "arpu": round(arpu, 2),
        "ltv": round(ltv, 2),
        "ltv_cac_ratio": round(ltv_cac_ratio, 2) if ltv_cac_ratio else None,
        "breakeven_revenue": round(breakeven_revenue, 2),
        "opex_pct_of_revenue": round(opex_pct_of_revenue, 2),
        "cogs_pct_of_revenue": round(cogs_pct_of_revenue, 2),
    }
