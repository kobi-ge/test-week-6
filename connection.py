import sqlite3

db_connection = "C:\projects\data-course\tests\test-week-6\csv_file\hayal_300_no_status.csv"

def get_connection():
    conn = sqlite3.connect(db_connection)
    conn.execute("PRAGMA foreign_keys = ON")
    return conn

get_connection()