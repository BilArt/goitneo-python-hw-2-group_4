def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def input_error(func):
    #Декоратор для обробки винятків та повернення відповідних повідомлень користувачеві
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            return f"Error: {e}"
        except KeyError:
            return "Enter user name."
        except IndexError:
            return "Invalid command. Please enter a valid command."
        
    return inner


@input_error
def add_contact(args, contacts):
    # Додає новий контакт до словника
    if len(args) == 2:
        name, phone = args

        if not phone.isdigit():
            raise ValueError("Phone must be a numeric value.")
        

        contacts[name] = phone
        return "Contact added."
    else:
        return ValueError("Give me name and phone please.")


@input_error
def change_contact(args, contacts):
    # Змінює номер телефону для існуючого контакту
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            raise KeyError("Enter user name.")
    else:
        return ValueError("Give me name and phone please.")


@input_error
def show_phone(args, contacts):
    # Показує номер телефону для зазначеного контакту
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return KeyError("Enter user name.")
    else:
        return ValueError("Give me phone number please.")


def show_all(contacts):
    # Показує усі збережені контакти з номерами телефонів
    for name, phone in contacts.items():
        print(f"{name}: {phone}")


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command in ["hello", "hi"]:
            print("////////////////////////////////////////////////////////////////////////")
            print("How can I help you?")
            print("choose a command:")
            print("add - add a contact 'add [name] [phone]'")
            print("change - change a contact 'change [name] [new_phone]'")
            print("phone - show contact's telephone number 'phone [name]'")
            print("all - show all contacts")
        elif command in ["help", "commands"]:
            print("////////////////////////////////////////////////////////////////////////")
            print("How can I help you?")
            print("choose a command:")
            print("add - add a contact 'add [name] [phone]'")
            print("change - change a contact 'change [name] [new_phone]'")
            print("phone - show contact's telephone number 'phone [name]'")
            print("all - show all contacts")
        elif command == "add":
            result = add_contact(args, contacts)
            print("////////////////////////////////////////////////////////////////////////")
            print(result)
        elif command == "change":
            result = change_contact(args, contacts)
            print("////////////////////////////////////////////////////////////////////////")
            print(result)
        elif command == "phone":
            result = show_phone(args, contacts)
            print("////////////////////////////////////////////////////////////////////////")
            print(result)
        elif command == "all":
            print("////////////////////////////////////////////////////////////////////////")
            print("Contacts list:")
            show_all(contacts)
        else:
            print("Invalid command. Please enter a valid command.")

if __name__ == "__main__":
    main()
