from app.mcp.database import get_connection

conn = get_connection()

cursor = conn.cursor()

tables = [
    "patients",
    "lab_results",
    "billing",
    "appointments",
    "doctors"
]

for table in tables:

    try:

        cursor.execute(
            f"SELECT COUNT(*) FROM {table}"
        )

        count = cursor.fetchone()[0]

        print(table, ":", count)

    except Exception as e:

        print(table, "ERROR", e)

conn.close()