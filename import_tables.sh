#!/bin/bash
#
cd Tables
rm ../import_test.db
    sqlite3 ../import_test.db << EOF
create table People(
PersonID INT PRIMARY KEY,
FullName TEXT,
LogonName TEXT,
HashedPassword TEXT,
IsSystemUser INT,
IsEmployee INT,
IsSalesperson INT,
PhoneNumber TEXT,
EmailAddress TEXT);

create table StockItems(
StockItemID INT PRIMARY KEY,
StockItemName TEXT,
LeadTimeDays INT,
UnitPrice REAL,
RecommendedRetailPrice REAL
);

create table Customers(
CustomerID INT PRIMARY KEY,
CustomerName TEXT,
PrimaryContactPersonID INT REFERENCES People(PersonID),
PhoneNumber INT,
WebsiteURL TEXT,
DeliveryAddressLine1 TEXT,
DeliveryAddressLine2 TEXT);


create table InvoiceLines(
InvoiceLineID INT PRIMARY KEY,
InvoiceID INT REFERENCES Invoices(InvoiceID),
StockItemID INT REFERENCES StockItems(StockItemID),
Description TEXT,
Quantity INT,
UnitPrice REAL,
LineProfit REAL,
ExtendedPrice REAL
);

create table Invoices( 
InvoiceID INT PRIMARY KEY,
CustomerID INT REFERENCES Customers(CustomerID),
OrderID	INT REFERENCES Orders(OrderID),
ContactPersonID INT REFERENCES People(PersonID),
AccountsPersonID INT REFERENCES People(PersonID),
InvoiceDate TEXT,
CustomerPurchaseOrderNumber INT,
DeliveryInstructions TEXT,
InternalComments TEXT,
DeliveryRun TEXT,
RunPosition INT,
ReturnedDeliveryData TEXT,
ConfirmedDeliveryTime TEXT,
ConfirmedReceivedBy TEXT);

create table CustomerTransactions(
CustomerTransactionID INT PRIMARY KEY,
CustomerID INT REFERENCES Customers(CustomerID),
InvoiceID INT REFERENCES Invoices(InvoiceID),
TransactionDate TEXT,
AmountExcludingTax REAL,
TaxAmount REAL,
TransactionAmount REAL,
OutstandingBalance REAL,
FinalizationDate TEXT,
IsFinalized INT
);

create table OrderLines(
OrderLineID INT PRIMARY KEY,
OrderID INT REFERENCES Orders(OrderID),
StockItemID INT REFERENCES StockItems(StockItemID),
Description TEXT,
Quantity INT,
UnitPrice REAL,
PickedQuantity INT,
PickingCompletedWhen TEXT);

create table Orders(
OrderID INT PRIMARY KEY,
CustomerID INT REFERENCES Customers(CustomerID),
OrderDate TEXT,
ExpectedDeliveryDate TEXT,
CustomerPurchaseOrderNumber INT,
IsUndersupplyBackordered INT,
PickingCompletedWhen TEXT
);


create table StockItemHoldings(
StockItemID INT REFERENCES StockItems(StockItemID),
QuantityOnHand INT,
BinLocation TEXT, 
LastStocktakeQuantity INT,
LastCostPrice REAL,
ReorderLevel INT,
TargetStockLevel INT);


create table StockItemTransactions(
StockItemTransactionID INT,
StockItemID INT REFERENCES StockItems(StockItemID),
CustomerID INT REFERENCES Customers(CustomerID),
InvoiceID INT REFERENCES Invoices(InvoiceID),
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

