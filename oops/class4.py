class Person:
    def __init__(self, p_id, name, gender, age, contact, address):
        self.p_id = p_id
        self.name = name
        self.gender = gender
        self.age = age
        self.contact = contact
        self.address = address

    def detail(self):
        D = {
            "ID": self.p_id,
            "Name": self.name,
            "Gender": self.gender,
            "Age": self.age,
            "Contact": self.contact,
            "Address": self.address
        }
        return 