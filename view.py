import text


# Вывод основного меню
def main_menu() -> int:
    print(text.main_menu)
    while True:
        value = input(text.input_value)
        if value.isdigit() and 0 < int(value) < 7:
            return int(value)


# Вывод меню изменения заметки
def change_notes_menu() -> int:
    print(text.change_note_menu)
    while True:
        value = input(text.input_value)
        if value.isdigit() and 0 < int(value) < 4:
            return int(value)


# Вывод всех заметок
def print_notes_dict(notes_dict):
    if notes_dict:
        for value in notes_dict.values():
            for key, elem in value.items():
                print(key, ":", elem)
            print()
    else:
        print_message(text.notes_empty)


# Вывод вспомогательных сообщений
def print_message(message):
    print("\n" + "*" * len(message) + "\n")
    print(message)
    print("\n" + "*" * len(message) + "\n")
