from mcp.server.fastmcp import FastMCP
import uvicorn

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    # Get the ASGI app from FastMCP
    app = mcp.get_asgi_app(transport="streamable-http")
    # Run uvicorn with custom host/port
    uvicorn.run(app, host="0.0.0.0", port=8000)
