import os
from fastapi import FastAPI
from mcp_python_sdk import MCPServer
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Initialize MCP Server
mcp_server = MCPServer()

@app.get("/")
async def root():
    return {"message": "MCP Server is running"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "server:app",
        host=os.getenv("MCP_SERVER_HOST", "0.0.0.0"),
        port=int(os.getenv("MCP_SERVER_PORT", 8000)),
        reload=True
    )