import typing
from decimal import Decimal

import sqlalchemy as sa
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

import settings
from database import ExchangeRate, Session

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ConversionRequest(BaseModel):
    from_currency: str
    to_currency: str
    amount: Decimal


@app.post("/convert")
async def convert_currency(conversion_request: ConversionRequest):
    from_currency = conversion_request.from_currency.upper()
    to_currency = conversion_request.to_currency.upper()
    amount = conversion_request.amount

    async with Session() as session:
        from_rate = (
            await session.execute(
                sa.select(ExchangeRate).filter(ExchangeRate.currency == from_currency)
            )
        ).scalars().first()
        to_rate = (
            await session.execute(
                sa.select(ExchangeRate).filter(ExchangeRate.currency == to_currency)
            )
        ).scalars().first()

    if not from_rate or not to_rate:
        raise HTTPException(status_code=400, detail="Invalid currency code")

    rate = to_rate.rate / from_rate.rate  # pyright: ignore
    converted_amount = amount * rate

    return {
        "from_currency": from_currency,
        "to_currency": to_currency,
        "amount": amount,
        "converted_amount": converted_amount,
        "rate": rate
    }
