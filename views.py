from flask import current_app, render_template, request, redirect, url_for
import services.customer_service as customerService

from services.service import *

class Context():
    def __init__(self):
        self.isEdit = False
        self.selectedID = 0
        self.selectedIDColumn = 0

class Table():
    def __init__(self, type, service, data_class):
        self.type = type
        self.service = service
        self.data_class = data_class
        #self.context = Context()

    def get_table(self):
        service = self.service()
        data = service.get_data()
        return render_template("generic_list.html", title=self.type, table=data, context=Context())

    def add_row(self):
        row = []
        columns = self.data_class.getColumns()
        for column in columns:
            if column in self.data_class.getNonKeyColumns():
                row.append(request.form[column])
            else:
                row.append(None)

        obj = self.data_class(row)

        service = self.service()
        service.add_row(obj)

        return redirect(url_for(self.type + "_page"))

    def update_row(self):
        idString = request.args.get("update_id")
        idString = idString.replace("'", "")
        id = idString.split("[")[1].split(",")[0]
        idColumn = self.data_class.getColumns()[0]
        
        if request.method == "GET":
            service = self.service()
            data = service.get_data()
            
            context = Context()
            context.isEdit = True
            context.selectedID = id
            context.selectedIDColumn = idColumn
            return render_template("generic_list.html", title=self.type, table=data, context=context)
        else:
            row = []
            columns = self.data_class.getColumns()
            for column in columns:
                if column in self.data_class.getNonKeyColumns():
                    row.append(request.form[column])
                else:
                    row.append(None)

            obj = self.data_class(row)

            service = self.service()
            service.update_row(obj, id, idColumn)
            return redirect(url_for(self.type + "_page"))

    def delete_row(self):
        idString = request.args.get("delete_id")
        idString.replace("'", "")
        id = idString.split("[")[1].split(",")[0]

        idColumn = self.data_class.getColumns()[0]

        service = self.service()
        service.delete_row(id, idColumn)

        return redirect(url_for(self.type + "_page"))

    def search(self):
        if request.method == "POST":
            
            service = self.service()
            search_data = service.search_and_list(request.form)
            return render_template("generic_list.html", title=self.type, table=search_data, context=Context())

        


class CustomerTable(Table):
    def __init__(self):
        super().__init__("Customers", CustomerService, Customer)
        

def home_page():
    return render_template("home.html")        
