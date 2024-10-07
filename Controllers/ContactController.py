from Model.DTO.ContactForView import ContactForView
from Model.Repository.ContactRepository import ContactRepository


class ContactController:
    def get_contacts_by_user(self, username):
        contact_repository = ContactRepository()
        contacts = contact_repository.get_contacts_by_user(username)
        return contacts 
    
    def get_contacts_by_characteristic(self, username, characteristic):
        contact_repository = ContactRepository()
        contacts = contact_repository.get_contacts_by_characteristic(username, characteristic)
        return contacts

    def clean_phone_number(self, phone_number):
        # Eliminar caracteres especiales del número de teléfono
        cleaned_number = phone_number.replace("-", "").replace("(", "").replace(")", "").replace("+", "").replace(" ", "")
        return cleaned_number

    def get_contact(self, contact):
        contact_repository = ContactRepository()
        contact = contact_repository.get_contact(contact)
        contactForView = ContactForView(contact)
        return contactForView
    
    def add_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.add_contact(contact)

    def update_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.update_contact(contact)

    def delete_contact(self, contact):
        contact_repository = ContactRepository()
        contact_repository.delete_contact(contact)