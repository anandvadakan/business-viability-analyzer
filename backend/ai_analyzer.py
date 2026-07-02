"""
Sends KPIs + market snapshot to Groq (free, fast Llama 3.3 70B), gets back
a written diagnosis: where money is leaking, and a suggested different approach.
"""
import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_diagnosis(business_input: dict, kpis: dict, market: dict) -> str:
    prompt = f"""You are a sharp, no-fluff business analyst. Analyze this company's unit economics.

BUSINESS INPUT:
{business_input}

CALCULATED KPIs:
{kpis}

CURRENT MARKET CONDITIONS (last 5 days):
{market}

Give me:
1. A one-line verdict: is this business currently profitable / breakeven / burning cash?
2. The single biggest leak — where is money actually being lost (COGS, OPEX, CAC inefficiency, etc)? Be specific with numbers.
3. How current market conditions (forex, oil, index movement) affect this business's near-term costs or pricing power, if at all — say clearly if they're irrelevant instead of forcing a connection.
4. One concrete alternative approach — a pricing change, cost cut, or channel shift — with a rough estimate of the impact if implemented.

Keep it tight. No generic startup advice. Numbers over adjectives."""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        max_tokens=1000,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
