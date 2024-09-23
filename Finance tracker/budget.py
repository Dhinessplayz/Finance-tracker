from database import get_connection

def set_budget(category, amount):
    conn = get_connection()
    c = conn.cursor()
    c.execute("REPLACE INTO budgets (category, amount) VALUES (?, ?)", (category, amount))
    conn.commit()
    conn.close()
    print(f"Budget set for {category}: {amount}")

def view_budget():
    conn = get_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM budgets")
    budgets = c.fetchall()
    conn.close()

    print("\nBudgets:")
    for budget in budgets:
        print(f"Category: {budget[1]}, Amount: {budget[2]}")
