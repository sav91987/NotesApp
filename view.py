import text


def main_menu() -> int:
    print(text.main_menu)
    while True:
        value = input(text.input_value)
        if value.isdigit() and 0 < int(value) < 7:
            return int(value)
        

        
def change_contact_menu() -> int:
    print(text.change_contact_menu)
    while True:
        value = input(text.input_value)
        if value.isdigit() and 0 < int(value)< 4:
            return int(value)
        

        
def print_contact_list(contact_list):
    if contact_list:
        for value in contact_list.values():
            for key, elem in value.items():
                print(key, ":", elem)
            print()
    else: print_message(text.phone_book_empty)


def print_message(message):
    print('\n'+ '*'*len(message) + '\n')
    print(message)
    print('\n' + '*'*len(message) + '\n')