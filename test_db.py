from app.mcp.database import get_connection

print("Imported database module successfully")

try:
    conn = get_connection()
    print("Database Connected Successfully")
    conn.close()

except Exception as e:
    print("ERROR:")
    print(e)