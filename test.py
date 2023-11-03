from cs50 import SQL

db = SQL("sqlite:///st.db")

roster = input("State: ")

rows = db.execute("SELECT * FROM roaster WHERE State Code = 'BDS'")

for row in rows:
    print(row["State"])

