"""
Tron - A Blazingly fast API for the new age

This FastAPI application includes:
- A hello world HTTP endpoint
- An MCP (Model Context Protocol) endpoint for AI agent integration
- Modular router system for feature-specific endpoints
"""

from fastapi import FastAPI

from src.etf.router import router as etf_router


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


# Include feature routers
app.include_router(etf_router)


def setup_mcp():
    """Setup MCP server. Called at runtime, not import time."""
    from fastapi_mcp import FastApiMCP
    
    mcp = FastApiMCP(
        fastapi=app,
        name="Tron MCP Server",
        description="MCP server for Tron API - providing AI agents access to the Tron API endpoints"
    )
    mcp.mount_http(mount_path="/mcp")
    mcp.mount_sse(mount_path="/mcp/sse")
    return mcp


if __name__ == "__main__":
    import uvicorn
    
    # Setup MCP when running as main
    setup_mcp()
    
    uvicorn.run(app, host="0.0.0.0", port=8000)
