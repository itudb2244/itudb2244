#!/bin/bash
#
cd Tables
rm ../import_test.db
    sqlite3 ../import_test.db << EOF
create table if not exists  People(
PersonID INT PRIMARY KEY,
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
StockItemID INT PRIMARY KEY,
StockItemName TEXT,
LeadTimeDays INT,
UnitPrice REAL,
RecommendedRetailPrice REAL
);

create table if not exists Customers(
CustomerID INT PRIMARY KEY,
CustomerName TEXT,
PrimaryContactPersonID INT REFERENCES People(PersonID) ON DELETE CASCADE,
PhoneNumber TEXT,
WebsiteURL TEXT,
DeliveryAddressLine1 TEXT,
DeliveryAddressLine2 TEXT
);


create table if not exists InvoiceLines(
InvoiceLineID INT PRIMARY KEY,
InvoiceID INT REFERENCES Invoices(InvoiceID) ON DELETE CASCADE,
StockItemID INT REFERENCES StockItems(StockItemID) ON DELETE CASCADE,
Description TEXT,
Quantity INT,
UnitPrice REAL,
LineProfit REAL,
ExtendedPrice REAL
);

create table if not exists Invoices( 
InvoiceID INT PRIMARY KEY,
CustomerID INT REFERENCES Customers(CustomerID) ON DELETE CASCADE,
OrderID	INT REFERENCES Orders(OrderID) ON DELETE CASCADE,
ContactPersonID INT REFERENCES People(PersonID) ON DELETE CASCADE,
AccountsPersonID INT REFERENCES People(PersonID) ON DELETE CASCADE,
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
CustomerTransactionID INT PRIMARY KEY,
CustomerID INT REFERENCES Customers(CustomerID) ON DELETE CASCADE,
InvoiceID INT REFERENCES Invoices(InvoiceID) NULL ON DELETE CASCADE,
TransactionDate TEXT,
AmountExcludingTax REAL,
TaxAmount REAL,
TransactionAmount REAL,
OutstandingBalance REAL,
FinalizationDate TEXT,
IsFinalized INT
);

create table if not exists OrderLines(
OrderLineID INT PRIMARY KEY,
OrderID INT REFERENCES Orders(OrderID) ON DELETE CASCADE,
StockItemID INT REFERENCES StockItems(StockItemID) ON DELETE CASCADE,
Description TEXT,
Quantity INT,
UnitPrice REAL,
PickedQuantity INT,
PickingCompletedWhen TEXT);

create table if not exists Orders(
OrderID INT PRIMARY KEY,
CustomerID INT REFERENCES Customers(CustomerID) ON DELETE CASCADE,
OrderDate TEXT,
ExpectedDeliveryDate TEXT,
CustomerPurchaseOrderNumber INT,
IsUndersupplyBackordered INT,
PickingCompletedWhen TEXT
);

create table if not exists StockItemHoldings(
StockItemHoldingID INT PRIMARY KEY,
StockItemID INT REFERENCES StockItems(StockItemID) ON DELETE CASCADE,
QuantityOnHand INT,
BinLocation TEXT, 
LastStocktakeQuantity INT,
LastCostPrice REAL,
ReorderLevel INT,
TargetStockLevel INT);


create table if not exists StockItemTransactions(
StockItemTransactionID INT,
StockItemID INT REFERENCES StockItems(StockItemID) ON DELETE CASCADE,
CustomerID INT REFERENCES Customers(CustomerID) ON DELETE CASCADE,
InvoiceID INT REFERENCES Invoices(InvoiceID) ON DELETE CASCADE,
TransactionOccurredWhen TEXT,
Quantity INT
);

EOF
for FILE in *.csv; do 
    echo "Importing $FILE"
    sqlite3 ../import_test.db << EOF
.mode csv
.import $FILE  ${FILE%.csv} 
EOF
done

