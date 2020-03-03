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


def notebook__test():
    noteb = notebook.Notebook()
    note1 = noteb.new_note("Hello, world!", "hello")
    print("Unmodified first note: ", note1.memo)
    noteb.modify_memo(note1.id, "La de dah day!")
    noteb.modify_tags(note1.id, 'day')
    print("First note modified using 'modify_memo' method: ", note1.memo)

    note2 = noteb.new_note("Hello, world!", "hello")
    note3 = noteb.new_note('Hello, heyyy!!', "hey hello")
    print("Second note: ", note2.memo)

    print("Does the 'Hello, world!' note  match 'hello'?")
    print(note2.match("hello"))
    print("Does the 'Heyyy!!' note  match 'hey'?")
    print(note3.match("hey"))
    print("Does the 'Heyyy!!' note  match 'bla'?")
    print(note3.match("bla"))
    print("All of the notes that include 'hello': ")
    for i in noteb.search('hello'):
        print(i.memo)


if __name__ == "__main__":
    main()
    notebook__test()