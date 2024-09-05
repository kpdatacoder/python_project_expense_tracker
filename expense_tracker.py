import json
import os
import datetime
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# File to store the data
DATA_FILE = 'daily_expense_data.json'

# Initialize data
data = {
    "income_log": [],
    "expense_log": [],
    "savings_log": []
}

# Load existing data from file (if available)
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as file:
            global data
            data = json.load(file)
    else:
        save_data()

# Save data to file
def save_data():
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

# Function to add income
def add_income(amount, description):
    if not amount:
        messagebox.showerror("Error", "Please enter an income amount.")
        return

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    data['income_log'].append({"date": date, "amount": float(amount), "description": description})
    save_data()
    messagebox.showinfo("Income Added", f"Income added: ₹{amount} ({description})")

# Function to add expense
def add_expense(amount, description):
    if not amount:
        messagebox.showerror("Error", "Please enter an expense amount.")
        return

    date = datetime.datetime.now().strftime("%Y-%m-%d")
    data['expense_log'].append({"date": date, "amount": float(amount), "description": description})
    save_data()
    messagebox.showinfo("Expense Added", f"Expense added: ₹{amount} ({description})")

# Function to calculate total savings
def calculate_savings():
    total_income = sum(item['amount'] for item in data['income_log'])
    total_expense = sum(item['amount'] for item in data['expense_log'])
    total_savings = total_income - total_expense
    data['savings_log'].append({"date": datetime.datetime.now().strftime("%Y-%m-%d"), "total_savings": total_savings})
    save_data()
    messagebox.showinfo("Total Savings", f"Your total savings are: ₹{total_savings}")

# Function to display logs
def display_logs():
    logs_window = tk.Toplevel()
    logs_window.title("Logs")
    logs_text = tk.Text(logs_window)
    logs_text.pack(expand=True, fill=tk.BOTH)

    logs_text.insert(tk.END, "---- Income Log ----\n")
    for entry in data['income_log']:
        logs_text.insert(tk.END, f"Date: {entry['date']}, Amount: ₹{entry['amount']}, Description: {entry['description']}\n")

    logs_text.insert(tk.END, "\n---- Expense Log ----\n")
    for entry in data['expense_log']:
        logs_text.insert(tk.END, f"Date: {entry['date']}, Amount: ₹{entry['amount']}, Description: {entry['description']}\n")

    logs_text.insert(tk.END, "\n---- Savings Log ----\n")
    for entry in data['savings_log']:
        logs_text.insert(tk.END, f"Date: {entry['date']}, Total Savings: ₹{entry['total_savings']}\n")

    logs_text.config(state=tk.DISABLED)

# GUI setup
def create_gui():
    root = tk.Tk()
    root.title("Expense and Savings Tracker")
    root.geometry("400x400")

    # Add a notebook widget to organize different sections
    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # Income tab
    income_tab = ttk.Frame(notebook)
    notebook.add(income_tab, text="Add Income")

    tk.Label(income_tab, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
    income_amount = tk.Entry(income_tab)
    income_amount.grid(row=0, column=1)

    tk.Label(income_tab, text="Description:").grid(row=1, column=0)
    income_description = tk.Entry(income_tab)
    income_description.grid(row=1, column=1)

    tk.Button(income_tab, text="Add Income", command=lambda: add_income(income_amount.get(), income_description.get())).grid(row=2, column=1)

    # Expense tab
    expense_tab = ttk.Frame(notebook)
    notebook.add(expense_tab, text="Add Expense")

    tk.Label(expense_tab, text="Amount:").grid(row=0, column=0, padx=10, pady=10)
    expense_amount = tk.Entry(expense_tab)
    expense_amount.grid(row=0, column=1)

    tk.Label(expense_tab, text="Description:").grid(row=1, column=0)
    expense_description = tk.Entry(expense_tab)
    expense_description.grid(row=1, column=1)

    tk.Button(expense_tab, text="Add Expense", command=lambda: add_expense(expense_amount.get(), expense_description.get())).grid(row=2, column=1)

    # Savings and Logs tab
    savings_logs_tab = ttk.Frame(notebook)
    notebook.add(savings_logs_tab, text="Savings & Logs")

    tk.Button(savings_logs_tab, text="Calculate Savings", command=calculate_savings).pack(pady=10)
    tk.Button(savings_logs_tab, text="Display Logs", command=display_logs).pack(pady=10)

    # Run the main loop
    root.mainloop()

# Load data and run GUI
load_data()
create_gui()
