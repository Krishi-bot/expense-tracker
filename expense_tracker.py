expenses =[]

def add_expense(amount, category):
    expense={
        "amount": amount,
        "category": category
    }
    expenses.append(expense)

def show_total():
    total=0
    for expense in expenses:
        total += expense["amount"]
    print("Total spent:", total)

while True:
    amount = float(input("Enter the expense amount(or 0 to stop): "))
    if amount == 0:
        break
    category = input("Enter Category: ")
    add_expense(amount, category)

show_total()

def category_summary():
    summary={}
    for expense in expenses:
        cate = expense["category"]
        summary[cate] = summary.get(cate, 0) + expense["amount"]

    print("Category Summary: ")
    for cate, amt in summary.items():
        print(cate, ":", amt)

category_summary()