from openai import OpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
# Set the OpenAI API key
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

def chat_mcp(input_text: str, show_tool_calls: bool) -> str:
    resp = client.responses.create(
        model="gpt-4.1",
        tools=[
            {
                "type": "mcp",
                "server_label": "ecfs",
                "server_url": "https://ecfs-mcp-server.azurewebsites.net/sse",
                "require_approval": "never",
            },
        ],
        tool_choice = "required",
        input=input_text,
    )

    tool_calls = [json.dumps(tool_call, indent=2) for tool_call in resp.to_dict()["output"][1:] if tool_call["type"] == "mcp_call"]

    if show_tool_calls:
        print("Tools called:")
        for tool_call in tool_calls:
            print(tool_call)
            print("===")

    return resp.output_text

if __name__ == "__main__":
    print(chat_mcp("Give me the 5 latest filing on spectrum", show_tool_calls=True))
