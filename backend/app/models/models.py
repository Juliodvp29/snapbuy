from sqlalchemy import Column, String, Float, Integer, Boolean, Text, ForeignKey, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import datetime, timezone
import uuid

class Product(Base):
    __tablename__ = "products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = Column(Text, nullable=False)
    category = Column(String(100))
    image_url = Column(Text)
    store = Column(String(100), nullable=False)
    product_url = Column(Text, unique=True, nullable=False)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    prices = relationship("ProductPrice", back_populates="product")
    search_results = relationship("SearchResult", back_populates="product")


class ProductPrice(Base):
    __tablename__ = "product_prices"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id", ondelete="CASCADE"))
    price = Column(Float, nullable=False)
    currency = Column(String(3), default="USD")
    in_stock = Column(Boolean, default=True)
    scraped_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    product = relationship("Product", back_populates="prices")


class Search(Base):
    __tablename__ = "searches"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    image_hash = Column(Text, nullable=False)
    category = Column(String(100))
    confidence = Column(Float)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))

    results = relationship("SearchResult", back_populates="search")


class SearchResult(Base):
    __tablename__ = "search_results"

    search_id = Column(UUID(as_uuid=True), ForeignKey("searches.id"), primary_key=True)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.id"), primary_key=True)
    score = Column(Float)
    rank = Column(Integer)
    badge = Column(String(50))

    search = relationship("Search", back_populates="results")
    product = relationship("Product", back_populates="search_results")