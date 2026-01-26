from json import dump,load
def save_settings(data, file_name='Save.json'):
    with open(file_name, 'w', encoding='UTF-8') as file:
        dump(data, file)
    file.close()
def load_settings(file_name='Save.json'):
    with open(file_name, 'r', encoding='UTF-8') as file:
        data = load(file)
    file.close()
    return data