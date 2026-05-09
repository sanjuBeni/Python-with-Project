
# Requirement Packages
import json
import random
import string
from datetime import datetime
from pathlib import Path
from FileConnection import connection_with_file

class LibraryManagement():

    # Generate ID
    def gen_id(Prefix = "B"):
        """
            Generage Unique Random ID for new book and new member.
                - Prefix B for Book
                - Prefix M for member
        """
        random_id = ""
        for _ in range(5):
            random_id += random.choice(string.ascii_uppercase + string.digits)

        return f"{Prefix}-{random_id}"
    
    # Add Method
    def add_data(key, data):
        # True for get data
        all_data = connection_with_file(True)
        all_data[key].append(data)
        # False for add data
        all_data = connection_with_file(False, all_data)
        print(f"{key[:len(key)-1].capitalize()} saved successfully.")

    # Add a book
    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter book author: ")
        copies = int(input("Enter number of books: "))

        book_data = {
            "id" : LibraryManagement.gen_id(), # Unique random generated
            "title" : title,
            "author" : author,
            "copies" : copies,
            "available_copies" : copies,
            "add_on" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        LibraryManagement.add_data('books', book_data)

    # Get All Books
    def get_books(self):
        data = connection_with_file(True)
        books = data.get('books', [])
        print(f"{'ID':12} {'Title':25} {'Author':20} {'Total Copies':10} {'Available Copies':10}")
        for book in books:
            print(f"{book.get('id', ''):12} {book.get('title', '')[:25]:25} {book.get('author', '')[:15]:20} {book.get('copies', 0):10} {book.get('available_copies', 0):10}")
            # print(f"Book Add on: {book.get('add_on', '')}")


    """
        Member Methods
    """
    # Add Member
    def add_member(self):
        name = input("Enter member name: ")
        email = input("Enter member mail: ")

        member_data = {
            "id" : LibraryManagement.gen_id('M'),
            "name" : name,
            "email" : email,
            "borrow" : [],
            "add_on" : datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        LibraryManagement.add_data('members', member_data)

    # Get Members
    def get_members(self):
        members = connection_with_file(True)['members']
        for member in members:
            print("-"*50)
            print(f"Member ID: {member.get('id', '')}")
            print(f"Member Title: {member.get('name', '')}")
            print(f"Member Email: {member.get('email', '')}")
            print(f"Book Add on: {member.get('add_on', '')}")

    # Borrow Book
    def borrow_book(self):
        data = connection_with_file(True)
        
        member_name = input("Enter member name: ").strip().lower()
        which_book = input("Which one book you want to get: ").strip().lower()
        how_many = int(input("How many book you want to get: "))
        
        find_book = [book for book in data['books'] if book['title'].lower() == which_book]
        if not find_book:
            print(f'Book name `{which_book}` is not found.')
            return
        
        book = find_book[0]
        book['available_copies'] -= how_many
                
        member = [member for member in data['members'] if member['name'].lower() == member_name]
        if not member:
            print(f'Member name `{member_name}` is not found.')
            return  

        member[0]['borrow'].append({
                    "book_id" : book['id'],
                    "no_of_books" : how_many,
                })
        member[0]['update_on'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")            
        connection_with_file(False, data)
        print(f"You borrow {how_many} book: {which_book}")
        return

    # Return Book
    def return_book(self):
        member_id = input('Enter member id: ').strip()
        book_id = input('Enter book id, which book you return: ').strip()
        data = connection_with_file(True)

        no_of_books_return = 0
        member = [member for member in data['members'] if member['id'] == member_id]
        if not member:
            print(f'Member not found.')
            return  

        borrowed_book = [borrow for borrow in member[0]['borrow'] if borrow['book_id'] == book_id]
        if not borrowed_book:
            print("No one book borrowed by this member.")
            return

        borrowed_book

        # no_of_books_return = book['no_of_books']
        # book['no_of_books'] = 0
        # book['is_return'] = 'Y'
        # book['update_on'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        find_book = [book for book in data['books'] if book['id'] == book_id]
        if not find_book:
            print("Book not found")
        
        # book['available_copies'] += no_of_books_return
    
        connection_with_file(False, data)
        print("Book return successfully.")
        

lm = LibraryManagement()

print("="*50)
print("Library Management System")
print("="*50)
print("1. Add Book")
print("2. List Book")
print("3. Add Member")
print("4. List Member")
print("5. Borrow Books")
print("6. Return Books")
print("0. Exist the Portal")
print("-"*50)


while True:
    choice = int(input("What type of the operation you want to perform: "))

    if choice == 1:
        lm.add_book()
    elif choice == 2:
        lm.get_books()
    elif choice == 3:
        lm.add_member()
    elif choice == 4:
        lm.get_members()
    elif choice == 5:
        lm.borrow_book()
    elif choice == 6:
        lm.return_book()
    elif choice == 0:
        break
    else:
        print("Wrong entry...")