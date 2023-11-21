from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    def __init__(self, value):
        self.value = value.title()
#    def __str__(self):
#        return str.title(self.value)

class Phone(Field):
    def __init__(self, value):
        try:
            if (len (value) != 10) or (not value.isdigit()):
#                print (self.value) # AttributeError: 'Phone' object has no attribute 'value'
                raise ValueError
            else:
                self.value = value
        except ValueError:
#            print (self.value) # AttributeError: 'Phone' object has no attribute 'value'
            print ('Phone number should have 10 digit.')
#        print (self.value) # AttributeError: 'Phone' object has no attribute 'value'

#    def __str__(self):
#        return str(self.value) if self else None

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone (self, phone):
        phone_checked = Phone (phone)
#        print (phone_checked)
        try:
            print (phone_checked)
            self.phones.append (phone_checked)
            print (f"Phone number for '{self.name.value}' added.\n")
        except:
            print (f"Phone number '{phone}' not added.\n") 

    def remove_phone (self, phone):
        try:
            self.phones.remove (phone)
            print ("Phone number for '{self.name.value}' deleted\n")
        except:
            print ('There is not this phone number\n')

    def edit_phone (self, phone1, phone2):
        for exist_phone in self.phones:
            if phone1 == exist_phone.value:
                self.phones.remove (exist_phone)
                phone_checked = Phone (phone2)
                if phone_checked:
                    self.phones.append (phone_checked)
                    return f"Phone number for '{self.name.value}' edited\n"
        raise ValueError
#        print (f"'{self.name.value}' don't have phone number, what you want to edit\n")

    def find_phone (self, phone):
        for find_phone in self.phones:
            if phone == find_phone.value:
                return find_phone
        print (f"'{self.name.value}' don't have phone number, what you want to find\n")

    def __str__(self):
        try:
            return f"Contact name: {self.name.value}; phones: {', '.join(p.value for p in self.phones)}"
        except AttributeError:
            return f"Contact name: {self.name.value}; phones: no phones added"

class AddressBook(UserDict):
    def __init__(self):
        self.data = {}

    def add_record (self, record: Record):
        self.data.update ({record.name.value: record})
#        print (self.data)
        print (f"Contact '{record.name.value}' added\n")

    def find (self, name):
        self.name = Name (name)
        return self.data.get (self.name.value)
#        return self.data.get (self.name.value, print (f"Contact '{name}' not found\n"))

    def delete (self, Record):
        record_to_delete = book.find(Record)
        if self.data.get (record_to_delete.name.value):
            self.data.pop (record_to_delete.name.value)
            print (f"Contact '{record_to_delete.name.value}' deleted\n")
        else:
            print (f"Contact book don't have contact '{record_to_delete.name.value}'\n")

if __name__ == "__main__":
 # Створення нової адресної книги
    book = AddressBook()

# Створення запису для John
    print ('-----Створення запису для John-----')
    john_record = Record("john")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555d")

# Додавання запису John до адресної книги
    print ('-----Додавання запису John до адресної книги-----')
    book.add_record(john_record)

# Створення та додавання нового запису для Jane
#    print ('-----Створення та додавання нового запису для Jane-----')
#    jane_record = Record("jane")
#    jane_record.add_phone("9876543210")
#    book.add_record(jane_record)

# Виведення всіх записів у книзі
    print ('-----Виведення всіх записів у книзі-----')
    for name, record in book.data.items():
        print(record)
    print ('')

# Знаходження та редагування телефону для John
#    print ('-----Знаходження та редагування телефону для John-----')
#    john = book.find("john")
#    john.edit_phone("1234567890", "1112223333")

#    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
#    print ('-----Пошук конкретного телефону у записі John-----')
#    found_phone = john.find_phone("5555555555")
#    print(f"{john.name}: {found_phone}\n")  # Виведення: 5555555555

    # Видалення запису Jane
#    print ('-----Видалення запису Jane-----')
#    jane11 = book.find("jane")
#    print (jane11, '- found jane11')
#    book.delete("Jane")
#    jane22 = book.find("Jane")
#    print (jane22, '- found jane22')
