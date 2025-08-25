book.delete()  

# Confirm deletion by retrieving all books
print(list(Book.objects.all()))
