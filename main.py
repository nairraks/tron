"""
Tron - A Blazingly fast API for the new age

This FastAPI application includes:
- A hello world HTTP endpoint
- An MCP (Model Context Protocol) endpoint for AI agent integration
"""

from fastapi import FastAPI
from fastapi_mcp import FastApiMCP

# Create FastAPI application
app = FastAPI(
    title="Tron",
    description="A Blazingly fast API for the new age",
    version="0.1.0",
)


@app.get("/")
async def hello_world():
    """
    Hello World HTTP endpoint
    
    Returns a simple greeting message.
    """
    return {
        "message": "Hello, World!",
        "service": "Tron",
        "description": "A Blazingly fast API for the new age"
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint
    
    Returns the service status.
    """
    return {"status": "healthy"}


# Create MCP server from the FastAPI app
mcp = FastApiMCP(
    fastapi=app,
    name="Tron MCP Server",
    description="MCP server for Tron API - providing AI agents access to the Tron API endpoints"
)

# Mount the MCP server with HTTP transport (recommended)
mcp.mount_http(mount_path="/mcp")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
