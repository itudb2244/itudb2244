#!/bin/bash
#
cd Tables/full_backup
rm ../../import_test.db
    
for FILE in *.csv; do 
    echo "Importing $FILE"
    sqlite3 ../../import_test.db << EOF
.headers on
.mode csv
.import $FILE  ${FILE%.csv} 

EOF
done
cd ..
rm *.csv
sqlite3 ../import_test.db << EOF
.headers on 
.mode csv
.read ../drop_unnecessary.sql
.output People.csv
select * from People;
.output StockItems.csv
select * from StockItems;
.output Customers.csv
select * from Customers;
.output InvoiceLines.csv
select * from InvoiceLines;
.output Invoices.csv
select * from Invoices;
.output CustomerTransactions.csv
select * from CustomerTransactions;
.output OrderLines.csv
select * from OrderLines;
.output Orders.csv
select * from Orders;
.output StockItemHoldings.csv
select * from StockItemHoldings;
.output StockItemTransactions.csv
select * from StockItemTransactions;

EOF
echo "Created CSV files"
