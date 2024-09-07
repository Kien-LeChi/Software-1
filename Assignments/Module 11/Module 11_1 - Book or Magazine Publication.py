class Publication :

    def __init__(self, name):
        self._name = name


class Book (Publication) :

    def __init__(self, name, author, page_cnt):
        Publication.__init__(self, name)
        self._author = author
        self._page_cnt = page_cnt

    def print_information(self):
        print(f"Publication's type: Book\n"
              f"Book's name: {self._name}\n"
              f"Author: {self._author}\n"
              f"No. Page: {self._page_cnt}\n")


class Magazine (Publication) :

    def __init__(self, name, chief_editor):
        Publication.__init__(self, name)
        self._chief_editor = chief_editor

    def print_information(self):
        print(f"Publication's type: Magazine\n"
              f"Magazine's name: {self._name}\n"
              f"Chief editor: {self._chief_editor}\n")

publication1 = Magazine("Donald Duck", "Aki Hyyppa")
publication2 = Book("Compartment No. 6", "Rosa Liksom", 192)

publication1.print_information()
publication2.print_information()