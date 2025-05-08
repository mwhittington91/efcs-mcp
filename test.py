# my_server.py
from fastmcp import FastMCP

mcp = FastMCP(name="MyServer", port=8050, host="0.0.0.0")


@mcp.tool()
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    # This runs the server, defaulting to STDIO transport
    mcp.run()

    # To use a different transport, e.g., Streamable HTTP:
    # mcp.run(transport="streamable-http", host="127.0.0.1", port=9000)
