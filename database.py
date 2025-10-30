import sqlite3

DB_NAME = "calculator_history.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            num1 REAL,
            operator TEXT,
            num2 REAL,
            result REAL,
            error TEXT
        )
    """)
    conn.commit()
    conn.close()

def add_record(num1, operator, num2, result, error=None):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO history (num1, operator, num2, result, error) VALUES (?, ?, ?, ?, ?)",
        (num1, operator, num2, result, error)
    )
    conn.commit()
    conn.close()

def get_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT num1, operator, num2, result, error FROM history ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows

def clear_history():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM history")
    conn.commit()
    conn.close()
