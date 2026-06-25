from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT DISTINCT patient_id
FROM lab_results
LIMIT 20
""")

rows = cursor.fetchall()

print(rows)

conn.close()