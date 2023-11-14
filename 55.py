# Создать телефонный справочник с возможностью импорта
# и экспорта данных в формате .txt. Фамилия, имя, отчество,
# номер телефона - данные, которые должны находиться в файле.
# Программа должна выводить данные Программа должна сохранять
# данные в текстовом файле Пользователь может ввести одну
# из характеристик для поиска определенной записи
# (Например имя или фамилию человека) Использование функций.
# Ваша программа не должна быть линейной

# 1. Создать сам файл:
# - открываем файл на дозапись

# 2. Добавление контакта:
# - запросить/получить у пользователя данные (осуществить проверку на корректность) +++
# - подготовить форматирование данных к записи +++
# - открыть файл на дозапись
# - добавить новый контакт в файл

# 3. Вывод данных на экран +++
# - открыть файл на чтение +++
# - считать текст +++
# - вывод на экран +++

# 4. Поиск контакта
# - запросить/получить у пользователя данные для поиска
# - открыть файл на чтение
# - произвести поиск контакта
# - вывести на экран

# 5. Интерфейс
# - создать файл
# - вывод на экран меню пользователя +++
# - запросить/получить у пользователя вариант режима работы (1,2,3,4) +++
# - вызов соответствующей функции +++
# - осуществление выхода из программы +++


# Дополнить справочник возможностью копирования данных из одного файла в другой. 
# Пользователь вводит номер строки, которую необходимо перенести из одного файла в другой.

import os, re


fileName = "phonebook.txt"

def phone_format(n):  # форматирование телефонного номера
    n = n.removeprefix("+")
    n = re.sub("[ ()-]", "", n)
    return format(int(n[:-1]), ",").replace(",", "-") + n[-1]

def print_data(fileName): # Функция вывода данных контакта
    with open(fileName,"r",encoding="utf-8") as file:
        phonebook_str = file.read()
        print(phonebook_str)
print()

def input_name():
    return input("Введите имя контакта: ").title()

def input_surname():
    return input("Введите фамилию контакта: ").title()
    
def input_patronymic():
    return input("Введите отчество контакта: ").title()

def input_phone():
    return input("Введите номер телефона контакта: ")
   
def input_address():
    return input("Введите адрес контакта: ").title()

def input_data():
    surname = input_surname()
    name = input_name()
    patronymic = input_patronymic()
    phone = input_phone()
    address = input_address()
    my_sep = ","
    return f"{surname}{my_sep}{name}{my_sep}{patronymic}{my_sep}{phone}{my_sep}{address}.\n"

def add_contact(fileName):
    new_contact_str = input_data()
    with open(fileName,"a",encoding="utf-8") as file:
        file.write(new_contact_str)
    print('\nКонтакт успешно записан!\n')


def printData(data):  # Функция вывода телефонной книги в консоль
    phoneBook = []
    splitLine = "=" * 95
    print(splitLine)
    print("  №  Фамилия         Имя             Отчество           Номер телефона         Город проживания")
    print(splitLine)
    personID = 1

    for contact in data:
        lastName, name, patronymic, phone, address = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "lastName": lastName,
                "name": name,
                "patronymic": patronymic,
                "phone": phone_format(phone),
                "address": address,
            }
        )
        personID += 1
    for contact in phoneBook:
        personID, lastName, name, patronymic, phone, address = contact.values()
        print(f"{personID:>3}. {lastName:<15} {name:<15} {patronymic:<15} -- {phone:<14} --      {address:<15}")

    print(splitLine)
    return

def showContacts(fileName):  # Функция открытия телефонной книги
    os.system("cls")
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
    

