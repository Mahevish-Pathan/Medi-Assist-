from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute(
    """
    SELECT table_name
    FROM information_schema.tables
    WHERE table_schema='public';
    """
)

tables = cursor.fetchall()

print("\nTables:\n")

for table in tables:
    print(table[0])

conn.close()