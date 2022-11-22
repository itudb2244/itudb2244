#!/bin/bash
#
cd Tables
rm ../import_test.db
    sqlite3 ../import_test.db << EOF
create table People(
PersonID INTEGER PRIMARY KEY,
FullName TEXT,
LogonName TEXT,
HashedPassword TEXT,
IsSystemUser INTEGER,
IsEmployee INTEGER,
IsSalesperson INTEGER,
PhoneNumber TEXT,
EmailAddress TEXT);

create table StockItems(
StockItemID INTEGER PRIMARY KEY,
StockItemName TEXT,
LeadTimeDays INTEGER,
UnitPrice REAL,
RecommendedRetailPrice REAL
);

create table Customers(
CustomerID INTEGER PRIMARY KEY,
CustomerName TEXT,
PrimaryContactPersonID INTEGER REFERENCES People(PersonID),
PhoneNumber INTEGER,
WebsiteURL TEXT,
DeliveryAddressLine1 TEXT,
DeliveryAddressLine2 TEXT);


create table InvoiceLines(
InvoiceLineID INTEGER PRIMARY KEY,
InvoiceID INTEGER REFERENCES Invoices(InvoiceID),
StockItemID INTEGER REFERENCES StockItems(StockItemID),
Description TEXT,
Quantity INTEGER,
UnitPrice REAL,
LineProfit REAL,
ExtendedPrice REAL
);

create table Invoices( 
InvoiceID INTEGER PRIMARY KEY,
CustomerID INTEGER REFERENCES Customers(CustomerID),
OrderID	INTEGER REFERENCES Orders(OrderID),
ContactPersonID INTEGER REFERENCES People(PersonID),
AccountsPersonID INTEGER REFERENCES People(PersonID),
InvoiceDate TEXT,
CustomerPurchaseOrderNumber INTEGER,
DeliveryInstructions TEXT,
InternalComments TEXT,
DeliveryRun TEXT,
RunPosition INTEGER,
ReturnedDeliveryData TEXT,
ConfirmedDeliveryTime TEXT,
ConfirmedReceivedBy TEXT);

create table CustomerTransactions(
CustomerTransactionID INTEGER PRIMARY KEY,
CustomerID INTEGER REFERENCES Customers(CustomerID),
InvoiceID INTEGER REFERENCES Invoices(InvoiceID),
TransactionDate TEXT,
AmountExcludingTax REAL,
TaxAmount REAL,
TransactionAmount REAL,
OutstandingBalance REAL,
FinalizationDate TEXT,
IsFinalized INTEGER
);

create table OrderLines(
OrderLineID INTEGER PRIMARY KEY,
OrderID INTEGER REFERENCES Orders(OrderID),
StockItemID INTEGER REFERENCES StockItems(StockItemID),
Description TEXT,
Quantity INTEGER,
UnitPrice REAL,
PickedQuantity INTEGER,
PickingCompletedWhen TEXT);

create table Orders(
OrderID INTEGER PRIMARY KEY,
CustomerID INTEGER REFERENCES Customers(CustomerID),
OrderDate TEXT,
ExpectedDeliveryDate TEXT,
CustomerPurchaseOrderNumber INTEGER,
IsUndersupplyBackordered INTEGER,
PickingCompletedWhen TEXT
);


create table StockItemHoldings(
StockItemID INTEGER REFERENCES StockItems(StockItemID),
QuantityOnHand INTEGER,
BinLocation TEXT, 
LastStocktakeQuantity INTEGER,
LastCostPrice REAL,
ReorderLevel INTEGER,
TargetStockLevel INTEGER);


create table StockItemTransactions(
StockItemTransactionID INTEGER,
StockItemID INTEGER REFERENCES StockItems(StockItemID),
CustomerID INTEGER REFERENCES Customers(CustomerID),
InvoiceID INTEGER REFERENCES Invoices(InvoiceID),
TransactionOccurredWhen TEXT,
Quantity INTEGER
);

EOF
for FILE in *.csv; do 
    echo "Importing $FILE"
    sqlite3 ../import_test.db << EOF
.mode csv
.import $FILE  ${FILE%.csv} 
EOF
done

