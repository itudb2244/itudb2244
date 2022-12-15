
ALTER TABLE Customers DROP COLUMN BillToCustomerID;
ALTER TABLE Customers DROP COLUMN AlternateContactPersonID;
ALTER TABLE Customers DROP COLUMN CustomerCategoryID;
ALTER TABLE Customers DROP COLUMN BuyingGroupID;
ALTER TABLE Customers DROP COLUMN DeliveryMethodID;
ALTER TABLE Customers DROP COLUMN DeliveryCityID;
ALTER TABLE Customers DROP COLUMN PostalCityID;
ALTER TABLE Customers DROP COLUMN CreditLimit;
ALTER TABLE Customers DROP COLUMN AccountOpenedDate;
ALTER TABLE Customers DROP COLUMN StandardDiscountPercentage;
ALTER TABLE Customers DROP COLUMN IsStatementSent;
ALTER TABLE Customers DROP COLUMN IsOnCreditHold;
ALTER TABLE Customers DROP COLUMN PaymentDays;
ALTER TABLE Customers DROP COLUMN FaxNumber;
ALTER TABLE Customers DROP COLUMN DeliveryRun;
ALTER TABLE Customers DROP COLUMN RunPosition;
ALTER TABLE Customers DROP COLUMN DeliveryPostalCode;
ALTER TABLE Customers DROP COLUMN DeliveryLocation;
ALTER TABLE Customers DROP COLUMN PostalAddressLine1;
ALTER TABLE Customers DROP COLUMN PostalAddressLine2;
ALTER TABLE Customers DROP COLUMN PostalPostalCode;
ALTER TABLE Customers DROP COLUMN LastEditedBy;
ALTER TABLE Customers DROP COLUMN ValidFrom;
ALTER TABLE Customers DROP COLUMN ValidTo;


ALTER TABLE CustomerTransactions DROP COLUMN PaymentMethodID;
ALTER TABLE CustomerTransactions DROP COLUMN TransactionTypeID;
ALTER TABLE CustomerTransactions DROP COLUMN LastEditedBy;
ALTER TABLE CustomerTransactions DROP COLUMN LastEditedWhen;


ALTER TABLE InvoiceLines DROP COLUMN PackageTypeID;
ALTER TABLE InvoiceLines  DROP COLUMN TaxRate;
ALTER TABLE InvoiceLines  DROP COLUMN TaxAmount;
ALTER TABLE InvoiceLines DROP COLUMN LastEditedBy;
ALTER TABLE InvoiceLines DROP COLUMN LastEditedWhen;


ALTER TABLE Invoices DROP COLUMN BillToCustomerID;
ALTER TABLE Invoices DROP COLUMN DeliveryMethodID;
ALTER TABLE Invoices DROP COLUMN SalespersonPersonID;
ALTER TABLE Invoices DROP COLUMN PackedByPersonID;
ALTER TABLE Invoices DROP COLUMN IsCreditNote;
ALTER TABLE Invoices DROP COLUMN CreditNoteReason;
ALTER TABLE Invoices DROP COLUMN Comments;
ALTER TABLE Invoices DROP COLUMN TotalDryItems;
ALTER TABLE Invoices DROP COLUMN TotalChillerItems;
ALTER TABLE Invoices DROP COLUMN LastEditedBy;
ALTER TABLE Invoices DROP COLUMN LastEditedWhen;


ALTER TABLE OrderLines DROP COLUMN PackageTypeID;
ALTER TABLE OrderLines DROP COLUMN TaxRate;
ALTER TABLE OrderLines DROP COLUMN LastEditedBy;
ALTER TABLE OrderLines DROP COLUMN LastEditedWhen;


ALTER TABLE Orders DROP COLUMN SalespersonPersonID;
ALTER TABLE Orders DROP COLUMN PickedByPersonID;
ALTER TABLE Orders DROP COLUMN ContactPersonID;
ALTER TABLE Orders DROP COLUMN BackorderOrderID;
ALTER TABLE Orders DROP COLUMN Comments;
ALTER TABLE Orders DROP COLUMN DeliveryInstructions;
ALTER TABLE Orders DROP COLUMN InternalComments;
ALTER TABLE Orders DROP COLUMN LastEditedBy;
ALTER TABLE Orders DROP COLUMN LastEditedWhen;


ALTER TABLE People DROP COLUMN PreferredName;
ALTER TABLE People DROP COLUMN SearchName;
ALTER TABLE People DROP COLUMN IsPermittedToLogon;
ALTER TABLE People DROP COLUMN IsExternalLogonProvider;
ALTER TABLE People DROP COLUMN UserPreferences;
ALTER TABLE People DROP COLUMN FaxNumber;
ALTER TABLE People DROP COLUMN Photo;
ALTER TABLE People DROP COLUMN CustomFields;
ALTER TABLE People DROP COLUMN OtherLanguages;
ALTER TABLE People DROP COLUMN LastEditedBy;
ALTER TABLE People DROP COLUMN ValidFrom;
ALTER TABLE People DROP COLUMN ValidTo;


ALTER TABLE StockItemHoldings DROP COLUMN LastEditedBy;
ALTER TABLE StockItemHoldings DROP COLUMN LastEditedWhen;


ALTER TABLE StockItems DROP COLUMN SupplierID;
ALTER TABLE StockItems DROP COLUMN ColorID;
ALTER TABLE StockItems DROP COLUMN UnitPackageID;
ALTER TABLE StockItems DROP COLUMN OuterPackageID;
ALTER TABLE StockItems DROP COLUMN Brand;
ALTER TABLE StockItems DROP COLUMN Size;
ALTER TABLE StockItems DROP COLUMN QuantityPerOuter;
ALTER TABLE StockItems DROP COLUMN IsChillerStock;
ALTER TABLE StockItems DROP COLUMN Barcode;
ALTER TABLE StockItems DROP COLUMN TaxRate;
ALTER TABLE StockItems DROP COLUMN TypicalWeightPerUnit;
ALTER TABLE StockItems DROP COLUMN MarketingComments;
ALTER TABLE StockItems DROP COLUMN InternalComments;
ALTER TABLE StockItems DROP COLUMN Photo;
ALTER TABLE StockItems DROP COLUMN CustomFields;
ALTER TABLE StockItems DROP COLUMN Tags;
ALTER TABLE StockItems DROP COLUMN SearchDetails;
ALTER TABLE StockItems DROP COLUMN LastEditedBy;
ALTER TABLE StockItems DROP COLUMN ValidFrom;
ALTER TABLE StockItems DROP COLUMN ValidTo;


ALTER TABLE StockItemTransactions DROP COLUMN TransactionTypeID;
ALTER TABLE StockItemTransactions DROP COLUMN SupplierID;
ALTER TABLE StockItemTransactions DROP COLUMN PurchaseOrderID;
ALTER TABLE StockItemTransactions DROP COLUMN LastEditedBy;
ALTER TABLE StockItemTransactions DROP COLUMN LastEditedWhen;
