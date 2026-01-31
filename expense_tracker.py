expenses =[]

def add_expense(amount, category):
   amount=float((input("Enter amount: ")))
   category=float((input("Enter category: ")))
   expense.append({"amount": amount, "category": category})
   print("Expense added")

def view_expense():
    if not expense:
        print("No expense recorded")
        return

    print("All expense: ")
    for expense in expenses:
        print(f"{expense['category']}: {expense['amount']}")
    print()


def show_total():
    total=0
    for expense in expenses:
        total += expense["amount"]
    print("Total spent:", total, "\n")

def category_summary():
    summary={}
    for expense in expenses:
        cate = expense["category"]
        summary[cate] = summary.get(cate, 0) + expense["amount"]

    print("Category Summary: ")
    for cate, amt in summary.items():
        print(f"{cate} : {amt}")
    print()

def main():
    while True:
        print("1. Add expense")
        print("2. View expense")
        print("3. Show total")
        print("4. Category summary")
        print("5. Exit")

        choice=input("Choose an option")

        if choice=="1":
            add_expense()
        elif choice=="2":
            view_expense()
        elif choice=="3":
            show_total()
        elif choice=="4":
            category_summary()
        elif choice=="5":
            print("Goodbye!")
            break
        else:
            print("Invalid option\n")

main()
