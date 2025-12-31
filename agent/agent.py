"""
ETF Agent - Google ADK Agent for Testing Tron MCP Integration

This agent connects to the Tron MCP server to discover and use
the ETF price lookup tool via the ADK web interface.
"""

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import SseConnectionParams
from google.genai import types

# Load environment variables
load_dotenv()


# Create MCP toolset to connect to Tron server using SSE
mcp_toolset = McpToolset(
    connection_params=SseConnectionParams(
        url="http://localhost:8000/mcp/sse",
    )
)

# Define the root agent (required for ADK web)
root_agent = Agent(
    name="etf_agent",
    model="gemini-2.5-flash",
    description="An agent that can look up ETF prices using the Tron API",
    instruction="""You are an ETF research assistant. You can look up current ETF prices
using the tools available to you. When a user asks about an ETF, use the appropriate
tool to fetch the price information.

Common ETF symbols include:
- SPY (S&P 500)
- QQQ (Nasdaq 100)
- VTI (Total Stock Market)
- VOO (Vanguard S&P 500)
""",
    tools=[mcp_toolset],
)
