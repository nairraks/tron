"""
ETF Models - Pydantic models for ETF data.
"""

from pydantic import BaseModel


class ETFPriceResponse(BaseModel):
    """Response model for ETF price data."""
    symbol: str
    name: str
    price: float
    currency: str
    timestamp: str


class ErrorResponse(BaseModel):
    """Response model for errors."""
    error: str
    detail: str
