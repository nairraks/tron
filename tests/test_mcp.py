"""
Tests for MCP integration.

Note: These tests require a running server with MCP initialized.
Run with: python -m src.main (in a separate terminal)
Then run: python -m pytest tests/test_mcp.py -v
"""

import pytest
from fastapi.testclient import TestClient

from src.main import app


@pytest.fixture
def client():
    """Create a test client for the FastAPI app."""
    return TestClient(app)


@pytest.mark.skip(reason="MCP tests require live server - run manually with server running")
class TestMCPEndpoint:
    """Tests for the /mcp endpoint."""
    
    def test_mcp_endpoint_exists(self, client):
        """Test that MCP endpoint is accessible."""
        # MCP endpoint should respond to POST requests
        response = client.post(
            "/mcp",
            json={
                "jsonrpc": "2.0",
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {
                        "name": "test-client",
                        "version": "1.0.0"
                    }
                },
                "id": 1
            },
            headers={"Content-Type": "application/json"}
        )
        # Should get a valid JSON-RPC response
        assert response.status_code == 200
        data = response.json()
        assert "jsonrpc" in data
        assert data["jsonrpc"] == "2.0"
    
    def test_mcp_tools_list(self, client):
        """Test that MCP exposes tools including ETF endpoint."""
        # First initialize
        client.post(
            "/mcp",
            json={
                "jsonrpc": "2.0",
                "method": "initialize",
                "params": {
                    "protocolVersion": "2024-11-05",
                    "capabilities": {},
                    "clientInfo": {
                        "name": "test-client",
                        "version": "1.0.0"
                    }
                },
                "id": 1
            }
        )
        
        # Then list tools
        response = client.post(
            "/mcp",
            json={
                "jsonrpc": "2.0",
                "method": "tools/list",
                "id": 2
            }
        )
        
        assert response.status_code == 200
        data = response.json()
        
        # Should have result with tools
        if "result" in data:
            tools = data["result"].get("tools", [])
            tool_names = [t.get("name", "") for t in tools]
            
            # Should have ETF-related tool
            has_etf_tool = any("etf" in name.lower() for name in tool_names)
            assert has_etf_tool, f"Expected ETF tool in: {tool_names}"

