from cs50 import SQL

import csv

open("cakes.db", "w").close()

db = SQL("sqlite:///cakes.db")

db.execute("""CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email TEXT,
    rating INTEGER,
    amount INTEGER
    );""")

db.execute("""CREATE TABLE cakes(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    flavour TEXT,
    size TEXT,
    type TEXT
    );""")

db.execute("""CREATE TABLE payments(
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    payment_type TEXT
    );""")

db.execute("""CREATE TABLE functions(
    function_id INTEGER PRIMARY KEY AUTOINCREMENT,
    function_type TEXT
    );""")

db.execute("""CREATE TABLE receipts(
    c_id INTEGER,
    f_id INTEGER,
    t_id INTEGER,
    p_id INTEGER,
    FOREIGN KEY (c_id) REFERENCES customers(id),
    FOREIGN KEY (f_id) REFERENCES functions(function_id),
    FOREIGN KEY (p_id) REFERENCES payments(payment_id),
    FOREIGN KEY (t_id) REFERENCES cakes(id)
    );""")

with open("cake survey.csv", "r")as file:
    reader = csv.DictReader(file)
    
    for row in reader:
        emails = row["Email"]
        types = row["Type"]
        functions = row["Function"]
        amounts = row["Amount"]
        payment = row["Payment"]
        rating = row["Rating"]
        sizes = row["Size"]
        flavour = row["Flavour"]
        
        db.execute("""INSERT INTO customers(email,rating,amount) VALUES(?,?,?);""", emails,rating,amounts)
        db.execute("""INSERT INTO cakes(flavour,size,type) VALUES(?,?,?);""", flavour,sizes,types)
        db.execute("""INSERT INTO payments(payment_type) VALUES(?);""",payment)
        db.execute("""INSERT INTO functions(function_type) VALUES(?);""",functions)
 
        db.execute("""INSERT INTO receipts(c_id) VALUES((SELECT id FROM customers WHERE  email = ?));""", emails)
        db.execute("""INSERT INTO receipts(f_id) VALUES((SELECT function_id FROM functions WHERE function_type= DISTINCT(?)));""", functions)
        db.execute("""INSERT INTO receipts(t_id) VALUES((SELECT id FROM cakes WHERE  type = ?));""", types )
        db.execute("""INSERT INTO receipts(p_id) VALUES((SELECT payment_id FROM payments WHERE  payment_type = DISTINCT(?)));""", payment)
       