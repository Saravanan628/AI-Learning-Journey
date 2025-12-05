class Library:
    def __init__(self,books):
        self.books=books
    def addbooks(self,newbook):
        self.books.append(newbook)
        print(self.books)
        return f"{newbook} is added to the library"

    def removebooks(self,existingbook):
        self.books.remove(existingbook)
        print(self.books)
        return f"{existingbook} is given for reading"

l1=Library(["Atomic habits","20 hours of learning","how to influence others"])
print(l1.addbooks("Networking"))
print(l1.removebooks("Atomic habits"))