def search_contact(fileName):
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        phoneBook = []
        splitLine = "=" * 95
        print(splitLine)
        print("  №  Фамилия         Имя             Отчество           Номер телефона         Город проживания")
        print(splitLine)
        personID = 1

    for contact in data:
        lastName, name, patronymic, phone, address = contact.rstrip().split(",")
        phoneBook.append(
            {
                "ID": personID,
                "lastName": lastName,
                "name": name,
                "patronymic": patronymic,
                "phone": phone_format(phone),
                "address": address,
            }
        )
        personID += 1
    for contact in phoneBook:
        personID, lastName, name, patronymic, phone, address = contact.values()
        print(f"{personID:>3}. {lastName:<15} {name:<15} {patronymic:<15} -- {phone:<14} --      {address:<15}")

    print(splitLine)

    print("Выберите вариант поиска:\n"
        "1. По номеру (ID)\n"
        "2. По фамилии\n"
        "3. По имени\n"
        "4. По отчеству\n"
        "5. По городу проживания\n")
    
    print("0. Выход в основное меню\n")
    command = input("Выберите вариант поиска: ")

    while command not in ("1", "2", "3", "4","5","0"):
        print("Некорректный ввод, повторите запрос")
        command = input("Выберите вариант поиска:\n")  
     
    match command:
        case "1":
                with open(fileName, "r", encoding="UTF-8") as file:
                    data = sorted(file.readlines())
                    phoneBook = []
                    search = input("Введите значение №: ")
                    search = int(search)
                    splitLine = "=" * 95
                    print(splitLine)
                    print("  №  Фамилия         Имя             Отчество           Номер телефона         Город проживания")
                    print(splitLine)
                    personID = 1
                for contact in data:
                    lastName, name, patronymic, phone, address = contact.rstrip().split(",")
                    phoneBook.append(
                        {
                            "ID": personID,
                            "lastName": lastName,
                            "name": name,
                            "patronymic": patronymic,
                            "phone": phone_format(phone),
                            "address": address,
                        }
                    )
                    if search == personID:
                        print(f"{personID:>3}. {lastName:<15} {name:<15} {patronymic:<15} -- {phone:<14} --      {address:<15}") 
                    else: print ("Ошибка, такого номера нет")    
                    personID += 1
                input("\n--- Нажмите любую кнопку ---")         
        case "2":
                with open(fileName, "r", encoding="UTF-8") as file:
                    data = sorted(file.readlines())
                    phoneBook = []
                    search = input("Введите фамилию контакта: ")
                    search = str(search)
                    splitLine = "=" * 95
                    print(splitLine)
                    print("  №  Фамилия         Имя             Отчество           Номер телефона         Город проживания")
                    print(splitLine)
                    personID = 1
                for contact in data:
                    lastName, name, patronymic, phone, address = contact.rstrip().split(",")
                    phoneBook.append(
                        {
                            "ID": personID,
                            "lastName": lastName,
                            "name": name,
                            "patronymic": patronymic,
                            "phone": phone_format(phone),
                            "address": address,
                        }
                    )
                    if search == lastName:
                        print(f"{personID:>3}. {lastName:<15} {name:<15} {patronymic:<15} -- {phone:<14} --      {address:<15}") 
                    else: print ("Ошибка, такой фамилии нет")    
                    personID += 1
                input("\n--- Нажмите Enter ---")   
        case "3":
                with open(fileName, "r", encoding="UTF-8") as file:
                    data = sorted(file.readlines())
                    phoneBook = []
                    search = input("Введите имя контакта: ")
                    search = str(search)
                    splitLine = "=" * 95
                    print(splitLine)
                    print("  №  Фамилия         Имя             Отчество           Номер телефона         Город проживания")
                    print(splitLine)
                    personID = 1
                for contact in data:
                    lastName, name, patronymic, phone, address = contact.rstrip().split(",")
                    phoneBook.append(
                        {
                            "ID": personID,
                            "lastName": lastName,
                            "name": name,
                            "patronymic": patronymic,
                            "phone": phone_format(phone),
                            "address": address,
                        }
                    )
                    if search == name:
                        print(f"{personID:>3}. {lastName:<15} {name:<15} {patronymic:<15} -- {phone:<14} --      {address:<15}") 
                    else: print ("Ошибка, такого имени нет")    
                    personID += 1
                input("\n--- Нажмите Enter ---")  
        case "4":
                with open(fileName, "r", encoding="UTF-8") as file:
                    data = sorted(file.readlines())
                    phoneBook = []
                    search = input("Введите отчество контакта: ")
                    search = str(search)
                    splitLine = "=" * 95
                    print(splitLine)
                    print("  №  Фамилия         Имя             Отчество           Номер телефона         Город проживания")
                    print(splitLine)
                    personID = 1
                for contact in data:
                    lastName, name, patronymic, phone, address = contact.rstrip().split(",")
                    phoneBook.append(
                        {
                            "ID": personID,
                            "lastName": lastName,
                            "name": name,
                            "patronymic": patronymic,
                            "phone": phone_format(phone),
                            "address": address,
                        }
                    )
                    if search == patronymic:
                        print(f"{personID:>3}. {lastName:<15} {name:<15} {patronymic:<15} -- {phone:<14} --      {address:<15}") 
                    else: print ("Ошибка, такого отчества нет")    
                    personID += 1
                input("\n--- Нажмите Enter ---")  
        case "5":
                with open(fileName, "r", encoding="UTF-8") as file:
                    data = sorted(file.readlines())
                    phoneBook = []
                    search = input("Введите город проживания контакта: ")
                    search = str(search)
                    splitLine = "=" * 95
                    print(splitLine)
                    print("  №  Фамилия         Имя             Отчество           Номер телефона         Город проживания")
                    print(splitLine)
                    personID = 1
                for contact in data:
                    lastName, name, patronymic, phone, address = contact.rstrip().split(",")
                    phoneBook.append(
                        {
                            "ID": personID,
                            "lastName": lastName,
                            "name": name,
                            "patronymic": patronymic,
                            "phone": phone_format(phone),
                            "address": address,
                        }
                    )
                    if search == address:
                        print(f"{personID:>3}. {lastName:<15} {name:<15} {patronymic:<15} -- {phone:<14} --      {address:<15}") 
                    else: print ("Ошибка, такого города в списке нет")    
                    personID += 1
                input("\n--- Нажмите Enter ---")  
        case "6":
                print("Переход в основное меню")
                input("\n--- Нажмите Enter ---") 
    
