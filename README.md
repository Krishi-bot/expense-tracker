# 💰 Expense Tracker

A Python command-line application to log, categorise, and track personal expenses — with persistent storage so your data is saved between sessions.

---

## 🚀 Features

- Add expenses with an amount and category
- View all recorded expenses
- Show total amount spent
- Category summary (how much spent per category)
- Automatically saves to a CSV file and reloads on next run

---

## 🛠️ Tech Used

- Python 3
- `csv` and `os` modules (standard library — no installs needed)

---

## ▶️ How to Run

1. Clone the repository:
```
git clone https://github.com/Krishi-bot/expense-tracker.git
```

2. Navigate to the folder:
```
cd expense-tracker
```

3. Run the program:
```
python expense_tracker.py
```

---

## 💡 Example Usage

```
1. Add expense
2. View expenses
3. Show total
4. Category summary
5. Save and exit
Choose an option: 1
Enter amount: 200
Enter category: Food
Expense added.

Choose an option: 1
Enter amount: 500
Enter category: Travel
Expense added.

Choose an option: 4
Category Summary:
  Food: $200.00
  Travel: $500.00

Choose an option: 5
Expenses saved.
Goodbye!
```

Next time you run the program, your previous expenses load automatically.

---

## 📁 Data Storage

Expenses are saved to `expenses.csv` in the same folder. The file is created automatically on first save. You can open it in Excel or Google Sheets to view your data.

---

## 💡 What I Learned

This was my first independent Python project. A few things that were genuinely tricky:

- **Persistent storage** — the first version lost all data when the program closed. Adding CSV load/save taught me how to read and write files properly and think about state across sessions.
- **Debugging variable name errors** — I had a bug where I used `expense` instead of `expenses` in several places. Tracking it down taught me to read error messages carefully rather than just guessing.
- **Input handling** — deciding when to use `float()` vs `input()` and what happens when the user enters unexpected values.

If I were to extend this further I would add date tracking per expense, a monthly summary view, and input validation so the program doesn't crash on bad input.

---

## 👤 Author

Krishika Singh — [github.com/Krishi-bot](https://github.com/Krishi-bot)
