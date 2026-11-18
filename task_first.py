from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        if value is None or not str(value).strip():
            raise ValueError("Required name")
        super().__init__(str(value).strip())

class Phone(Field):
     def __init__(self, value):
        value = str(value)
        if len(value) != 10 or not value.isdigit():
            raise ValueError("Required phone number (10 numbers)")
        super().__init__(value)

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []


    def add_phone(self, phone, *args):
        phones = [Phone(number) for number in (phone, *args)]
        self.phones.extend(phones)


    def find_phone(self, phone):
        phone = str(phone)
        for existing_phone in self.phones:
            if existing_phone.value == phone:
                return existing_phone
        return None


    def remove_phone(self, phone):
        found = self.find_phone(phone)
        if found is None:
            raise ValueError("Phone is not found")
        self.phones.remove(found)


    def edit_phone(self, old_phone, new_phone):
        old_phone = str(old_phone)
        for index, existing_phone in enumerate(self.phones):
            if existing_phone.value == old_phone:
                self.phones[index] = Phone(new_phone)
                return
        raise ValueError("Phone is not found")


    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(str(name))

    def delete(self, name):
        self.data.pop(str(name), None)

if __name__ == "__main__":
    # Створення нової адресної книги
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону в записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")

