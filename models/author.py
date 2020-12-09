class Author:
    def __init__(self, name, id = None):
        self.name = name
        self.id = id

    def name(self):
        return f"{self.name}"
