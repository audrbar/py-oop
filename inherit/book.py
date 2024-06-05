# 4. Sukurkite paprastą bibliotekos sistemą su knygomis, nariais ir skolintomis knygomis.
# 	4.1 Sukurkite bazinę klasę Book su atributais title, author ir isbn (knygis id).
# 	4.2 Sukurkite bazinę klasę Member su atributais name ir member_id.
# 	4.3 Sukurkite išvestinę klasę BorrowedBook, kuri paveldi iš Book ir prideda atributus
# 	borrower_name (member vardas kuris pasiėmė knygą) ir due_date (iki kada pasiėmė).
# 	4.4. Sukurkite Member ir imituokite bibliotekos veiklą.

class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn


class Member:
    def __init__(self, name: str, member_id: str):
        self.name = name
        self.member_id = member_id


class BorrowedBook(Book):
    def __init__(self, title: str, author: str, isbn: str, borrower_name: str, due_date: str):
        super().__init__(title, author, isbn)
        self.borrower_name = borrower_name
        self.due_date = due_date


book_1 = Book('Pievos', 'Antanas', '456')
print(f"Book: {book_1.title}, {book_1.author}, {book_1.isbn}.")
memb_1 = Member('Audrius', '123')
print(f"Member: {memb_1.name}, {memb_1.member_id}")
borbk = BorrowedBook(book_1, memb_1)