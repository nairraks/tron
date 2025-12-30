# Tron

A Blazingly fast API for the new age - A Python FastAPI service with MCP (Model Context Protocol) support.

## Features

- 🚀 Built with FastAPI and Python 3.12+
- 🤖 MCP (Model Context Protocol) endpoint for AI agent integration
- ⚡ High-performance async HTTP endpoints
- 📖 Auto-generated OpenAPI documentation

## Requirements

- Python 3.12 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Service

### Using Python directly:
```bash
python main.py
```

### Using Uvicorn:
```bash
uvicorn main:app --host 0.0.0.0 --port 8000
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

## Project Structure

```
tron/
├── main.py              # Main FastAPI application
├── requirements.txt     # Python dependencies
├── pyproject.toml      # Project metadata and build configuration
└── README.md           # This file
```

## Technologies

- [FastAPI](https://fastapi.tiangolo.com/) - Modern, fast web framework for building APIs
- [fastapi-mcp](https://github.com/tadata-org/fastapi-mcp) - MCP integration for FastAPI
- [Uvicorn](https://www.uvicorn.org/) - ASGI web server implementation

## License

See repository license.
