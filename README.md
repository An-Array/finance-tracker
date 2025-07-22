# 💰 Personal Finance Tracker (Python + SQLite)

A clean and simple terminal-based finance tracker that helps you record, view, and analyze your personal income and expenses.

---

## ⚙️ Tech Stack

- 🐍 Python
- 🗃️ SQLite3
- 📊 Pandas

---

## 🚀 Features

- Add income/expense transactions via terminal
- View all transactions with filters
- Import from CSV
- Summarize totals by category and type

---

## 📂 Project Structure

```bash
finance-tracker/
├── app/
│   ├── add_transaction.py          # Add a transaction
│   ├── file_to_db.py               # Add CSV transactions to database
│   ├── view_summary.py             # View and summarize
│   └── visualize.py                # Visualization of income and expenditure
├── data/
│   ├── finance.db
│   └── sample_data.csv
├── create_db.py
└── README.md

---

## 🧪 How to Run

```bash
# 1. Clone repo
git clone https://github.com/yourusername/finance-tracker.git
cd finance-tracker

# 2. Set up environment (optional)
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows (use commandprompt)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run a script
python scripts/add_transaction.py
