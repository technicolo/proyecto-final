class ContactForView:

    def __init__(self, contact) -> None:
        self.name = contact.name
        self.surname = contact.surname
        self.email = contact.email
        self.username = contact.username
        self.phone_number = contact.phone_number
        self.id = contact.id

    def __str__(self) -> str:
        return f"Id: {self.id} - Nombre: {self.name} - Apellido: {self.surname} - Email: {self.email} - Teléfono: {self.phone_number}"