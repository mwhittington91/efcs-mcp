import asyncio

from fastmcp import Client
from fastmcp.client.transports import SSETransport

client = Client("server.py")
#client = Client(transport=SSETransport("http://0.0.0.0:8000/sse"))


async def main():
    # Connection is established here
    async with client:
        print(f"Client connected: {client.is_connected()}")
        print(client.transport)

        # Make MCP calls within the context
        tools = await client.list_tools()
        print(f"Available tools: {[tool.name for tool in tools]}")

        # if any(tool.name == "get_filings" for tool in tools):
        #     result = await client.call_tool("get_filings", {"q": "NCTA"})
        #     print(f"Greet result: {result}")

    # Connection is closed automatically here
    print(f"Client connected: {client.is_connected()}")


if __name__ == "__main__":
    asyncio.run(main())
