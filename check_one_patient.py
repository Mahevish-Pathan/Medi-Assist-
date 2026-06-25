from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM patients
WHERE patient_id = 1
""")

print(cursor.fetchone())

conn.close()