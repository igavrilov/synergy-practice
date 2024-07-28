import asyncio
from decimal import Decimal
from typing import Annotated

from sqlalchemy import Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, registry
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker

import settings


engine = create_async_engine(settings.DATABASE_URL)
Session = async_sessionmaker(engine, expire_on_commit=False)


money = Annotated[Numeric, 10, 4]


class Base(AsyncAttrs, DeclarativeBase):
    registry = registry(
        type_annotation_map={
            money: Numeric(10, 3, asdecimal=True)
        }
    )


class ExchangeRate(Base):
    __tablename__ = "exchange_rate"

    currency: Mapped[str] = mapped_column(primary_key=True)
    rate: Mapped[money]


async def initdb():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with Session() as session:
        async with session.begin():
            session.add_all([
                ExchangeRate(currency="USD", rate=Decimal("1.000")),
                ExchangeRate(currency="RUR", rate=Decimal("85.901")),
                ExchangeRate(currency="EUR", rate=Decimal("0.853")),
                ExchangeRate(currency="JPY", rate=Decimal("110.000")),
                ExchangeRate(currency="GBP", rate=Decimal("0.754")),
                ExchangeRate(currency="AUD", rate=Decimal("1.352")),
            ])


if __name__ == "__main__":
    asyncio.run(initdb())
