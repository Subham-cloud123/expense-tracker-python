import pandas as pd
import matplotlib.pyplot as plt
import os
import datetime

DATA_FILE = "expenses.csv"

def load_data():
    if os.path.exists(DATA_FILE):
        return pd.read_csv(DATA_FILE)
    return pd.DataFrame(columns=["Date", "Amount", "Category", "Note"])

def save_data(df):
    df.to_csv(DATA_FILE, index=False)

def add_expense():
    date = input("Enter date (YYYY-MM-DD) or leave blank for today: ")
    if not date:
        date = datetime.date.today().isoformat()
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food/Travel/Shopping/Others): ")
    note = input("Enter note: ")

    df = load_data()
    df = df.append({"Date": date, "Amount": amount, "Category": category, "Note": note}, ignore_index=True)
    save_data(df)
    print("Expense added successfully!")

def view_expenses():
    df = load_data()
    print(df)

def visualize_spending():
    df = load_data()
    if df.empty:
        print("No data to visualize.")
        return
    grouped = df.groupby("Category")["Amount"].sum()
    plt.figure(figsize=(6,6))
    plt.pie(grouped, labels=grouped.index, autopct="%1.1f%%")
    plt.title("Spending Distribution")
    plt.show()

def main():
    while True:
        print("\n--- Personal Finance Tracker ---")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Visualize Spending")
        print("4. Exit")
        choice = input("Enter choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            visualize_spending()
        elif choice == "4":
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
