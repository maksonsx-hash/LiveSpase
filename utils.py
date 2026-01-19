from json import dump,load
def save_settings(data):
    with open('Save.json', 'w', encoding='UTF-8') as file:
        dump(data, file)
def load_settings():
    with open('Save.json', 'r', encoding='UTF-8') as file:
        data = load(file)
        return data