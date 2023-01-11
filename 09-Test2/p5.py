def f(first_letter,last_letter):
    file= open("data.txt","r")
    filecontent= file.read()
    liczba= 0
    for x in filecontent:
        for word in x:
            if word[0]==first_letter and word[-1]==last_letter:
                liczba+=1
    return liczba