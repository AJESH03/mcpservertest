from mcp.server.fastmcp import FastMCP

mcp = FastMCP("server")

@mcp.tool()
def greeting(name: str) -> str:
    "Send a greeting"
    return f"Hi {name}"

if __name__ == "__main__":
    import uvicorn
    from mcp.server.streamable_http import create_app
    
    app = create_app(mcp)
    uvicorn.run(app, host="0.0.0.0", port=8000)
