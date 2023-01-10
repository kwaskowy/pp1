import re
#otwieramy plik
file= open("grades.txt", "r")

#czytamy zawartosc
filecontent= file.read()

#szukamy ocen, w tym przypadku dostaniemy tablice ktora wyglada nastepująco oceny=['3', '.', '5', '4', '.','0'...] 
# dlatego trzeba się tego pozbyć tak żeby oceny wyglądały jak ['3.5','4.0'...]
oceny= re.findall("[{\d}.{\d}]",filecontent)

#zamykamy plik
file.close()

#w zmiennej wlasciwe przechowamy oceny juz w poprawnym formacie
wlasciwe= [] #####przykladowa zawartosc zmiennej podczas wykonywania pętli: wlasciwe= ['3.5','4.0']

#licznik sluzy do tego zeby po trzech pozycjach wrzuciło naszego stringa do zmiennej wlasciwe
licznik=0

#zmienna string służy do "sklejenia" trzech następujących po sobie pozycji w tablicy
string= "" #####przykladowa zawartosc zmiennej podczas wykonywania pętli: string="3.5"


#pętla for dla kazdego elementu w zmiennej oceny
for x in oceny:
    string+=x
    licznik+=1
    #po trzech znakach licznik się resetuje, a ciąg znaków w formacie 'x.x' zostaje dodany do tablicy wlasciwe
    if licznik==3:
        wlasciwe.append(string)
        licznik=0
        #po tym zmienna string zostaje wyczyszczona i zostają dodane kolejne znaki aż do zakończenia pętli
        string= ""

#tutaj program oblicza srednią biorąc dane z tablicy "wlasciwej" z liczbami w poprawnym formacie,takim jakim chcielismy
suma=0
liczbaocen=0
for x in wlasciwe:
    suma+=float(x)
    liczbaocen+=1

#wyswietlenie wyniku
print(f"{filecontent}\nArithmetic mean of student`s grades: {suma//liczbaocen} ")