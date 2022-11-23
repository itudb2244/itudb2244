import sqlite3

con = sqlite3.connect("test.db")

init_statements = {

    'create_customers_table' : """CREATE TABLE IF NOT EXISTS CUSTOMERS(
        customerID INTEGER PRIMARY KEY,
        customerName VARCHAR(50),
        primaryContactPersonID INTEGER REFERENCES PEOPLE,
        phoneNumber INTEGER,
        websiteURL VARCHAR(100),
        deliveryAddressLine1 VARCHAR(10),
        deliveryAddressLine2 VARCHAR(50)
    )""",
    'create_invoices_table' : """CREATE TABLE IF NOT EXISTS INVOICES(
        invoiceID INTEGER PRIMARY KEY,
        customerID INTEGER REFERENCES CUSTOMERS,
        orderID	INTEGER REFERENCES ORDERS,
        contactPersonID INTEGER REFERENCES PEOPLE,
        accountsPersonID INTEGER REFERENCES PEOPLE,
        invoiceDate DATE,
        customerPurchaseOrderNumber INTEGER,
        deliveryInstructions VARCHAR(50),
        internalComments VARCHAR(200),
        deliveryRun VARCHAR(200),
        runPosition INTEGER,
        returnedDeliveryData VARCHAR(200),
        confirmedDeliveryTime VARCHAR(200),
        confirmedReceivedBy VARCHAR(200)
    )""",
    'create_orders_table' : """CREATE TABLE IF NOT EXISTS ORDERS(
        orderID INTEGER PRIMARY KEY,
        customerID INTEGER REFERENCES CUSTOMERS,
        orderDate DATE,
        expectedDeliveryDate DATE,
        customerPurchaseOrderNumber INTEGER,
        isUndersupplyBackordered INTEGER,
        pickingCompletedWhen VARCHAR(25)
    )""",
    'create_invoiceLines_table' : """CREATE TABLE IF NOT EXISTS INVOICE_LINES(
        invoiceLineID INTEGER PRIMARY KEY,
        invoiceID INTEGER REFERENCES ınvoıces,
        stockItemID INTEGER REFERENCES STOCK_ITEMS,
        description VARCHAR(100),
        quantity INTEGER,
        unitPrice DECIMAL(10,2),
        lineProfit DECIMAL(10,2),
        extendedPrice DECIMAL(10,2)
    )""",
    'create_orderLines_table' : """CREATE TABLE IF NOT EXISTS ORDER_LINES(
        orderLineID INTEGER PRIMARY KEY,
        orderID INTEGER REFERENCES ORDERS,
        stockItemID INTEGER REFERENCES StockItems(StockItemID),
        description VARCHAR(100),
        quantity INTEGER,
        unitPrice DECIMAL(10,2),
        pickedQuantity INTEGER,
        pickingCompletedWhen VARCHAR(50)
    )""",
    'create_customerTransaction_table' : """CREATE TABLE IF NOT EXISTS CUSTOMER_TRANSACTIONS(
        customerTransactionID INTEGER PRIMARY KEY,
        customerID INTEGER REFERENCES CUSTOMERS,
        invoiceID INTEGER REFERENCES INVOICES,
        transactionDate DATE,
        amountExcludingTax DECIMAL(10,2),
        taxAmount DECIMAL(10,2),
        transactionAmount DECIMAL(10,2),
        outstandingBalance DECIMAL(10,2),
        finalizationDate DATE,
        isFinalized INTEGER
    )""",
    'create_people_table' : """CREATE TABLE IF NOT EXISTS PEOPLE(
        personID INTEGER PRIMARY KEY,
        fullName VARCHAR(50),
        logonName VARCHAR(50),
        hashedPassword VARCHAR(100),
        isSystemUser INTEGER,
        isEmployee INTEGER,
        isSalesperson INTEGER,
        phoneNumber VARCHAR(20),
        emailAddress VARCHAR(20)
    )""",
    'create_stockItem_table' : """CREATE TABLE IF NOT EXISTS STOCK_ITEMS(
        stockItemID INTEGER PRIMARY KEY,
        stockItemName VARCHAR(100),
        leadTimeDays INTEGER,
        unitPrice DECIMAL(10, 2),
        recommendedRetailPrice DECIMAL(10, 2)
    )""",
    'create_stockItemHoldings_table' : """CREATE TABLE IF NOT EXISTS STOCK_ITEM_HOLDINGS(
        stockItemID INTEGER REFERENCES StockItems(StockItemID),
        quantityOnHand INTEGER,
        binLocation VARCHAR(5), 
        lastStocktakeQuantity INTEGER,
        lastCostPrice DECIMAL(10, 2),
        reorderLevel INTEGER,
        targetStockLevel INTEGER
    )""",
    'create_stockItemTransaction_table' : """CREATE TABLE IF NOT EXISTS STOCK_ITEM_TRANSACTIONS(
        stockItemTransactionID INTEGER,
        stockItemID INTEGER REFERENCES STOCK_ITEMS,
        customerID INTEGER REFERENCES CUSTOMERS,
        invoiceID INTEGER REFERENCES INVOICES,
        transactionOccurredWhen VARCHAR(50),
        quantity INTEGER
    )""",
}