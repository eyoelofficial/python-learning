def book_profile(title, author, page):
    return {"title": title, "author": author, "page": page}
book = book_profile("unknown", "unknown", 0)
while True:
    print(" menu")
    print("1. View book ")
    print("2. Edit title ")
    print("3. Edit author ")
    print("4. Edit pages ")
    print("5. Show formatted profile ")
    print("6. Exit")
    menu = input(": ")
    if menu == "1":
        print(book)    
    if menu == "2":
        book["title"] = input("Enter new title: ")
    if menu == "3":
        book["author"] = input("Enter new author: ")
    if menu == "4":
        book["page"] = int(input("Enter new page count: "))
    if menu == "5":
        print(f"title: {book["title"]}, author: {book["author"]}, page: {book["page"]}")
    if menu == "6":
        break