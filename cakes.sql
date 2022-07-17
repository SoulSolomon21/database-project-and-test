--@block
CREATE DATABASE cakes;

--@block
CREATE TABLE customers(
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    email TEXT,
    rating INTEGER,
    amount INTEGER
    );

--@block
CREATE TABLE cakes(
    id INTEGER PRIMARY KEY AUTO INCREMENT,
    flavour TEXT,
    size TEXT,
    type TEXT
    );

--@block
CREATE TABLE payments(
    payment_id INTEGER PRIMARY KEY AUTO INCREMENT,
    payment_type TEXT 
    );

--@block
CREATE TABLE functions(
    function_id INTEGER PRIMARY KEY AUTO INCREMENT,
    function_type TEXT 
    );

--@block
CREATE TABLE receipts(
    c_id INTEGER,
    f_id INTEGER,
    t_id INTEGER,
    p_id INTEGER,
    FOREIGN KEY (c_id) REFERENCES customers(id),
    FOREIGN KEY (f_id) REFERENCES functions(function_id),
    FOREIGN KEY (p_id) REFERENCES payments(payment_id),
    FOREIGN KEY (t_id) REFERENCES cakes(id)
    );