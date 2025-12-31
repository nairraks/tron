"""
ETF Agent - Google ADK Agent for Testing Tron MCP Integration

This agent connects to the Tron MCP server to discover and use
the ETF price lookup tool.
"""

import asyncio
from google import genai
from google.adk.tools.mcp_tool import McpToolset


async def main():
    """Main function to run the ETF agent."""
    
    print("=" * 60)
    print("ETF Agent - Testing Tron MCP Integration")
    print("=" * 60)
    
    # Connect to Tron MCP server
    mcp_url = "http://localhost:8000/mcp"
    print(f"\nConnecting to Tron MCP server at {mcp_url}...")
    
    try:
        # Create MCP toolset connection
        toolset = McpToolset(
            connection_params={
                "url": mcp_url,
            }
        )
        
        # Discover available tools
        print("\nDiscovering available tools...")
        tools = await toolset.get_tools()
        
        print(f"\nFound {len(tools)} tools:")
        for tool in tools:
            print(f"  - {tool.name}: {tool.description}")
        
        # Look for the ETF price tool
        etf_tool = None
        for tool in tools:
            if "etf" in tool.name.lower() or "price" in tool.name.lower():
                etf_tool = tool
                break
        
        if etf_tool:
            print(f"\nFound ETF tool: {etf_tool.name}")
            
            # Test with some ETF symbols
            test_symbols = ["SPY", "QQQ", "VTI"]
            
            for symbol in test_symbols:
                print(f"\nFetching price for {symbol}...")
                try:
                    result = await etf_tool.call(symbol=symbol)
                    print(f"  Result: {result}")
                except Exception as e:
                    print(f"  Error: {e}")
        else:
            print("\nNo ETF-related tool found. Available tools:")
            for tool in tools:
                print(f"  - {tool.name}")
        
        print("\n" + "=" * 60)
        print("Agent test completed!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\nError connecting to MCP server: {e}")
        print("\nMake sure the Tron server is running:")
        print("  cd c:\\Users\\rakes\\dev\\tron")
        print("  python -m src.main")


if __name__ == "__main__":
    asyncio.run(main())