def deleteContact(fileName):  # Функция удаления контакта из телефонной книги
    os.system("cls")
    with open(fileName, "r+", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(input("Введите номер контакта для удаления или 0 для перехода в основное меню: "))
        if numberContact != 0:
            confirmation = input(f"Вы желаете удалить контакт? {data[numberContact-1].rstrip().split(',')}  (y/n): ").lower()
            if confirmation == ("y"):
                print(f"Удалён контакт: {data[numberContact-1].rstrip().split(',')}\n")
                data.pop(numberContact - 1)
                with open(fileName, "w", encoding="UTF-8") as file:
                    file.write("".join(data))
            print ("Переход в основное меню")
        else: 
            print ("Переход в основное меню")
            return
        

def changeContact(fileName):  # Функция изменения информации в контакте
    os.system("cls")
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)

        numberContact = int(
            input("Введите неомер контакта, который хотите изменить или 0 для возврата в основное меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            newLastName = input("Введите фамилию нового контакта: ")
            newName = input("Введите имя нового контакта: ")
            newPatronymic = input("Введите отчество нового контакта: ")
            newPhone = input("Введите телефон нового контакта: ")
            newCity = input("Введите город проживания нового контакта: ")

            data[numberContact - 1] = (
                newLastName + "," + newName + ","+ newPatronymic + "," + newPhone + "," + newCity + "\n"
                )
            with open(fileName, "w", encoding="UTF-8") as file:
                file.write("".join(data))
                print("\nКонтакт заменен!")
                input("\n--- Нажмите Enter ---")
        else:
            return
def CopyInContactsInNewFile(fileName): # Функция копирования контактов в новый файл
    os.system("cls")
    with open(fileName, "r", encoding="UTF-8") as file:
        data = sorted(file.readlines())
        printData(data)
        numberContact = int(
            input("Введите неомер контакта, который хотите скопировать в новый файл или 0 для возврата в основное меню: ")
        )
        print(data[numberContact - 1].rstrip().split(","))
        if numberContact != 0:
            NewFile = input("Введите название нового файла: ")
            with open(f"{NewFile}.txt", "a", encoding="UTF-8") as file_new:
                file_new.write(data[numberContact - 1])
                print('\nКонтакт успешно записан в новый файл!\n')                

def interface(fileName): # Функция интерфейса главного меню
    with open(fileName,"a",encoding="utf-8"):
        pass 
    command = ""
    os.system("cls")
    while command !="0":
        
        print("====  Телефонный справочник ====")
        print("=" * 29)
        print("[1] -- Вывод данных на экран\n"
            "[2] -- Добавить контакт\n"
            "[3] -- Поиск контакта\n"
            "[4] -- Изменение контакта\n"
            "[5] -- Удаление контакта\n"
            "[6] -- Копирование контакта в новый файл\n\n")
        print("[0] -- Выход\n")
        print("=" * 29)
        command = input("Выберите пункт меню: ")

        while command not in ("0", "1", "2", "3", "4", "5", "6"):
            print("Некорректный ввод, повторите запрос")
            command = input("Выберите пункт меню: ")

        match command:
            case "1":
                showContacts(fileName)
            case "2":
                add_contact(fileName)
            case "3":
                search_contact(fileName)
            case "4":
                changeContact(fileName)
            case "5":
                deleteContact(fileName)
            case "0":
                print("Завершение программы")
            case "6":
                CopyInContactsInNewFile(fileName)
        print()


if __name__ == "__main__":
    interface(fileName)


