class Contact_List():
    def __init__(self):
        self.lista_kontaktow= []
    def add(self):
        from contact import Contact
        kontakt= Contact(input("Podaj nazwe: "),input("Podaj mail: "),int(input("Podaj nr.: ")))
        self.lista_kontaktow.append(kontakt.name)
        self.lista_kontaktow.append(kontakt.email)
        self.lista_kontaktow.append(kontakt.telephone)
    def display(self):
        licznik=1
        for x in range(len(self.lista_kontaktow)):
            if licznik==3:
                print(self.lista_kontaktow[x])
                licznik=1
            else:
                print(self.lista_kontaktow[x],end=" ")
                licznik+=1