import asyncio
import os

import httpx
from dotenv import load_dotenv
from fastmcp import FastMCP

load_dotenv()

transport = "sse"

# Create a client for your API
api_client = httpx.AsyncClient(base_url="https://publicapi.fcc.gov/ecfs/")

def get_api_key() -> str:
    """Get the API key from the environment variable"""
    return os.getenv("ECFS_API_KEY")


async def search(
    q: str = None,
    date_submission: str = None,
    date_received: str = None,
    date_disseminated: str = None,
    date_comment_period: str = None,
    date_reply_comment: str = None,
    sort: str = None,
    limit: int = None,
    offset: int = None,
):
    """
    Search for FCC filings using the /filings endpoint.
    All parameters are optional except the API key (from env).
    """
    params = {"api_key": get_api_key()}
    if q is not None:
        params["q"] = q
    # if date_submission is not None:
    #     params["date_submission"] = date_submission
    # if date_received is not None:
    #     params["date_received"] = date_received
    # if date_disseminated is not None:
    #     params["date_disseminated"] = date_disseminated
    # if date_comment_period is not None:
    #     params["date_comment_period"] = date_comment_period
    # if date_reply_comment is not None:
    #     params["date_reply_comment"] = date_reply_comment
    # if sort is not None:
    #     params["sort"] = sort
    if limit is not None:
        params["limit"] = limit
    # if offset is not None:
    #     params["offset"] = offset
    resp = await api_client.get("/filings", params=params)
    resp.raise_for_status()
    return resp.json()


async def fetch(id_submission: str):
    """
    Fetch a single FCC filing by Submission ID using the /filing/{id_submission} endpoint.
    """
    params = {"api_key": get_api_key()}
    url = f"/filing/{id_submission}"
    resp = await api_client.get(url, params=params)
    resp.raise_for_status()
    return resp.json()

mcp = FastMCP(
    name="ECFS",
    instructions="You are a helpful assistant that can search and fetch FCC filings.",
)

mcp.add_tool(get_api_key)
mcp.add_tool(search)
mcp.add_tool(fetch)


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
