# Розробіть систему для управління адресною книгою.

# Сутності:
# Field: Базовий клас для полів запису.
# Name: Клас для зберігання імені контакту. Обов'язкове поле.
# Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр).
# Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів.
# AddressBook: Клас для зберігання та управління записами.

# Функціональність:
# AddressBook:Додавання записів.
# Пошук записів за іменем.
# Видалення записів за іменем.
# Record:Додавання телефонів.
# Видалення телефонів.
# Редагування телефонів.
# Пошук телефону.

from typing import Any


class Field():
    def __init__(self, value):
        self.value = value
    
    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, name:str):
        super().__init__(name)

class Phone(Field):
    def __init__(self, phone:str):
        if not self.is_valid(phone):
           raise ValueError
        super().__init__(phone) 

    def is_valid(self, phone):
        return len(phone)==10 and str(phone).isalnum()

class Record():
    def __init__(self, name):
        self.name = Name(name)
        self.items = []
    
    def add_phone(self, phone):
        try:
            ph = Phone(phone)
            self.items.append(ph)
            return ph
        except ValueError:
            return

    def find_phone(self, phone):
        try:
            return list(filter(lambda x:x.value == phone, self.items))[0]
        except IndexError:
            return


    def delete_phone(self, phone):
        ph = self.find_phone(phone)
        if ph:
            self.items.remove(ph)
        return ph
    
    def edit_phone(self, old_phone, new_phone):
        self.add_phone(new_phone)
        self.delete_phone(old_phone)

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.items)}"

class AddressBook():
    def __init__(self):
        self.data = []
    
    def add_record(self, record:Record):
        self.data.append(record)
    
    def find(self, name):
        try:
            return list(filter(lambda x: x.name.value == name, self.data))[0]
        except IndexError:
            return

    def delete(self, name):
        record = self.find(name)
        if record:
            self.data.remove(record)
        return record
    