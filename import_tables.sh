#!/bin/bash
#
cd Tables
rm ../import_test.db
    sqlite3 ../import_test.db << EOF
create table if not exists  People(
PersonID INTEGER PRIMARY KEY AUTOINCREMENT,
FullName TEXT,
LogonName TEXT,
HashedPassword TEXT,
IsSystemUser INT,
IsEmployee INT,
IsSalesperson INT,
PhoneNumber TEXT,
EmailAddress TEXT
);

create table if not exists StockItems(
StockItemID INTEGER PRIMARY KEY AUTOINCREMENT,
StockItemName TEXT,
LeadTimeDays INT,
UnitPrice REAL,
RecommendedRetailPrice REAL
);

create table if not exists Customers(
CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
CustomerName TEXT,
PrimaryContactPersonID INTEGER REFERENCES People(PersonID) ON DELETE CASCADE,
PhoneNumber TEXT,
WebsiteURL TEXT,
DeliveryAddressLine1 TEXT,
DeliveryAddressLine2 TEXT
);


create table if not exists InvoiceLines(
InvoiceLineID INTEGER PRIMARY KEY AUTOINCREMENT,
InvoiceID INTEGER REFERENCES Invoices(InvoiceID) ON DELETE CASCADE,
StockItemID INTEGER REFERENCES StockItems(StockItemID) ON DELETE CASCADE,
Description TEXT,
Quantity INT,
UnitPrice REAL,
LineProfit REAL,
ExtendedPrice REAL
);

create table if not exists Invoices( 
InvoiceID INTEGER PRIMARY KEY AUTOINCREMENT,
CustomerID INTEGER REFERENCES Customers(CustomerID) ON DELETE CASCADE,
OrderID	INTEGER REFERENCES Orders(OrderID) ON DELETE CASCADE,
ContactPersonID INTEGER REFERENCES People(PersonID) ON DELETE CASCADE,
AccountsPersonID INTEGER REFERENCES People(PersonID) ON DELETE CASCADE,
InvoiceDate TEXT,
CustomerPurchaseOrderNumber INT,
DeliveryInstructions TEXT,
InternalComments TEXT,
DeliveryRun TEXT,
RunPosition INT,
ReturnedDeliveryData TEXT,
ConfirmedDeliveryTime TEXT,
ConfirmedReceivedBy TEXT);

create table if not exists CustomerTransactions(
CustomerTransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
CustomerID INTEGER REFERENCES Customers(CustomerID) ON DELETE CASCADE,
InvoiceID INTEGER REFERENCES Invoices(InvoiceID) ON DELETE CASCADE,
TransactionDate TEXT,
AmountExcludingTax REAL,
TaxAmount REAL,
TransactionAmount REAL,
OutstandingBalance REAL,
FinalizationDate TEXT,
IsFinalized INT
);

create table if not exists OrderLines(
OrderLineID INTEGER PRIMARY KEY AUTOINCREMENT,
OrderID INTEGER REFERENCES Orders(OrderID) ON DELETE CASCADE,
StockItemID INTEGER REFERENCES StockItems(StockItemID) ON DELETE CASCADE,
Description TEXT,
Quantity INT,
UnitPrice REAL,
PickedQuantity INT,
PickingCompletedWhen TEXT);

create table if not exists Orders(
OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
CustomerID INTEGER REFERENCES Customers(CustomerID) ON DELETE CASCADE,
OrderDate TEXT,
ExpectedDeliveryDate TEXT,
CustomerPurchaseOrderNumber INT,
IsUndersupplyBackordered INT,
PickingCompletedWhen TEXT
);

create table if not exists StockItemTransactions(
StockItemTransactionID INTEGER PRIMARY KEY AUTOINCREMENT,
StockItemID INTEGER REFERENCES StockItems(StockItemID) ON DELETE CASCADE,
CustomerID INTEGER REFERENCES Customers(CustomerID) ON DELETE CASCADE,
InvoiceID INTEGER REFERENCES Invoices(InvoiceID) ON DELETE CASCADE,
TransactionOccurredWhen TEXT,
Quantity INT
);

EOF
for FILE in *.csv; do 
    echo "Importing $FILE"
    sqlite3 ../import_test.db << EOF
.mode csv
.import --skip 1 $FILE ${FILE%.csv} 
EOF
done

