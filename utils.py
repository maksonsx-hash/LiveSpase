import json
def save_settings(data):
    with open('Save.json', 'w', encoding='UTF-8') as file:
        json.dump(data, file)