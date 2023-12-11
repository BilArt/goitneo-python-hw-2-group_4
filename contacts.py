def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    # Додає новий контакт до словника
    if len(args) == 2:
        name, phone = args
        contacts[name] = phone
        return "Contact added."
    else:
        return "Invalid command. Use 'add [name] [phone]'."


def change_contact(args, contacts):
    # Змінює номер телефону для існуючого контакту
    if len(args) == 2:
        name, new_phone = args
        if name in contacts:
            contacts[name] = new_phone
            return "Contact updated."
        else:
            return "Contact not found."
    else:
        return "Invalid command. Use 'change [name] [new_phone]'."


def show_phone(args, contacts):
    # Показує номер телефону для зазначеного контакту
    if len(args) == 1:
        name = args[0]
        if name in contacts:
            return contacts[name]
        else:
            return "Contact not found."
    else:
        return "Invalid command. Use 'phone [name]'."


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
