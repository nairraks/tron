"""
ETF Router - API routes for ETF price lookup.
"""

from datetime import datetime, timezone
import re

from fastapi import APIRouter, HTTPException
import yfinance as yf

from .models import ETFPriceResponse, ErrorResponse


# Create router for ETF endpoints
router = APIRouter(prefix="/etf", tags=["ETF"])


@router.get(
    "/{symbol}",
    response_model=ETFPriceResponse,
    responses={
        404: {"model": ErrorResponse, "description": "ETF not found"},
        400: {"model": ErrorResponse, "description": "Invalid symbol format"}
    }
)
async def get_etf_price(symbol: str):
    """
    Get ETF Price
    
    Returns the current price and metadata for an ETF.
    
    Parameters:
    - **symbol**: The ETF ticker symbol (e.g., SPY, QQQ, VTI)
    
    Returns the symbol, name, current price, currency, and timestamp.
    """
    # Validate symbol format (alphanumeric, 1-10 characters)
    symbol = symbol.upper().strip()
    if not re.match(r'^[A-Z0-9]{1,10}$', symbol):
        raise HTTPException(
            status_code=400,
            detail={"error": "Invalid symbol", "detail": f"Symbol '{symbol}' is not a valid ETF ticker format"}
        )
    
    try:
        # Fetch ETF data using yfinance
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        # Check if we got valid data
        if not info or info.get('regularMarketPrice') is None:
            # Try getting price from history as fallback
            hist = ticker.history(period="1d")
            if hist.empty:
                raise HTTPException(
                    status_code=404,
                    detail={"error": "ETF not found", "detail": f"Could not find ETF data for symbol '{symbol}'"}
                )
            price = float(hist['Close'].iloc[-1])
            name = info.get('shortName') or info.get('longName') or symbol
            currency = info.get('currency', 'USD')
        else:
            price = info.get('regularMarketPrice') or info.get('previousClose', 0)
            name = info.get('shortName') or info.get('longName') or symbol
            currency = info.get('currency', 'USD')
        
        return ETFPriceResponse(
            symbol=symbol,
            name=name,
            price=round(price, 2),
            currency=currency,
            timestamp=datetime.now(timezone.utc).isoformat()
        )
        
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=404,
            detail={"error": "ETF not found", "detail": f"Error fetching data for '{symbol}': {str(e)}"}
        )
