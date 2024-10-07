class Contact:
    def __init__(self):
        self.id = 0
        self.name = ""
        self.surname = ""
        self.email = ""
        self.phone_number = ""
        self.username = ""
        self.state = True


    def __repr__(self) -> str:
        return f"Contact(id={self.id}, name={self.name}, surname={self.surname}, email={self.email}, phone_number={self.phone_number}, username={self.username}, state={self.state})"
