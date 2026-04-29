-- =========================================
-- 3. INSERT DUMMY DATA
-- =========================================

-- Categories
INSERT INTO Categories VALUES (1, 'Fruits');

INSERT INTO Categories VALUES (2, 'Vegetables');

INSERT INTO Categories VALUES (3, 'Dairy');

-- Products
INSERT INTO
    Products
VALUES (
        101,
        'Apple',
        1,
        80,
        SYSDATE + 5,
        100
    );

INSERT INTO
    Products
VALUES (
        102,
        'Banana',
        1,
        30,
        SYSDATE + 2,
        50
    );

INSERT INTO
    Products
VALUES (
        103,
        'Carrot',
        2,
        100,
        SYSDATE + 10,
        40
    );

INSERT INTO Products VALUES ( 104, 'Milk', 3, 60, SYSDATE + 3, 60 );

INSERT INTO
    Products
VALUES (
        105,
        'Cheese',
        3,
        20,
        SYSDATE + 20,
        200
    );

-- Sales Transactions
INSERT INTO SalesTransactions VALUES (1, 101, 2, 200, SYSDATE - 10);

INSERT INTO SalesTransactions VALUES (2, 101, 1, 100, SYSDATE - 5);

INSERT INTO SalesTransactions VALUES (3, 104, 3, 180, SYSDATE - 20);

INSERT INTO SalesTransactions VALUES (4, 102, 5, 250, SYSDATE - 70);

COMMIT;