from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT patient_id, patient_name
FROM patients
LIMIT 10
""")

rows = cursor.fetchall()

print(rows)

conn.close()