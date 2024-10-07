class ContactForUpdate:
    def __init__(self, id, name, surname, email, phone_number, username) -> None:
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.phone_number = phone_number
        self.username = username
        self.state = 1
    