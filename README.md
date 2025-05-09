# ECFS MCP (Model Control Protocol)

A Python-based implementation of the Model Control Protocol (MCP) for the FCC's Electronic Comment Filing System (ECFS) API. This project provides a server and client implementation that allows for easy interaction with the ECFS API using FastMCP.

## Features

- FastMCP server implementation for ECFS API
- OpenAPI specification integration
- Environment-based configuration
- Docker support
- Python 3.13+ compatibility

## Prerequisites

- Python 3.13 or higher
- uv package manager
- Docker (optional)

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd efcs-mcp
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Unix/macOS
# or
.venv\Scripts\activate  # On Windows
```

3. Install dependencies using uv:
```bash
uv pip install -r requirements.txt
```

## Configuration

1. Create a `.env` file in the project root:
```bash
ECFS_API_KEY=your_api_key_here
```

## Usage

### Running the Server

```bash
python server.py
```

The server will start on `http://0.0.0.0:8000` with SSE transport enabled.

### Running the Client

```bash
python client.py
```

## Docker Support

Build and run using Docker:

```bash
docker build -t efcs-mcp .
docker run -p 8000:8000 efcs-mcp
```

## Project Structure

- `server.py` - Main server implementation
- `client.py` - Client implementation
- `ECFS-OPENAPI-Spec.yaml` - OpenAPI specification for ECFS
- `Dockerfile` - Docker configuration
- `requirements.txt` - Python dependencies
- `pyproject.toml` - Project metadata and configuration

## Dependencies

- fastmcp >= 2.2.10
- mcp[cli] >= 1.7.1
- python-dotenv >= 1.1.0
- pyyaml >= 6.0.2

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here]
