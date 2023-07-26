from datetime import datetime
import text
import json


class PhoneBook:

    def __init__(self):
        self.path = text.file_path

    def get_contact_list(self):
        with open(self.path, 'r', encoding='UTF-8') as data:
            #for contact in data:
            contact = data.readline()
            if contact != '':
                self.phone_book = json.loads(contact)
            else:
                self.phone_book = {}
        # for i in range(len(my_list)):
        #     my_list[i] = tuple(my_list[i].strip().split(','))
        #     self.phone_book.append(my_list[i])
        return self.phone_book

    def add_contact(self):
        keys_list = []
        new_dict = {}
        header = input(text.new_header)
        body = input(text.new_body)
        current_datetime = datetime.now()
        new_dict["header"] = header
        new_dict["body"] = body
        new_dict["datetime"] = str (current_datetime)
        print(new_dict)

        for key in self.phone_book.keys():
            keys_list.append(int(key))
        index = max(keys_list)
        self.phone_book[index+1] = new_dict
        print(self.phone_book)

    def search_contact(self):
        search_data = input(text.search_info).lower()
        search_dict = {}
        #index_list = []
        for key, elem in self.phone_book.items():
            for elm in elem.values():
                if search_data in elm.lower():
                    search_dict[key] = elem
                    #index_list.append(elem)
        return search_dict #, index_list

    def save_contact(self):
        jsonData = json.dumps(self.phone_book)
        
        with open(self.path, 'w', encoding='UTF-8') as file:
            file.write(jsonData)

    def change_contact(self, search_contact_list, input_value):
        new_data = input(text.new_data)
        if input_value == 1:
            for elem in search_contact_list.values():
                elem["header"] = new_data
                elem["datetime"] = str (datetime.now())
                #changed_contact = (new_data, elem[1])
        else:
            for elem in search_contact_list.values():
                elem["body"] = new_data
                elem["datetime"] = str (datetime.now())
                #changed_contact = (elem[0], new_data)
        # needed_key = search_contact_list.setdefault()
        # print(needed_key)
        # self.phone_book.pop(needed_key)
        self.phone_book.update(search_contact_list)
        

    def del_contact(self, search_dict):
        key = list(search_dict)
        
        self.phone_book.pop(key[0])
