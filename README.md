# MCP DigitalOcean Server

A Model Context Protocol implementation that integrates with DigitalOcean for server management.

## Setup

1. Clone this repository
2. Copy `.env.example` to `.env` and fill in your DigitalOcean API token
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the server:
   ```bash
   python src/server.py
   ```

## Features

- MCP Protocol implementation
- DigitalOcean integration for server management
- FastAPI-based HTTP server

## Configuration

Configure the following environment variables in your `.env` file:

- `DIGITALOCEAN_TOKEN`: Your DigitalOcean API token
- `MCP_SERVER_PORT`: Port for the MCP server (default: 8000)
- `MCP_SERVER_HOST`: Host for the MCP server (default: 0.0.0.0)