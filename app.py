import ui
def run():
    while True:
        print("\nMINI LIBRARY MANAGEMENT SYSTEM")
        print("1. Add Book")
        print("2. Display Books")
        print("3. Search Book")
        print("4. Issue Book")
        print("5. Return Book")
        print("6. Exit")
        choice = input("Enter your choice: ")
         if choice == "1":
            ui.add_book()
        elif choice == "2":
            ui.display_books()
        elif choice == "3":
            ui.search_book()
        elif choice == "4":
            ui.issue_book()
        elif choice == "5":
            ui.return_book()
        elif choice == "6":
            print("Thank you for using Library Management System!")
            break
        else:
            print("Invalid choice. Please try again.")
