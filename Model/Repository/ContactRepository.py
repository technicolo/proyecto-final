from ..Entities.Contact import Contact
from ..Context import Context
import re

class ContactRepository:

    def get_contacts_by_user(self, username):
        with Context() as context1:
            query = "SELECT * FROM contact WHERE state = 1 AND username = %s "
            values = (username,)
            context1.mycursor.execute(query, values)
            contactsDB = context1.mycursor.fetchall()
        contacts = []
        for contactDB in contactsDB:
            contact = Contact()
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]
            contact.username = contactDB[4]
            contact.state = contactDB[5]
            contact.phone_number = contactDB[6]
            contacts.append(contact)
        return contacts
    
    
    def get_contacts_by_characteristic(self, username, phone_number):
        # Eliminamos los caracteres especiales del número de teléfono ingresado
        clean_phone_number = re.sub(r'\W', '', phone_number)

        with Context() as context1:
            query = "SELECT * FROM contact WHERE state = 1 AND username = %s AND phone_number LIKE %s"
            values = (username, f"{clean_phone_number}%")
            context1.mycursor.execute(query, values)
            contactsDB = context1.mycursor.fetchall()

        contacts = []
        for contactDB in contactsDB:
            contact = Contact()
            contact.id = contactDB[0]
            contact.name = contactDB[1]
            contact.surname = contactDB[2]
            contact.email = contactDB[3]
            contact.username = contactDB[4]
            contact.state = contactDB[5]
            contact.phone_number = contactDB[6]
            contacts.append(contact)
        return contacts

    def get_contact(self, contact):
            with Context() as context1:
                query = "SELECT * FROM contact WHERE idcontact = %s AND state = 1"
                values = (contact.id,)
                context1.mycursor.execute(query, values)
                contactDB = context1.mycursor.fetchone()
                contact = Contact()
                contact.id = contactDB[0]
                contact.name = contactDB[1]
                contact.surname = contactDB[2]
                contact.email = contactDB[3]
                contact.phone_number = contactDB[4]
                contact.username = contactDB[5]
                contact.state = contactDB[6]
            return contact
            
    def add_contact(self, contact):
        with Context() as context1:
            query = "INSERT INTO contact (name, surname, email, username, phone_number, state) VALUES (%s, %s, %s, %s, %s, %s)"
            values = (contact.name, contact.surname, contact.email, contact.username, contact.phone_number, contact.state)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
            contact.id = context1.mycursor.lastrowid
        return contact
    
    def update_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET name = %s, surname = %s, email = %s, phone_number = %s WHERE idcontact = %s AND username = %s"
            values = (contact.name, contact.surname, contact.email, contact.phone_number, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()

    def delete_contact(self, contact):
        with Context() as context1:
            query = "UPDATE contact SET state = %s WHERE idcontact = %s AND username = %s"
            values = (0, contact.id, contact.username)
            context1.mycursor.execute(query, values)
            context1.mydb.commit()
    