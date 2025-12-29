import sqlite3
import csv

connection_obj = sqlite3.connect("finance.db")
cursor_obj = connection_obj.cursor()

cursor_obj.execute("PRAGMA foreign_keys = ON")

#CUSTOMERS
with open("raw_data/users_data.csv", newline="", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  for row in reader:
    cursor_obj.execute("""
      INSERT OR IGNORE INTO customers (customer_id, age, gender, yearly_income, total_debt)
      VALUES (?, ?, ?, ?, ?)
    """, (
      row["id"],
      row["current_age"],
      row["gender"],
      row["yearly_income"],
      row["total_debt"]
    ))

#ACCOUNTS
with open("raw_data/cards_data.csv", newline="", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  for row in reader:
    cursor_obj.execute("""
  INSERT OR IGNORE INTO accounts (account_id, customer_id, card_type, credit_limit) VALUES (?, ?, ?, ?)
""", (
  row["id"],
  row["client_id"],
  row["card_type"],
  row["credit_limit"]
))

#TRANSACTIONS
with open("raw_data/transactions_data.csv", newline="", encoding="utf-8") as file:
  reader = csv.DictReader(file)
  for row in reader:
    cursor_obj.execute("""
  INSERT OR IGNORE INTO transactions (transaction_id, customer_id, account_id, date, amount) VALUES (?, ?, ?, ?, ?)
""", (
  row["id"],
  row["client_id"],
  row["card_id"],
  row["date"],
  row["amount"]
))
    
connection_obj.commit()
connection_obj.close()
