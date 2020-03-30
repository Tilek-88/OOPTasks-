class Contactlist:
    def __init__(self, names):
        self.names = names

    def search_by_name(self, search):
        for name in self.names:
            if name == search:
                print(name)

    
all_contacts = Contactlist(['Usa', 'John', 'Kuba', 'Sadyk', 'John'])
all_contacts.search_by_name("John")
     

