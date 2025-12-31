"""
Tests for ETF API endpoint.
"""

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


class TestETFEndpoint:
    """Tests for the /etf/{symbol} endpoint."""
    
    def test_valid_etf_symbol_spy(self, client):
        """Test that a valid ETF symbol returns price data."""
        response = client.get("/etf/SPY")
        assert response.status_code == 200
        
        data = response.json()
        assert data["symbol"] == "SPY"
        assert "name" in data
        assert "price" in data
        assert isinstance(data["price"], (int, float))
        assert data["price"] > 0
        assert "currency" in data
        assert "timestamp" in data
    
    def test_valid_etf_symbol_qqq(self, client):
        """Test QQQ ETF symbol."""
        response = client.get("/etf/QQQ")
        assert response.status_code == 200
        
        data = response.json()
        assert data["symbol"] == "QQQ"
        assert data["price"] > 0
    
    def test_symbol_case_insensitive(self, client):
        """Test that symbol lookup is case insensitive."""
        response = client.get("/etf/spy")
        assert response.status_code == 200
        
        data = response.json()
        assert data["symbol"] == "SPY"  # Should be uppercase in response
    
    def test_invalid_symbol_format(self, client):
        """Test that invalid symbol format returns 400."""
        response = client.get("/etf/INVALID-SYMBOL!")
        assert response.status_code == 400
    
    def test_nonexistent_symbol(self, client):
        """Test that nonexistent symbol returns 404."""
        response = client.get("/etf/ZZZZZZZ")
        assert response.status_code == 404
    
    def test_response_schema(self, client):
        """Test that response matches expected schema."""
        response = client.get("/etf/VTI")
        assert response.status_code == 200
        
        data = response.json()
        required_fields = ["symbol", "name", "price", "currency", "timestamp"]
        for field in required_fields:
            assert field in data, f"Missing required field: {field}"


class TestHealthEndpoint:
    """Tests for the /health endpoint."""
    
    def test_health_check(self, client):
        """Test health check returns healthy status."""
        response = client.get("/health")
        assert response.status_code == 200
        assert response.json() == {"status": "healthy"}


class TestRootEndpoint:
    """Tests for the / endpoint."""
    
    def test_hello_world(self, client):
        """Test root endpoint returns greeting."""
        response = client.get("/")
        assert response.status_code == 200
        
        data = response.json()
        assert data["message"] == "Hello, World!"
        assert data["service"] == "Tron"
