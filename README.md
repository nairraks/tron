# Tron

A Blazingly fast API for the new age - A Python FastAPI service with MCP (Model Context Protocol) support.

## Features

- 🚀 Built with FastAPI and Python 3.12+
- 🤖 MCP (Model Context Protocol) endpoint for AI agent integration
- ⚡ High-performance async HTTP endpoints
- 📈 Real-time ETF price lookup using yfinance
- 📖 Auto-generated OpenAPI documentation
- 🧪 Comprehensive pytest test suite

## Requirements

- Python 3.12 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Service

### Using Python module:
```bash
python -m src.main
```

### Using Uvicorn:
```bash
uvicorn src.main:app --host 0.0.0.0 --port 8000
```

The service will start on `http://localhost:8000`

## API Endpoints

### HTTP Endpoints

- **GET /** - Hello World endpoint
  ```bash
  curl http://localhost:8000/
  ```
  Response:
  ```json
  {
    "message": "Hello, World!",
    "service": "Tron",
    "description": "A Blazingly fast API for the new age"
  }
  ```

- **GET /health** - Health check endpoint
  ```bash
  curl http://localhost:8000/health
  ```
  Response:
  ```json
  {
    "status": "healthy"
  }
  ```

- **GET /etf/{symbol}** - Get ETF price
  ```bash
  curl http://localhost:8000/etf/SPY
  ```
  Response:
  ```json
  {
    "symbol": "SPY",
    "name": "SPDR S&P 500 ETF Trust",
    "price": 478.50,
    "currency": "USD",
    "timestamp": "2024-12-30T07:44:00Z"
  }
  ```

- **GET /docs** - Interactive API documentation (Swagger UI)
- **GET /redoc** - Alternative API documentation (ReDoc)

### MCP Endpoint

The MCP endpoint is available at `/mcp` and provides AI agents access to all API endpoints through the Model Context Protocol.

**Initialize MCP Session:**
```bash
curl -X POST http://localhost:8000/mcp \
  -H "Content-Type: application/json" \
  -H "Accept: application/json" \
  -d '{
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
  }'
```

## Testing

### Run Tests
```bash
python -m pytest tests/ -v
```

### Test with ADK Agent
The `agent/` folder contains a Google ADK agent for testing MCP integration:
```bash
python agent/etf_agent.py
```

## Project Structure

```
tron/
├── src/                 # Source code
│   ├── __init__.py
│   ├── main.py          # Main FastAPI application
│   └── etf/             # ETF module
│       ├── __init__.py
│       ├── models.py    # Pydantic models
│       └── router.py    # API routes
├── agent/               # Google ADK agent for MCP testing
│   ├── __init__.py
│   └── etf_agent.py     # ADK agent that connects to Tron MCP
├── tests/               # Pytest test suite
│   ├── __init__.py
│   ├── test_etf_api.py  # ETF API endpoint tests
│   └── test_mcp.py      # MCP integration tests
├── requirements.txt     # Python dependencies
├── pyproject.toml       # Project metadata and build configuration
└── README.md            # This file
```

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [fastapi-mcp](https://github.com/tadata-org/fastapi-mcp) - MCP integration for FastAPI
- [yfinance](https://github.com/ranaroussi/yfinance) - Yahoo Finance market data
- [Google ADK](https://github.com/google/adk-python) - Agent Development Kit for AI agents
- [Uvicorn](https://www.uvicorn.org/) - ASGI web server implementation

## License

See repository license.
