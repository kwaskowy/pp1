def f(player1,player2):
    wynik= 0
    for x in player1:
        if x=="A" or x=="K" or x=="Q" or x=="J" or x=="T":
            wynik+=10
        elif x=="9" or x=="8" or x=="7" or x=="6" or x=="5" or x=="4" or x=="3" or x=="2" or x=="1":
            wynik+=int(x)
    for x in player2:
        if x=="A" or x=="K" or x=="Q" or x=="J" or x=="T":
            wynik-=10
        elif x=="9" or x=="8" or x=="7" or x=="6" or x=="5" or x=="4" or x=="3" or x=="2" or x=="1":
            wynik-=int(x)
    if wynik>0:
        return True
    else: return False