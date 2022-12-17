import copy

class Customer(object):
    def __init__(self, row):
        self.CustomerID = row[0]
        self.CustomerName = row[1]
        self.PrimaryContactPersonID = row[2]
        self.PhoneNumber = row[3]
        self.WebsiteURL = row[4]
        self.DeliveryAddressLine1 = row[5]
        self.DeliveryAddressLine2 = row[6]

    def setID(self, id=None):
        self.id = id
        return self.id

    def toDict(self):
        customer = {
            'CustomerID': self.CustomerID,
            'CustomerName': self.CustomerName,
            'PrimaryContactPersonID': self.PrimaryContactPersonID,
            'PhoneNumber': self.PhoneNumber,
            'WebsiteURL': self.WebsiteURL,
            'DeliveryAddressLine1': self.DeliveryAddressLine1,
            'DeliveryAddressLine2': self.DeliveryAddressLine2,
        }
        return customer

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

    def getColumns():
        return ["CustomerName", "PhoneNumber", "WebsiteURL", "DeliveryAddressLine1", "DeliveryAddressLine2"]

    
class CustomerTransactions(object):
    def __init__(self,CustomerTransactionID,CustomerID,InvoiceID,TransactionDate,AmountExcludingTax,TaxAmount,TransactionAmount,OutstandingBalance,FinalizationDate,IsFinalized):
        self.CustomerTransactionID =CustomerTransactionID
        self.CustomerID =CustomerID
        self.InvoiceID =InvoiceID
        self.TransactionDate =TransactionDate
        self.AmountExcludingTax =AmountExcludingTax
        self.TaxAmount =TaxAmount
        self.TransactionAmount =TransactionAmount
        self.OutstandingBalance =OutstandingBalance
        self.FinalizationDate =FinalizationDate
        self.IsFinalize =IsFinalized

    def toDict(self):
        customertransactions = {
            'CustomerTransactionID': self.CustomerTransactionID,
            'CustomerID': self.CustomerID,
            'InvoiceID': self.InvoiceID,
            'TransactionDate': self.TransactionDate,
            'AmountExcludingTax': self.AmountExcludingTax,
            'TaxAmount': self.TaxAmount,
            'TransactionAmount': self.TransactionAmount,
            'OutstandingBalance': self.OutstandingBalance,
            'FinalizationDate': self.FinalizationDate,
            'IsFinalize': self.IsFinalize,
        }
        return customertransactions

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

class InvoiceLines(object):
    def __init__(self,InvoiceLineID,InvoiceID,StockItemID,Description,Quantity,UnitPrice,LineProfit,ExtendedPrice):
        self.InvoiceLineID =InvoiceLineID
        self.InvoiceID =InvoiceID
        self.StockItemID =StockItemID
        self.Description =Description
        self.Quantity =Quantity
        self.UnitPrice =UnitPrice
        self.LineProfit =LineProfit
        self.ExtendedPrice =ExtendedPrice

    def toDict(self):
        invoicelines = {
            'InvoiceLineID': self.InvoiceLineID,
            'InvoiceID': self.InvoiceID,
            'StockItemID': self.StockItemID,
            'Description': self.Description,
            'Quantity': self.Quantity,
            'UnitPrice': self.UnitPrice,
            'LineProfit': self.LineProfit,
            'ExtendedPrice': self.ExtendedPrice,
        }
        return invoicelines

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

class Invoices(object):
    def __init__(self, InvoiceID,CustomerID,OrderID,ContactPersonID,AccountsPersonID,InvoiceDate,CustomerPurchaseOrderNumber,DeliveryInstructions,InternalComments,DeliveryRun,RunPosition,ReturnedDeliveryData,ConfirmedDeliveryTime,ConfirmedReceivedBy):
        self.InvoiceID = InvoiceID
        self.CustomerID = CustomerID
        self.OrderID = OrderID
        self.ContactPersonID = ContactPersonID
        self.AccountsPersonID = AccountsPersonID
        self.InvoiceDate = InvoiceDate
        self.CustomerPurchaseOrderNumber = CustomerPurchaseOrderNumber
        self.DeliveryInstructions = DeliveryInstructions
        self.InternalComments = InternalComments
        self.DeliveryRun =DeliveryRun
        self.RunPosition=RunPosition
        self.ReturnedDeliveryData=ReturnedDeliveryData
        self.ConfirmedDeliveryTime=ConfirmedDeliveryTime
        self.ConfirmedReceivedBy=ConfirmedReceivedBy

    def toDict(self):
        invoices = {
            'InvoiceID': self.InvoiceID,
            'CustomerID': self.CustomerID,
            'OrderID': self.OrderID,
            'ContactPersonID': self.ContactPersonID,
            'AccountsPersonID': self.AccountsPersonID,
            'InvoiceDate': self.InvoiceDate,
            'CustomerPurchaseOrderNumber': self.CustomerPurchaseOrderNumber,
            'DeliveryInstructions': self.DeliveryInstructions,
            'InternalComments': self.InternalComments,
            'DeliveryRun': self.DeliveryRun,
            'RunPosition': self.RunPosition,
            'ReturnedDeliveryData': self.ReturnedDeliveryData,
            'ConfirmedDeliveryTime': self.ConfirmedDeliveryTime,
            'ConfirmedReceivedBy': self.ConfirmedReceivedBy,
        }
        return invoices

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

