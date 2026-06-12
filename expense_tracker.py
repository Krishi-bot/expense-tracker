import csv
import os

FILENAME = "expenses.csv"
expenses = []

def load_expenses():
    """Load expenses from CSV file on startup."""
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                expenses.append({"amount": float(row["amount"]), "category": row["category"]})
        print(f"Loaded {len(expenses)} expense(s) from {FILENAME}\n")

def save_expenses():
    """Save all expenses to CSV file."""
    with open(FILENAME, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["amount", "category"])
        writer.writeheader()
        writer.writerows(expenses)
    print("Expenses saved.\n")

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category: ")
    expenses.append({"amount": amount, "category": category})
    print("Expense added.\n")

def view_expenses():
    if not expenses:
        print("No expenses recorded.\n")
        return
    print("All expenses:")
    for e in expenses:
        print(f"  {e['category']}: ${e['amount']:.2f}")
    print()

def show_total():
    total = sum(e["amount"] for e in expenses)
    print(f"Total spent: ${total:.2f}\n")

def category_summary():
    if not expenses:
        print("No expenses recorded.\n")
        return
    summary = {}
    for e in expenses:
        summary[e["category"]] = summary.get(e["category"], 0) + e["amount"]
    print("Category Summary:")
    for category, total in summary.items():
        print(f"  {category}: ${total:.2f}")
    print()

def main():
    load_expenses()
    while True:
        print("1. Add expense")
        print("2. View expenses")
        print("3. Show total")
        print("4. Category summary")
        print("5. Save and exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            show_total()
        elif choice == "4":
            category_summary()
        elif choice == "5":
            save_expenses()
            print("Goodbye!")
            break
        else:
            print("Invalid option.\n")

main()
