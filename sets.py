#1
friday = {"Alice", "Bob", "Charlie"}
saturday = {"Charlie", "David","Eve"}
all_guests=friday.union(saturday)
print(f"Person attending all nights are{all_guests}")
all_nights=friday.intersection(saturday)
print(f"The person attending both nights is {all_nights}")
#2
data = [1, 2, 2, 3, 4, 4, 4, 5]
data=set(data)
data.add(6)
print(data)
#3
library_books = {"Hobbit", "1984", "Gatsby", "Odyssey", "Hamlet"}
checked_out = {"1984", "Hamlet"}
books_sitting=library_books-checked_out
print(books_sitting)
if "Don Quixote" not in library_books:
    library_books.add("Don Quixote")
print(library_books)
#4
user_permissions={"read", "write"}
admin_reqs={"read", "write", "execute"}
if admin_reqs.issubset(user_permissions):
    print("the user has all the permissions required for admin access")
else:
    print(f"{str(admin_reqs-user_permissions)} are missing")
#5
logs = {
    "404": [10, 12, 15, 20],
    "500": [12, 20, 22, 25],
    "403": [10, 20, 30]
}
new_set={k for k in logs["404"] if k in logs["500"] and  k in logs["403"]}
print(f"Server IDs that experienced every type of error :{new_set}")
critical_servers={k for k in logs["500"] if k not in logs["404"]}
print(f"servers that experienced a 500 error but never experienced 404 error:{critical_servers}")
