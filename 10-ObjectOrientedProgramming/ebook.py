class Ebook():
    def __init__(self,author,title,number_pgs):
        self.author= author
        self.title= title
        self.number_pgs= number_pgs
        self.current_pg= 0
        self.is_open= False
    def open_book(self):
        self.is_open=True
        self.current_pg=1
    def close_book(self):
        self.is_open=False
        self.current_pg=0
    def next_page(self):
        if self.is_open:
            if 1<=self.current_pg<=self.number_pgs:
                self.current_pg+=1
                #JEZELI PRZEWROCIMY KARTKE NA STRONE WIEKSZA NIZ LICZBA STRON TO ZAMKNIEMY KSIAZKE XD#
                if self.current_pg>self.number_pgs:
                    self.is_open=False
        else: print("You can`t read that book- it`s closed")
    def previous_pg(self):
        if self.is_open:
            if self.number_pgs>=self.current_pg>=1:
                self.current_pg-=1
                ##JEŻELI PRZEWROCIMY KARTKE NA STRONE 0 CZYLI TYTULOWA TO ZAMKNIEMY KSIAZKE XD#
                if self.current_pg==0:
                    self.is_open=False
        else: print("You can`t read that book- it`s closed")
    def book_status(self):
        if self.is_open:
            print(f"Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.number_pgs}\nCurrent page number: {self.current_pg}")
        else: print(f"Title: {self.title}\nAuthor: {self.author}\nNumber of pages: {self.number_pgs}\nOpen it and start reading!")