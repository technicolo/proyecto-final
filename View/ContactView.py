from os import system
from Controllers.ContactController import ContactController
from Model.DTO.ContactForDelete import ContactForDelete
from Model.DTO.ContactForUpdate import ContactForUpdate
from Model.DTO.UserForView import UserForView

class ContactView:    
    def __init__(self, user):
        self.user_logged = user
    
    def Menu(self):
        while True:
            system("cls")
            print(" Menu de contactos ".center(50, "#"))
            print("1 - Lista de contactos")
            print("2 - Agregar contacto")
            print("3 - Editar contacto")
            print("4 - Eliminar contacto")
            print("5 - Cerrar sesion de usuario")
            print("6 - busque un contatco por caracteristica")
            print("-" * 50)
            option = input("Ingrese una opcion:")
            if option == "1":
                self.listContacts()
            elif option == "2":
                self.addContact()
            elif option == "3":
                self.editContact()
            elif option == "4":
                self.deleteContact()
            elif option == "5":
                break
            elif option == "6":
                self.listContactsByCharacteristic()
            else:
                print(" Opcion incorrecta ".center(50, "!"))
                input(" Presione enter para continuar ".center(50, "!"))

    def listContacts(self):
        system("cls")
        print(" Lista de contactos ".center(50, "#"))
        contactC = ContactController()
        contacts = contactC.get_contacts_by_user(self.user_logged.username)
        for contact in contacts:
            # Accedemos al atributo 'phone_number' en el objeto 'contact'
            print(f"Id: {contact.id} - Nombre: {contact.name} - Apellido: {contact.surname} - Email: {contact.email} - Teléfono: {contact.phone_number}")
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))

    def addContact(self):
        system("cls")
        print(" Alta de contacto ".center(50, "!"))
        print("-"*50)
        name = input("Ingrese el nombre del contacto: ")
        print("-"*50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-"*50)
        email = input("Ingrese el email del contacto: ")
        print("-"*50)
        phone_number = input("Ingrese el número de teléfono del contacto: ")
        print("-"*50)
        contactC = ContactController()
        contactC.add_contact(ContactForUpdate(0, name, surname, email, phone_number, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))

    def editContact(self):
        system("cls")
        print(" Editar contacto ".center(50, "#"))
        print("-"*50)
        id = input("Ingrese el id del contacto a editar: ")
        print("-"*50)
        name = input("Ingrese el nombre del contacto: ")
        print("-"*50)
        surname = input("Ingrese el apellido del contacto: ")
        print("-"*50)
        email = input("Ingrese el email del contacto: ")
        print("-"*50)
        phone_number = input("Ingrese el número de teléfono del contacto: ")
        print("-"*50)
        contactC = ContactController()
        contactC.update_contact(ContactForUpdate(id, name, surname, email, phone_number, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))


    def listContactsByCharacteristic(self):
        system("cls")
        print(" Lista de contactos por característica ".center(50, "#"))
        characteristic = input("Ingrese la característica para buscar contactos que la contengan: ")
        contactC = ContactController()
        contacts = contactC.get_contacts_by_characteristic(self.user_logged.username, characteristic)
        if not contacts:
            print("No se encontraron contactos con la característica especificada.")
        else:
            for contact in contacts:
                print(f"Id: {contact.id} - Nombre: {contact.name} - Apellido: {contact.surname} - Email: {contact.email} - Teléfono: {contact.phone_number}")
        print("#"*50)
        input(" Presione enter para continuar ".center(50, "!"))


    def deleteContact(self):
        system("cls")
        print(" Eliminar contacto ".center(50, "!"))
        print("-"*50)
        id = input("Ingrese el id del contacto a eliminar: ")
        print("-"*50)
        contactC = ContactController()
        contactC.delete_contact(ContactForDelete(id, self.user_logged.username))
        input(" Presione enter para continuar ".center(50, "!"))


