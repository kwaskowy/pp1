from ebook import Ebook
i=0
ksiega= Ebook("John Ronald Reuel Tolkien","\"Hobbit, czyli tam i z powrotem\"",300)
print()
ksiega.book_status()
print()
ksiega.open_book()
ksiega.book_status()
print()
while i<299:
    ksiega.next_page()
    i+=1
ksiega.book_status()
print()
ksiega.next_page()
ksiega.book_status()
print()
ksiega.next_page()