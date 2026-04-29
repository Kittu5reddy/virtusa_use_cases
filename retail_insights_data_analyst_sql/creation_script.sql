-- =========================================
-- 1. DROP TABLES (ignore errors if not exist)
-- =========================================
CREATE USER kaushik IDENTIFIED BY virtusa;

GRANT ALL PRIVILEGES TO kaushik;

DROP TABLE SalesTransactions;

DROP TABLE Products;

DROP TABLE Categories;

-- =========================================
-- 2. SCHEMA DESIGN
-- =========================================

CREATE TABLE Categories (
    category_id NUMBER PRIMARY KEY,
    category_name VARCHAR2 (100) NOT NULL
);

CREATE TABLE Products (
    product_id NUMBER PRIMARY KEY,
    product_name VARCHAR2 (100) NOT NULL,
    category_id NUMBER,
    stock_count NUMBER,
    expiry_date DATE,
    price NUMBER,
    FOREIGN KEY (category_id) REFERENCES Categories (category_id)
);

CREATE TABLE SalesTransactions (
    transaction_id NUMBER PRIMARY KEY,
    product_id NUMBER,
    quantity NUMBER,
    amount NUMBER,
    sale_date DATE,
    FOREIGN KEY (product_id) REFERENCES Products (product_id)
);