class Krator:
    def __init__(self):
        self.name = 'железо'
        self.value = 15
class Inventory:
    def __init__(self):
        self.items = [{'name': 'железо', 'value': 10},
                      {'name': 'золото', 'value': 200},
                      {'name': 'медь', 'value': 50},
                      {'name': 'серебро', 'value': 15},
                      {'name': 'германий', 'value': 5}, ]
    def add_items(self,krator):

        self.dict = {}
        for i in self.items:
            if i['name'] == krator.name:
                i['value'] += krator.value






if __name__ == '__main__':
    krator = Krator()
    inventery = Inventory()
    print(inventery.items)
    inventery.add_items(krator)
    print(inventery.items)
