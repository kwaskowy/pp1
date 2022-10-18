st_cel = input("Podaj temperaturę w stopniach celsjusza:")
st_cel = int(st_cel)
kel = st_cel + 273
kel = int(kel)
st_fah = st_cel*(9/5)+32
st_fah = int(st_fah)
print(f"{st_cel}°C w stopniach Fahrenheita: {st_fah}F oraz w Kelwinach: {kel}K")