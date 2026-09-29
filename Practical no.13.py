library = {
    "978-0135166307": {
        "title": "Core Python Programming",
        "author": "Wesley J. Chun",
        "year": 2018,
        "available": True
    },
    "978-0596517748": {
        "title": "Programming Python",
        "author": "Mark Lutz",
        "year": 2011,
        "available": False
    }
}
running = True
while running:
    print("\n--- LIBRARY BOOK RECORD SYSTEM ---")
    print("1. Display All Books")
    print("2. Search Book by ISBN")
    print("3. Add New Book")
    print("4. Update Book Availability")
    print("5. Delete Book Record")
    print("6. Exit")
    choice = input("Enter your choice (1-6): ").strip()
    if choice == '1':
        if not library:
            print("\nNo books found in the record.")
        else:
            print("\n" + "=" * 70)
            for isbn, info in library.items():
                if info['available']:
                    status = "Available"
                else:
                    status = "Checked Out"
                print("ISBN:", isbn)
                print("Title:", info['title'], "| Author:", info['author'])
                print("Year:", info['year'], "| Status:", status)
                print("-" * 70)
    elif choice == '2':
        isbn = input("Enter ISBN to search: ").strip()
        book = library.get(isbn)
        if book != None:
            if book['available']:
                status = "Available"
            else:
                status = "Checked Out"
            print("\nBook Found!")
            print("Title:", book['title'])
            print("Author:", book['author'])
            print("Year:", book['year'])
            print("Status:", status)
        else:
            print("\nError: Book not found for the given ISBN.")
    elif choice == '3':
        isbn = input("Enter new ISBN: ").strip()
        if isbn in library:
            print("\nError: ISBN already exists in the records!")
        else:
            title = input("Enter Book Title: ").strip()
            author = input("Enter Author Name: ").strip()
            year = int(input("Enter Publication Year: ").strip())
            library[isbn] = {
                "title": title,
                "author": author,
                "year": year,
                "available": True
            }
            print("\nBook added successfully.")
    elif choice == '4':
        isbn = input("Enter ISBN to update availability: ").strip()
        if isbn in library:
            status_input = input(
                "Is the book available? (yes/no): "
            ).strip().lower()
            if status_input == 'yes':
                library[isbn]['available'] = True
            else:
                library[isbn]['available'] = False
            print("\nBook availability updated successfully.")
        else:
            print("\nError: ISBN not found.")
    elif choice == '5':
        isbn = input("Enter ISBN to delete: ").strip()
        removed = library.pop(isbn, None)
        if removed != None:
            print("\nRemoved book from library records.")
        else:
            print("\nError: ISBN not found.")
    elif choice == '6':
        print("\nExiting system. Goodbye!")
        running = False
    else:
        print("\nInvalid choice! Please select 1 to 6.")
