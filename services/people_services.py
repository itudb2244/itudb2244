from flask import current_app
import sqlite3
from models import People

def get_people():
    query = "SELECT * FROM PEOPLE"
    people = []

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        res = cursor.execute(query)
        for row in res:
            person = People(row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            people.append(person)
    return people

def get_person(id):
    query = "SELECT * FROM PEOPLE WHERE((PEOPLE.personID = %s)"

    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        tuple = cursor.fetchone()
        if tuple is not None:
            dictionary = dict(tuple)
            person = People(dictionary['PersonID'], dictionary['FullName'], dictionary['LogonName'], dictionary['HashedPassword'], dictionary['IsSystemUser'], dictionary['IsEmployee'], dictionary['IsSalesperson'], dictionary['PhoneNumber'], dictionary['EmailAddress'])
            return person
    return None

def add_person(Person):
    query = "INSERT INTO PEOPLE (fullName, logonName, hashedPassword,  isSystemUser, isEmployee, isSalesperson, phoneNumber, emailAddress)"\
            "VALUES (%(fullName)s, %(logonName)s,%(hashedPassword)s,%(isSystemUser)s,%(isEmployee)s,%(isSalesperson)s,%(phoneNumber)s, %(emailAddress)s)"\
            "RETURNING personID"
    with sqlite3.connect(current_app.config["dbname"]) as connection:
        cursor = connection.cursor()
        person = Person.get()
        cursor.execute(query,person)
        personID = cursor.fetchone()[0]
        return personID
        
def delete_person(id):
    query = "DELETE FROM PEOPLE WHERE(personID = %s)"
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (id,))
            return True
    except:
        return False

def update_person(id,Person):
    query = "UPDATE PEOPLE SET fullName=%s, logonName=%s, hashedPassword=%s, isSystemUser=%s, isEmployee=%s, isSalesperson=%s, phoneNumber=%s, emailAddress=%s WHERE (personID = %s)"
    person = Person.get()
    try:
        with sqlite3.connect(current_app.config["dbname"]) as connection:
            cursor = connection.cursor()
            cursor.execute(query, (person['fullName'], person['logonName'], person['hashedPassword'], person['isSystemUser'], person['isEmployee'], person['isSalesperson'], person['phoneNumber'], person['emailAddress'], id))
            return True
    except sqlite3.Error as er:
        # get the extended result code here
        return False 




