from app.backend.mcp_router import handle_mcp_query

result = handle_mcp_query(
    "patient history 1"
)

print(result)