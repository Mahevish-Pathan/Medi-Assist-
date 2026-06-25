from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT patient_id, patient_name
FROM patients
LIMIT 10;
""")

patients = cursor.fetchall()

print("\nPATIENTS:\n")

for p in patients:
    print(p)

conn.close()