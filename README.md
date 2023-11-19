Поки що це логіка роботи словника через застосування класів.
Без роботи користувача через командний рядок. Вона імітується перевірочним файлом

Завдання
У цій домашній роботі ми продовжимо розвивати нашого віртуального асистента з CLI інтерфейсом.

Наш асистент вже вміє взаємодіяти з користувачем за допомогою командного рядка, отримуючи команди та аргументи та виконуючи потрібні дії. У цьому завданні треба буде попрацювати над внутрішньою логікою асистента, над тим, як зберігаються дані, які саме дані і що з ними можна зробити.

Застосуємо для цих цілей об'єктно-орієнтоване програмування. Спершу виділимо декілька сутностей (моделей) з якими працюватимемо.

У користувача буде адресна книга або книга контактів. Ця книга контактів містить записи. Кожен запис містить деякий набір полів.

Таким чином ми описали сутності (класи), які необхідно реалізувати. Далі розглянемо вимоги до цих класів та встановимо їх взаємозв'язок, правила, за якими вони будуть взаємодіяти.

Користувач взаємодіє з книгой контактів, додаючи, видаляючи та редагуючи записи. Також користувач повинен мати можливість шукати в книзі контактів записи за одному або декількома критеріями (полям).

Про поля також можна сказати, що вони можуть бути обов'язковими (ім'я) та необов'язковими (наприклад телефон або email). Також записи можуть містити декілька полів одного типу (наприклад декілька телефонів). Користувач повинен мати можливість додавати/видаляти/редагувати поля у будь-якому записі.

Технічне завдання
Розробіть систему класів для управління адресною книгою.

Сутності:

Field: Базовий клас для полів запису. Буде батьківським для всіх полів, у ньому реалізується логіка загальна для всіх полів
Name: Клас для зберігання імені контакту. Обов'язкове поле.
Phone: Клас для зберігання номера телефону. Має валідацію формату (10 цифр). Необов'язкове поле з телефоном та таких один запис Record може містити декілька.
Record: Клас для зберігання інформації про контакт, включаючи ім'я та список телефонів. Відповідає за логіку додавання/видалення/редагування необов'язкових полів та зберігання обов'язкового поля Name
AddressBook: Клас для зберігання та управління записами. Успадковується від UserDict, та містить логіку пошуку за записами до цього класу
Функціональність:

AddressBook:
Додавання записів.
Пошук записів за іменем.
Видалення записів за іменем.
Record:
Додавання телефонів.
Видалення телефонів.
Редагування телефонів.
Пошук телефону.
Критерії приймання
Клас AddressBook:
Реалізовано метод add_record, який додає запис до self.data.
Реалізовано метод find, який знаходить запис за ім'ям.
Реалізовано метод delete, який видаляє запис за ім'ям.
Записи Record у AddressBook зберігаються як значення у словнику. В якості ключів використовується значення Record.name.value.
Клас Record:
Реалізовано зберігання об'єкта Name в окремому атрибуті.
Реалізовано зберігання списку об'єктів Phone в окремому атрибуті.
Реалізовано методи для додавання - add_phone/видалення - remove_phone/редагування - edit_phone/пошуку об'єктів Phone - find_phone.
Клас Phone:
Реалізовано валідацію номера телефону (має бути 10 цифр).
Реалізовано всі класи із завдання
Реалізація домашнього завдання
Ви повинні завантажити наступний репозиторій. Виконання домашнього завдання треба зробити в файлі main.py. Щоб перевірити правильність домашнього завдання вам потрібно запустити файл check_homework.py, який перевіряє тридцять основних тестових випадків, для вашої реалізації файлу main.py.

Якщо всі тести домашнього завдання пройдені він вам сповістить це зеленим кольором в консолі. Якщо тести не пройдено, то сповіщення для не пройденого тесту буде червоного кольору в консолі.

ВАЖЛИВО!
Після того як ваш код буде проходити всі тести, і вони виводяться в консоль зеленим кольором, ви здаєте його на перевірку ментору в LMS.

Рекомендації для виконання
В якості старту ви можете взяти наступний базовий код для реалізації цього домашнього завдання:

from collections import UserDict

class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

class Name(Field):
    # реалізація класу

class Phone(Field):
    # реалізація класу

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    # реалізація класу

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

class AddressBook(UserDict):
    # реалізація класу

Після реалізації ваш код має виконуватися наступним чином:

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

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")