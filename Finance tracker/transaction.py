from database import get_connection
from datetime import datetime

def add_transaction(description, category, amount):
    date = datetime.now().strftime("%Y-%m-%d")
    conn = get_connection()
    c = conn.cursor()
    c.execute("INSERT INTO transactions (date, description, category, amount) VALUES (?, ?, ?, ?)",
              (date, description, category, amount))
    conn.commit()
    conn.close()
    print("Transaction added successfully!")

def view_transactions():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM transactions")
    transactions = c.fetchall()
    conn.close()

    print("\nTransactions:")
    for trans in transactions:
        print(f"ID: {trans[0]}, Date: {trans[1]}, Description: {trans[2]}, Category: {trans[3]}, Amount: {trans[4]}")
