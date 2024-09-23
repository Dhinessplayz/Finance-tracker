import tkinter as tk
from transaction import add_transaction

def submit_transaction():
    desc = entry_desc.get()
    cat = entry_cat.get()
    amt = float(entry_amt.get())
    add_transaction(desc, cat, amt)

# Initialize the GUI window
root = tk.Tk()
root.title("Finance Manager")

# Create GUI components
tk.Label(root, text="Description").grid(row=0)
tk.Label(root, text="Category").grid(row=1)
tk.Label(root, text="Amount").grid(row=2)

entry_desc = tk.Entry(root)
entry_cat = tk.Entry(root)
entry_amt = tk.Entry(root)

entry_desc.grid(row=0, column=1)
entry_cat.grid(row=1, column=1)
entry_amt.grid(row=2, column=1)

# Submit button to add a transaction
tk.Button(root, text="Add Transaction", command=submit_transaction).grid(row=3, column=1)

root.mainloop()
