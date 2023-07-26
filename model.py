from datetime import datetime
import text
import json


class Notes:
    def __init__(self):
        self.path = text.file_path

    # Метод для получения списка заметок из файла
    def get_notes_dict(self):
        with open(self.path, "r", encoding="UTF-8") as data:
            line = data.readline()
            # Если файл не пустой, то мы парсим из json в словарь, иначе создаем пустой словарь
            if line != "":
                self.notes = json.loads(line)
            else:
                self.notes = {}

        return self.notes

    # Метод добавления новой заметки
    def add_note(self):
        keys_list = (
            []
        )  # keys_list нужен для хранения уже имеющихся в заметках ключей(id)
        new_dict = (
            {}
        )  # в new_dict будут записаны занчения "header", "body" и "datetime" новой заметки
        header = input(text.new_header)
        body = input(text.new_body)
        current_datetime = datetime.now()  # Текущее время создания новой заметки
        new_dict["header"] = header
        new_dict["body"] = body
        new_dict["datetime"] = str(
            current_datetime
        )  # кастуем в строку для отображения в виде yyyy-mm-dd hh:mm:ss.ms

        for key in self.notes.keys():
            keys_list.append(
                int(key)
            )  # Заполняем key_list ключами исходного словаря с заметками, предварительно кастую в int, т.к. в исходнике это строки
        index = max(keys_list)  # Находим max
        self.notes[
            index + 1
        ] = new_dict  # Добавляем в исходный словарь под следующим свободным ключем значение в виде словаря new_dict
        print(self.notes)

    # Метод поиска заметок
    def search_notes(self):
        search_data = input(text.search_info).lower()
        search_dict = {}  # Сюда складываем найденное

        for key, elem in self.notes.items():
            for elm in elem.values():
                if search_data in elm.lower():  # Проверка на совпадение
                    search_dict[
                        key
                    ] = elem  # Кладем в словарь для поиска ключ исходного словаря и соответствующее ему значение

        return search_dict

    # Метод сохрания заметок в файл
    def save_note(self):
        jsonData = json.dumps(self.notes)  # Парсим словарь в json

        with open(self.path, "w", encoding="UTF-8") as file:
            file.write(jsonData)

    # Метод изменеия заметки, принимает:
    # search_notes_dict - словарь от результата поиска метода search_notes
    # input_value - значение, указанное пользователем
    def change_note(self, search_notes_dict, input_value):
        new_data = input(text.new_data)

        # В зависимости от выбранного значения меняем "header" или "body"
        if input_value == 1:
            for elem in search_notes_dict.values():
                elem["header"] = new_data
                elem["datetime"] = str(datetime.now())
        else:
            for elem in search_notes_dict.values():
                elem["body"] = new_data
                elem["datetime"] = str(datetime.now())

        self.notes.update(search_notes_dict)  # Вносим изменения в основной словарь

    # Метод удаления заметки, принимает:
    # search_dict - словарь от результата поиска метода search_notes

    def del_note(self, search_dict):
        key = list(
            search_dict
        )  # Список с ключами для удаления (настроено так, что в списке может оказаться только 1 элемент)
        self.notes.pop(key[0])
