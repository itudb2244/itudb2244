class Customer():
    def __init__(self, CustomerID, CustomerName, PrimaryContactPersonID, PhoneNumber, WebsiteURL, DeliveryAddressLine1, DeliveryAddressLine2):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.PrimaryContactPersonID = PrimaryContactPersonID
        self.PhoneNumber = PhoneNumber
        self.WebsiteURL = WebsiteURL
        self.DeliveryAddressLine1 = DeliveryAddressLine1
        self.DeliveryAddressLine2 = DeliveryAddressLine2
class CustomerTransactions():
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

class InvoiceLines():
    def __init__(self,InvoiceLineID,InvoiceID,StockItemID,Description,Quantity,UnitPrice,LineProfit,ExtendedPrice):
        self.InvoiceLineID =InvoiceLineID
        self.InvoiceID =InvoiceID
        self.StockItemID =StockItemID
        self.Description =Description
        self.Quantity =Quantity
        self.UnitPrice =UnitPrice
        self.LineProfit =LineProfit
        self.ExtendedPrice =ExtendedPrice

class Invoices():
    def __init__(self, CustomerID, CustomerName, PrimaryContactPersonID, PhoneNumber, WebsiteURL, DeliveryAddressLine1, DeliveryAddressLine2):
        self.InvoiceID = InvoiceID
        self.CustomerID = CustomerID
        self.OrderID = CustomerName
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

class OrderLines():
    def __init__(self, OrderLineID,OrderID,StockItemID,Description,Quantity,UnitPrice,PickedQuantity,PickingCompletedWhen):
        self.OrderLineID =OrderLineID
        self.OrderID =OrderID
        self.StockItemID =StockItemID
        self.Description =Description
        self.Quantity =Quantity
        self.UnitPrice =UnitPrice
        self.PickedQuantity =PickedQuantity
        self.PickingCompletedWhen =PickingCompletedWhen

class Orders():
    def __init__(self, OrderID,CustomerID,OrderDate,ExpectedDeliveryDate,CustomerPurchaseOrderNumber,IsUndersupplyBackordered,PickingCompletedWhen):
        self.OrderID =OrderID
        self.CustomerID =CustomerID
        self.OrderDate =OrderDate
        self.ExpectedDeliveryDate =ExpectedDeliveryDate
        self.CustomerPurchaseOrderNumber =CustomerPurchaseOrderNumber
        self.IsUndersupplyBackordered =IsUndersupplyBackordered
        self.PickingCompletedWhen =PickingCompletedWhen

class People():
    def __init__(self, PersonID,FullName,LogonName,HashedPassword,IsSystemUser,IsEmployee,IsSalesperson,PhoneNumber,EmailAddress):
        self.PersonID =PersonID
        self.FullName =FullName
        self.LogonName =LogonName
        self.HashedPassword =HashedPassword
        self.IsSystemUser =IsSystemUser
        self.IsEmployee =IsEmployee
        self.IsSalesperson =IsSalesperson
        self.PhoneNumber =PhoneNumber
        self.EmailAddress =EmailAddress

class StockItemHoldings():
    def __init__(self, StockItemID,QuantityOnHand,BinLocation,LastStocktakeQuantity,LastCostPrice,ReorderLevel,TargetStockLevel):
        self.StockItemID =StockItemID
        self.QuantityOnHand =QuantityOnHand
        self.BinLocation =BinLocation
        self.LastStocktakeQuantity =LastStocktakeQuantity
        self.LastCostPrice =LastCostPrice
        self.ReorderLevel =ReorderLevel
        self.TargetStockLevel =TargetStockLevel

class StockItems():
    def __init(self, StockItemID,StockItemName,LeadTimeDays,UnitPrice,RecommendedRetailPrice):
        self.StockItemID =StockItemID
        self.StockItemName =StockItemName
        self.LeadTimeDays =LeadTimeDays
        self.UnitPrice =UnitPrice
        self.RecommendedRetailPrice =RecommendedRetailPrice

class StockItemTransactions():
    def __init__(self, StockItemTransactionID,StockItemID,CustomerID,InvoiceID,TransactionOccurredWhen,Quantity):
        self.StockItemTransactionID =StockItemTransactionID
        self.StockItemID =StockItemID
        self.CustomerID =CustomerID
        self.InvoiceID =InvoiceID
        self.TransactionOccurredWhen =TransactionOccurredWhen
        self.Quantity =Quantity

