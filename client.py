import asyncio
from fastmcp import FastMCP


async def main():
    # Create an MCP client that connects to your local server
    client = FastMCP(name="ECFS", host="localhost", port=8000, transport="sse")

    # Get available tools
    tools = await client.get_tools()
    print(f"Available tools: {', '.join([t.name for t in tools.values()])}")

    # Get available resources
    resources = await client.get_resources()
    print(f"Available resources: {', '.join([r.name for r in resources.values()])}")

    # Example of using a tool (replace with actual tool name from your API)
    # tool = tools["your_tool_name"]
    # result = await tool.execute(params={})
    # print(f"Tool result: {result}")


if __name__ == "__main__":
    asyncio.run(main())
