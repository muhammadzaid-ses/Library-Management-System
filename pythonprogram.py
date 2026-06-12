class Book:
    def __init__(self, book_id, title, author, total_copies):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.total_copies = total_copies
        self.available_copies = total_copies

    def borrow(self):
        if self.available_copies > 0:
            self.available_copies -= 1
            return True
        return False

    def return_book(self):
        if self.available_copies < self.total_copies:
            self.available_copies += 1
            return True
        return False

    def display(self):
        print(f"Book ID: {self.book_id}")
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Total Copies: {self.total_copies}")
        print(f"Available Copies: {self.available_copies}")
        print()


class Member:
    def __init__(self, member_id, name, department):
        self.member_id = member_id
        self.name = name
        self.department = department
        self.borrowed_books = []

    def borrow_book(self, book_id):
        if len(self.borrowed_books) < 3:
            self.borrowed_books.append(book_id)
            return True
        return False

    def return_book(self, book_id):
        if book_id in self.borrowed_books:
            self.borrowed_books.remove(book_id)
            return True
        return False

    def display(self):
        print(f"Member ID: {self.member_id}")
        print(f"Name: {self.name}")
        print(f"Department: {self.department}")

        if len(self.borrowed_books) == 0:
            print("Borrowed Books: None")
        else:
            print("Borrowed Books:", *self.borrowed_books)

        print()


class BorrowRecord:
    def __init__(self, member_id, book_id):
        self.member_id = member_id
        self.book_id = book_id

    def display(self):
        print(f"Member ID: {self.member_id}")
        print(f"Book ID: {self.book_id}")
        print()


class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.borrow_records = []

    def add_book(self):
        book_id = int(input("Enter Book ID: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        copies = int(input("Enter Total Copies: "))

        self.books.append(Book(book_id, title, author, copies))
        print("Book Added Successfully.\n")

    def remove_book(self):
        book_id = int(input("Enter Book ID to Remove: "))

        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print("Book Removed Successfully.\n")
                return

        print("Book Not Found.\n")

    def search_book(self):
        book_id = int(input("Enter Book ID: "))

        for book in self.books:
            if book.book_id == book_id:
                book.display()
                return

        print("Book Not Found.\n")

    def display_books(self):
        if len(self.books) == 0:
            print("No Books Available.\n")
            return

        for book in self.books:
            book.display()

    def register_member(self):
        member_id = int(input("Enter Member ID: "))
        name = input("Enter Name: ")
        department = input("Enter Department: ")

        self.members.append(Member(member_id, name, department))
        print("Member Registered Successfully.\n")

    def remove_member(self):
        member_id = int(input("Enter Member ID to Remove: "))

        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print("Member Removed Successfully.\n")
                return

        print("Member Not Found.\n")

    def search_member(self):
        member_id = int(input("Enter Member ID: "))

        for member in self.members:
            if member.member_id == member_id:
                member.display()
                return

        print("Member Not Found.\n")

    def display_members(self):
        if len(self.members) == 0:
            print("No Members Registered.\n")
            return

        for member in self.members:
            member.display()

    def borrow_book(self):
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if member is None:
            print("Member Not Found.\n")
            return

        if book is None:
            print("Book Not Found.\n")
            return

        if member.borrow_book(book_id) and book.borrow():
            self.borrow_records.append(BorrowRecord(member_id, book_id))
            print("Book Borrowed Successfully.\n")
        else:
            print("Borrowing Failed.\n")

    def return_book(self):
        member_id = int(input("Enter Member ID: "))
        book_id = int(input("Enter Book ID: "))

        member = None
        book = None

        for m in self.members:
            if m.member_id == member_id:
                member = m
                break

        for b in self.books:
            if b.book_id == book_id:
                book = b
                break

        if member is None or book is None:
            print("Member or Book Not Found.\n")
            return

        if member.return_book(book_id) and book.return_book():

            for record in self.borrow_records:
                if record.member_id == member_id and record.book_id == book_id:
                    self.borrow_records.remove(record)
                    break

            print("Book Returned Successfully.\n")
        else:
            print("Return Failed.\n")

    def display_borrow_records(self):
        if len(self.borrow_records) == 0:
            print("No Borrow Records.\n")
            return

        for record in self.borrow_records:
            record.display()

    def display_unavailable_books(self):
        found = False

        for book in self.books:
            if book.available_copies == 0:
                book.display()
                found = True

        if not found:
            print("No Unavailable Books.\n")

    def display_active_members(self):
        found = False

        for member in self.members:
            if len(member.borrowed_books) > 0:
                member.display()
                found = True

        if not found:
            print("No Active Members.\n")


class Menu:
    def __init__(self):
        self.library = Library()

    def display_menu(self):
        print("===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. Display Books")
        print("5. Register Member")
        print("6. Remove Member")
        print("7. Search Member")
        print("8. Display Members")
        print("9. Borrow Book")
        print("10. Return Book")
        print("11. Display Borrow Records")
        print("12. Display Unavailable Books")
        print("13. Display Active Members")
        print("0. Exit")

    def run(self):
        while True:
            self.display_menu()

            choice = int(input("Enter Choice: "))

            if choice == 1:
                self.library.add_book()

            elif choice == 2:
                self.library.remove_book()

            elif choice == 3:
                self.library.search_book()

            elif choice == 4:
                self.library.display_books()

            elif choice == 5:
                self.library.register_member()

            elif choice == 6:
                self.library.remove_member()

            elif choice == 7:
                self.library.search_member()

            elif choice == 8:
                self.library.display_members()

            elif choice == 9:
                self.library.borrow_book()

            elif choice == 10:
                self.library.return_book()

            elif choice == 11:
                self.library.display_borrow_records()

            elif choice == 12:
                self.library.display_unavailable_books()

            elif choice == 13:
                self.library.display_active_members()

            elif choice == 0:
                print("Goodbye!")
                break

            else:
                print("Invalid Choice.\n")


def main():
    system = Menu()
    system.run()


if __name__ == "__main__":
    main()