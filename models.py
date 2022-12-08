class Customer():
    def __init__(self, CustomerID, CustomerName, PrimaryContactPersonID, PhoneNumber, WebsiteURL, DeliveryAddressLine1, DeliveryAddressLine2):
        self.CustomerID = CustomerID
        self.CustomerName = CustomerName
        self.PrimaryContactPersonID = PrimaryContactPersonID
        self.PhoneNumber = PhoneNumber
        self.WebsiteURL = WebsiteURL
        self.DeliveryAddressLine1 = DeliveryAddressLine1
        self.DeliveryAddressLine2 = DeliveryAddressLine2

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

