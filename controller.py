import view
import model
import text

my_notes = model.Notes()


def start():
    notes = my_notes.get_notes_dict()
    while True:
        value = view.main_menu()
        match value:
            case 1:
                view.print_notes_dict(notes)
                view.print_message(text.succsesful_message)
            case 2:
                my_notes.add_note()
                my_notes.save_note()
                view.print_message(text.succsesful_message)
            case 3:
                search_dict = my_notes.search_notes()
                if len(search_dict) != 0:
                    view.print_notes_dict(search_dict)
                    view.print_message(text.succsesful_message)
                else:
                    view.print_message(text.search_fall)
            case 4:
                search_dict = my_notes.search_notes()
                flag = 1
                while flag:
                    if len(search_dict) > 1:
                        view.print_notes_dict(search_dict)
                        view.print_message(text.search_message)
                        search_dict = my_notes.search_notes()
                    elif len(search_dict) == 0:
                        view.print_message(text.search_fall)
                        search_dict = my_notes.search_notes()
                    else:
                        view.print_notes_dict(search_dict)
                        while flag:
                            input_value = view.change_notes_menu()
                            match input_value:
                                case 1:
                                    my_notes.change_note(search_dict, input_value)
                                    my_notes.save_note()
                                    view.print_message(text.succsesful_message)
                                case 2:
                                    my_notes.change_note(search_dict, input_value)
                                    my_notes.save_note()
                                    view.print_message(text.succsesful_message)
                                case 3:
                                    view.print_message(text.succsesful_message)
                                    flag = 0
            case 5:
                search_dict = my_notes.search_notes()
                flag = 1
                while flag:
                    if len(search_dict) > 1:
                        view.print_notes_dict(search_dict)
                        view.print_message(text.search_message)
                        search_dict = my_notes.search_notes()
                    elif len(search_dict) == 0:
                        view.print_message(text.search_fall)
                        search_dict = my_notes.search_notes()
                    else:
                        view.print_notes_dict(search_dict)
                        my_notes.del_note(search_dict)
                        my_notes.save_note()
                        view.print_message(text.succsesful_message)

                        flag = 0
            case 6:
                view.print_message(text.bye_message)
                exit()
