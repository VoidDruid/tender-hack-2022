from datetime import timezone, timedelta, datetime

from sqlalchemy import Column, Integer, String, Text, JSONB, DateTime, Double

from . import Base

TIMEZONE = timezone(timedelta(hours=3))


def get_now() -> datetime:
    return datetime.now(tz=TIMEZONE)


class Mapping(Base):
    __tablename__ = "mappings"
    product_id = Column(ForeignKey("products.product_id"), primary_key=True)
    contract_id = Column(ForeignKey("contracts.contract_id"), primary_key=True)
    product = relationship("Product", back_populates="contracts")
    contract = relationship("Contract", back_populates="products")
    quantity = Column(Integer, nullable=False)
    amount = Column(Double, nullable=False)


class Product(Base):
    __tablename__ = "products"
    id = Column("product_id", Integer, primary_key=True, index=True)
    name = Column(Text, nullable=False)
    category = Column(String(50), nullable=False)
    category_id = Column(Integer, index=True, nullable=False)
    code = Column(String(50), nullable=False)
    features = JSONB(nullable=False)
    contracts = relationship("Mapping", back_populates="product")


class Contract(Base):
    __tablename__ = "contracts"
    id = Column("contract_id", Integer, primary_key=True, index=True)
    # created_at = Column(DateTime, default=get_now, nullable=False)
    # deal_at = Column(DateTime, default=get_now, nullable=False)
    # price = Column(Integer)
    # inn_order = Column(String)
    # kpp_order = Column(String)
    products = relationship("Mapping", back_populates="contract")