class OrderLines(object):
    def __init__(self, OrderLineID,OrderID,StockItemID,Description,Quantity,UnitPrice,PickedQuantity,PickingCompletedWhen):
        self.OrderLineID =OrderLineID
        self.OrderID =OrderID
        self.StockItemID =StockItemID
        self.Description =Description
        self.Quantity =Quantity
        self.UnitPrice =UnitPrice
        self.PickedQuantity =PickedQuantity
        self.PickingCompletedWhen =PickingCompletedWhen

    def toDict(self):
        orderlines = {
            'OrderLineID': self.OrderLineID,
            'OrderID': self.OrderID,
            'OrderID': self.OrderID,
            'StockItemID': self.StockItemID,
            'Description': self.Description,
            'Quantity': self.Quantity,
            'PickedQuantity': self.PickedQuantity,
            'PickingCompletedWhen': self.PickingCompletedWhen,
        }
        return orderlines

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

class Orders(object):
    def __init__(self, OrderID,CustomerID,OrderDate,ExpectedDeliveryDate,CustomerPurchaseOrderNumber,IsUndersupplyBackordered,PickingCompletedWhen):
        self.OrderID =OrderID
        self.CustomerID =CustomerID
        self.OrderDate =OrderDate
        self.ExpectedDeliveryDate =ExpectedDeliveryDate
        self.CustomerPurchaseOrderNumber =CustomerPurchaseOrderNumber
        self.IsUndersupplyBackordered =IsUndersupplyBackordered
        self.PickingCompletedWhen =PickingCompletedWhen

    def toDict(self):
        orders = {
            'OrderID': self.OrderID,
            'CustomerID': self.CustomerID,
            'OrderDate': self.OrderDate,
            'ExpectedDeliveryDate': self.ExpectedDeliveryDate,
            'CustomerPurchaseOrderNumber': self.CustomerPurchaseOrderNumber,
            'IsUndersupplyBackordered': self.IsUndersupplyBackordered,
            'PickingCompletedWhen': self.PickingCompletedWhen,
        }
        return orders

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

class People(object):
    def __init__(self, row):
        self.PersonID = row[0]
        self.FullName = row[1]
        self.LogonName = row[2]
        self.HashedPassword = row[3]
        self.IsSystemUser = row[4]
        self.IsEmployee = row[5]
        self.IsSalesperson = row[6]
        self.PhoneNumber = row[7]
        self.EmailAddress = row[8]

    def toDict(self):
        people = {
            'PersonID': self.PersonID,
            'FullName': self.FullName,
            'LogonName': self.LogonName,
            'HashedPassword': self.HashedPassword,
            'IsSystemUser': self.IsSystemUser,
            'IsEmployee': self.IsEmployee,
            'IsSalesPerson': self.IsSalesperson,
            'PhoneNumber': self.PhoneNumber,
            'EmailAddress': self.EmailAddress,
        }
        return people

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

class StockItemHoldings(object):
    def __init__(self, StockItemHoldingID, StockItemID,QuantityOnHand,BinLocation,LastStocktakeQuantity,LastCostPrice,ReorderLevel,TargetStockLevel):
        self.StockItemHoldingID=StockItemHoldingID
        self.StockItemID =StockItemID
        self.QuantityOnHand =QuantityOnHand
        self.BinLocation =BinLocation
        self.LastStocktakeQuantity =LastStocktakeQuantity
        self.LastCostPrice =LastCostPrice
        self.ReorderLevel =ReorderLevel
        self.TargetStockLevel =TargetStockLevel

    def toDict(self):
        stockitemholdings = {
            'StockItemID': self.StockItemID,
            'QuantityOnHand': self.QuantityOnHand,
            'BinLocation': self.BinLocation,
            'LastStocktakeQuantity': self.LastStocktakeQuantity,
            'LastCostPrice': self.LastCostPrice,
            'ReorderLevel': self.ReorderLevel,
            'TargetStockLevel': self.TargetStockLevel,
        }
        return stockitemholdings

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

class StockItems(object):
    def __init(self, StockItemID,StockItemName,LeadTimeDays,UnitPrice,RecommendedRetailPrice):
        self.StockItemID =StockItemID
        self.StockItemName =StockItemName
        self.LeadTimeDays =LeadTimeDays
        self.UnitPrice =UnitPrice
        self.RecommendedRetailPrice =RecommendedRetailPrice

    def toDict(self):
        stockitems = {
            'StockItemID': self.StockItemID,
            'StockItemName': self.StockItemName,
            'LeadTimeDays': self.LeadTimeDays,
            'UnitPrice': self.UnitPrice,
            'RecommendedRetailPrice': self.RecommendedRetailPrice,
        }
        return stockitems

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

class StockItemTransactions(object):
    def __init__(self, StockItemTransactionID,StockItemID,CustomerID,InvoiceID,TransactionOccurredWhen,Quantity):
        self.StockItemTransactionID =StockItemTransactionID
        self.StockItemID =StockItemID
        self.CustomerID =CustomerID
        self.InvoiceID =InvoiceID
        self.TransactionOccurredWhen =TransactionOccurredWhen
        self.Quantity =Quantity

    def toDict(self):
        stockitemtransactions = {
            'StockItemTransactionID': self.StockItemTransactionID,
            'StockID': self.StockItemID,
            'CustomerID': self.CustomerID,
            'InvoiceID': self.InvoiceID,
            'TransactionOccerredWhen': self.TransactionOccurredWhen,
            'Quantity': self.Quantity,
        }
        return stockitemtransactions

    def get(self):
        return self.toDict()

    def getCopy(self):
        return copy.deepcopy(self)

