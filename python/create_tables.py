import sqlite3

connection_obj = sqlite3.connect("finance.db")
cursor_obj = connection_obj.cursor()

cursor_obj.execute("PRAGMA foreign_keys = ON")

#CUSTOMERS
cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS customers (
  customer_id INTEGER PRIMARY KEY,
  age INTEGER,
  gender TEXT,
  yearly_income INTEGER,
  total_debt INTEGER
  )
""")

#ACCOUNTS
cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS accounts (
  account_id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  card_type TEXT,
  credit_limit INTEGER,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
""")

#TRANSACTIONS
cursor_obj.execute("""
CREATE TABLE IF NOT EXISTS transactions (
  transaction_id INTEGER PRIMARY KEY,
  customer_id INTEGER,
  account_id INTEGER,
  date TEXT,
  amount REAL,
  FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
  FOREIGN KEY (account_id) REFERENCES accounts(account_id)                 
)
""")

connection_obj.commit()
connection_obj.close()