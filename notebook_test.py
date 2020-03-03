import notebook


def main():
    note = notebook.Note("Hello, world!", "hello")
    noteb = notebook.Notebook()
    print("Is variable 'note'(notebook.Note('Hello, world!', 'hello')) a Note object? ",
          isinstance(note, notebook.Note))
    print()
    print("Is variable 'noteb'(notebook.Notebook()) a Notebook object? ", isinstance(note, notebook.Note))
    print()
    print("Class Note attributes and methods: ")
    print(note.__dir__())
    print()
    print("List of attributes of Note Class: ")
    print(list(note.__dict__.keys()))
    print()
    print("Class Notebook attributes and methods: ")
    print(noteb.__dir__())
    print()
    print("List of attributes of Notebook Class: ")
    print(list(noteb.__dict__.keys()))
    print()
    print("Note object's method .__str__ when printed represents an object's place in memory.")
    print(note.__str__())
    print()
    print("Notebook object's method .__str__ when printed represents an object's place in memory.")
    print(noteb.__str__())
    print()
    print("This is an .__init__ method of Note class and it creates an object, but it does not return anything")
    print(note.__init__("hello world", "this is a tag"))


if __name__ == "__main__":
    main()
