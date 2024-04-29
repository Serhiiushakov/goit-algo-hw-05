def input_error(func):
     #Декоратор для обробки помилок введення користувача
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "Invalid command. Contact not found."
        except IndexError:
            return "Invalid command. Usage: command username phone"
        except Exception as e:
            return f"An error occurred: {str(e)}"
    return inner

def parse_input(user_input):
#Розбирає введений користувачем рядок на команду та аргументи
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

@input_error
def add_contact(args, contacts):
#Додає новий контакт до словника контактів
    if len(args) != 2:
        raise IndexError
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact(args, contacts):
#Змінює номер телефону для існуючого контакту
    if len(args) != 2:
        raise IndexError
    name, phone = args
    if name not in contacts:
        raise KeyError
    contacts[name] = phone
    return "Contact updated."

@input_error
def show_phone(args, contacts):
    #Показує номер телефону для зазначеного контакту.
    if len(args) != 1:
        raise IndexError
    name = args[0]
    if name not in contacts:
        raise KeyError
    return f"The phone number for {name} is {contacts[name]}."

@input_error
def show_all(contacts):
  #  Виводить всі збережені контакти з номерами телефонів.
    if not contacts:
        raise ValueError("No contacts found.")
    result = "Contacts:\n"
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()

def main():
    # функція бота (питання-відповідь)
    contacts = {}
    while True:
        user_input = input("Enter command: ").strip().lower()
        command, args = parse_input(user_input)
        
        if command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "close" or command == "exit":
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
# Команди:
#  Hello  -> How can I help you?
# add [ім'я] [номер телефону] = add Serhii 0979104392, add Ira 097170416
#add Ira Serhii - > Invalid command. Usage: add username phone
# add Serhii 0979104392 - > Invalid command. Usage: add username phone
# 380979104392 - > Invalid command.
# change [ім'я] [новий номер телефону] = change Serhii 1239104392
#"phone [ім'я]"  phone Serhii
#phone Anna -> Invalid command. Contact not found.
#"all"
# "close" або "exit"
