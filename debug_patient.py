from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT patient_id, patient_name
FROM patients
LIMIT 20
""")

rows = cursor.fetchall()

print("Total rows:", len(rows))

for row in rows:
    print(row)

conn.close()