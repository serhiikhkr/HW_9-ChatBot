

END_COMMAND = ['good bye', 'close', 'exit']

contacts = {}
def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return "Give me name of function, name and phone please"
        except KeyError:
            return "Try again. Please give me correct name"

    return inner

@input_error
def parsing_input(raw_string: str):
    parts_of_input = raw_string.strip().split()
    return parts_of_input

@input_error
def add_func(str_list: list):
    contacts[str_list[1].title()] = str_list[2]

@input_error
def change_func(str_list: list):
    if str_list[1].title() not in contacts.keys():
        raise KeyError
    else:
        contacts[str_list[1].title()] = str_list[2]

@input_error
def show_phone_number(str_list: list):
    return contacts[str_list[1].title()]

@input_error
def show_all():
    output_contacts = ''
    if len(contacts) == 0:
        return 'List of contacts is empty'
    for name, phone in contacts.items():
        output_contacts = output_contacts + f'{name}: {phone}\n'

    return output_contacts

COMMAND_CHAT = {'add': add_func,
                'change': change_func,
                'phone': show_phone_number,
                'show all': show_all}

def main():
    flag_start_chat = True
    while flag_start_chat:
        user_message = input(">>>")
        if user_message.strip().lower() == 'hello':
            print('How can i help you?')
        elif user_message.strip().lower() in END_COMMAND:
            print('Good bye')
            flag_start_chat = False
        list_input_elements = parsing_input(user_message)
        if list_input_elements:
            if list_input_elements[0] == 'phone':
                result = COMMAND_CHAT[list_input_elements[0]](list_input_elements)
                print(result)
            elif list_input_elements[0] == 'show' and list_input_elements[1] == 'all':
                result = COMMAND_CHAT['show all']()
                print(result)
            else:
                result = COMMAND_CHAT[list_input_elements[0]](list_input_elements)
                if result == None:
                    print('Done')
                else:
                    print(result)


if __name__ == "__main__":
    main()