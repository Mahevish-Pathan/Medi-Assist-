from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

cursor.execute("""
SELECT column_name
FROM information_schema.columns
WHERE table_name = 'patients';
""")

columns = cursor.fetchall()

print("\nPATIENTS TABLE COLUMNS:\n")

for col in columns:
    print(col[0])

conn.close()