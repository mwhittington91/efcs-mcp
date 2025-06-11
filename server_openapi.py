import asyncio
import os

import httpx
import yaml
from dotenv import load_dotenv
from fastmcp import FastMCP
from fastmcp.server.openapi import RouteMap, RouteType


load_dotenv()

transport = "sse"

# Create a client for your API
api_client = httpx.AsyncClient(base_url="https://publicapi.fcc.gov/ecfs/")


# Load your OpenAPI spec

with open("ECFS-OPENAPI-Spec.yaml", "r") as f:
    spec = yaml.safe_load(f)



custom_maps = [
    # Force all endpoints to be Tools
    RouteMap(methods=["GET"], pattern="", route_type=RouteType.TOOL)
]


def get_api_key() -> str:
    """Get the API key from the environment variable"""
    return os.getenv("ECFS_API_KEY")


# Create an MCP server from your OpenAPI spec
mcp = FastMCP.from_openapi(
    openapi_spec=spec,
    client=api_client,
    name="ECFS",
    timeout=5.0,
    route_maps=custom_maps,
    host="0.0.0.0",
    port=8000,
    path="/sse",
)

mcp.add_tool(get_api_key)

async def check_mcp(mcp: FastMCP):
    # List what components were created
    tools = await mcp.get_tools()
    resources = await mcp.get_resources()
    templates = await mcp.get_resource_templates()

    print(f"{len(tools)} Tool(s): {', '.join([t.name for t in tools.values()])}")
    print(
        f"{len(resources)} Resource(s): {', '.join([r.name for r in resources.values()])}"
    )
    print(
        f"{len(templates)} Resource Template(s): {', '.join([t.name for t in templates.values()])}"
    )

    return mcp


if __name__ == "__main__":
    asyncio.run(check_mcp(mcp))
    mcp.run(transport=transport)
