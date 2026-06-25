from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT COUNT(*)
FROM patients
""")

print(cursor.fetchone())

conn.close()