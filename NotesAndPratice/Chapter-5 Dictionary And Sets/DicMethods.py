Book = {
  "first" : 90,
  "second" : 80,
  "third" : 20

}

#print(Book.items())
#print(Book.keys())
#print(Book.values())

#Book.update({"first":99,"Amit":100})


#print(Book.get("first"))
#print(Book["first"])


#Book.clear()

value = Book.popitem()

print(value)

print(Book)