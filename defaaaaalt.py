parola=input("SPUNE PAROLA")
lista_num = ["1","2","3","4","5","6","7","8","9","0"]
lista2 = ["@","#","!","$","%","&","*"]

ok=False
for numar in lista_num:
    if numar in parola:
        ok=True

bun=False
for caracter in lista2:
    if caracter in parola:
        bun=True


if ok==False:
    print("gresit")


elif len(parola)<5:
    print("gresit")

elif len(parola)>10:
    print("gresit")


elif (" ") in parola:
    print("gresit")


else:
    print("PAROLA VALIDA")



