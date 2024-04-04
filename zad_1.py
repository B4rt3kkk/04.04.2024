a=0
b=0
print("podaj 10 liczb i sprawdź czy można z niego utworzyć kwadrat (WOW)")
for i in range(1,11) :
    bok=int(input("Podaj liczbę bratku: "))
    if bok>a:
        b=a
        a=bok
    else:
        if bok>b:
            b=bok
print(a,b)
