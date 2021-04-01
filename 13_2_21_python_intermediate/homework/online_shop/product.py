class Product:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price
        self.categories = []

    def add_category(self, category):
        if len(category) < 2 and not isinstance(category, str):
            raise ValueError("Category must be a string with at least 2 charachters.")
        if category not in self.categories:
            self.categories.append(category)

    def __hash__(self):
        return hash(self.name)

    def name_to_url(self):
        lower_name = ''.join([ch.lower() for ch in self.name])
        diacritics_removed = ""
        for ch in lower_name:
            if ch in ['ă', 'â']:
                diacritics_removed += 'a'
            elif ch == 'î':
                diacritics_removed += 'i'
            elif ch == 'ț':
                diacritics_removed += 't'
            elif ch == 'ș':
                diacritics_removed += 's'
            else:
                diacritics_removed += ch
        spaces_removed = '-'.join(diacritics_removed.split())
        not_allowed_characters = ['„', '<', '>', '#', '%', '{', '}', '\\', '|', '^', '[', ']', '`', '!', '$', '%', '\'',
                                  '(', ')', '*', '+', ',', '/', ':', ';', '=', '?', '@']
        for ch in spaces_removed:
            if ch in not_allowed_characters:
                spaces_removed.replace(ch, "")
        return spaces_removed

class Laptop(Product):
    def __init__(self, name, description, price):
        Product.__init__(name, description, price)

    @property
    def cpu(self):





ideapad_slim_7 = Product('Lenovo Ideapad Slim 7',
                         'Laptop Lenovo Yoga Slim 7 14ARE05 cu procesor AMD Ryzen™ 7 4700U, 14" Full HD, 16GB, 512GB SSD, AMD Radeon™ Graphics, Windows 10 Home, Slate Grey',
                         4299)

print(ideapad_slim_7.name_to_url())
