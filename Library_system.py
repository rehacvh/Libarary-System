# step1 :Define data structures
books = {
    "9780316769488": {"title": "The Catcher in the Rye", "author": "J.D. Salinger", "is_borrowed": False},
    "9780061120084": {"title": "To Kill a Mockingbird", "author": "Harper Lee", "is_borrowed": False}
}

#step 2 membership 
members = {
    "M1001": {"name": "Ahmed", "borrowed_books": []},
    "M1002": {"name": "Mohamed", "borrowed_books": []}
}

# step3 : Define function for add book 
def add_book(isbn, title, author):
    if isbn not in books:
        books[isbn] = {"title": title, "author": author, "is_borrowed": False}
    else:
        print("Book already exists.")


# step4 : Define function for add member 
def add_member(member_id, name):
    if member_id not in members:
        members[member_id] = {"name": name, "borrowed_books": []}
    else:
        print("Member already exists.")

# step5 : Define function for borrow book
def borrow_book(member_id, isbn):
    if member_id in members and isbn in books:
        book = books[isbn]
        member = members[member_id]
        if not book["is_borrowed"]:
            book["is_borrowed"] = True
            member["borrowed_books"].append(isbn)
        else:
            print("The book is already borrowed.")
    else:
        print("Invalid member ID or book ISBN.")


# step6 : Define function for return book
def return_book(member_id, isbn):
    if member_id in members and isbn in books:
        book = books[isbn]
        member = members[member_id]
        if isbn in member["borrowed_books"]:
            book["is_borrowed"] = False
            member["borrowed_books"].remove(isbn)
        else:
            print("The book is not borrowed by this member.")
    else:
        print("Invalid member ID or book ISBN.")

def display_books():
    for isbn, details in books.items():
        print(f"ISBN: {isbn}, Title: {details['title']}, Author: {details['author']}, Borrowed: {details['is_borrowed']}")

def display_members():
    for member_id, details in members.items():
        print(f"Member ID: {member_id}, Name: {details['name']}, Borrowed Books: {details['borrowed_books']}")

# Step 9: Define main function to run the library system
def main():
    while True:
        print("\nWelcome to the Library Management System")
        print("1. Add a Book")
        print("2. Add a Member")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Display all Books")
        print("6. Display all Members")
        print("7. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == "1":
            isbn = input("Enter ISBN of the book: ")
            title = input("Enter title of the book: ")
            author = input("Enter author of the book: ")
            add_book(isbn, title, author)
        
        elif choice == "2":
            member_id = input("Enter Member ID: ")
            name = input("Enter name of the member: ")
            add_member(member_id, name)
        
        elif choice == "3":
            member_id = input("Enter Member ID: ")
            isbn = input("Enter ISBN of the book to borrow: ")
            borrow_book(member_id, isbn)
        
        elif choice == "4":
            member_id = input("Enter Member ID: ")
            isbn = input("Enter ISBN of the book to return: ")
            return_book(member_id, isbn)
        
        elif choice == "5":
            display_books()
        
        elif choice == "6":
            display_members()
        
        elif choice == "7":
            print("Thank you for using the Library Management System.")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")

# Run the main function
if __name__ == "__main__":
    main()
