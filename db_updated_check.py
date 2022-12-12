from datetime import *

def database_date_check():
    today_date = date.today()

#today_date = today.strftime("%d.%m.%Y")
    f = open("Tables/last_date.log", "r")
    text = f.read()
    text = text.split(".")

    last_date = datetime(int(text[2]), int(text[1]), int(text[0]))
    last_date = last_date.date()
    lo = open("local_date.log", "w")
    if last_date < today_date:
        print("Database is at the last version")
        return True
    else:
        print("Database is not at the last version")
        lo.write(last_date.strftime("%d.%m.%Y"))
        return False
    


