#automat przechowuje
kasa_gr = (0.01, 0.02, 0.05, 0.1, 0.2, 0.5)
kasa_zl = (1, 2, 5, 10, 20, 50)
cennik = (0, 4, 5, 6, 2, 2.5, 3)

#lista biletów
print("---")
print("Witamy w MPK - Wybierz rodzaj biletu")
print("---")

print("Bilet Normalny:")
print("(1) 20-minutowy")
print("(2) 40-minutowy")
print("(3) 60-minutowy")
print("---")
print("Bilet Ulgowy (-50%):")
print("(4) 20-minutowy")
print("(5) 40-minutowy")
print("(6) 60-minutowy")
print("---")

#Wybór klienta
opcja = int(input("Wprowadź cyfrę (1-6): "))

#Sprawdz poprawność
while opcja <=0 or opcja >=7:
    print("Niepoprawny numer")
    opcja = int(input("Wprowadź cyfrę (1-6): "))

opcja_ilosc = int(input("Wprowadź ilość: "))



if opcja == 1:
    rodzaj_biletu = "20-minutowy"
    typ_biletu = "Normalny"
    cena_biletu = cennik[1]
    suma_kosztow = cennik[1] * opcja_ilosc
elif opcja == 2:
    rodzaj_biletu = "40-minutowy"
    typ_biletu = "Normalny"
    cena_biletu = cennik[2]
    suma_kosztow = cennik[2] * opcja_ilosc
elif opcja == 3:
    rodzaj_biletu = "60-minutowy"
    typ_biletu = "Normalny"
    cena_biletu = cennik[3]
    suma_kosztow = cennik[3] * opcja_ilosc
elif opcja == 4:
    rodzaj_biletu = "40-minutowy"
    typ_biletu = "Ulgowy"
    cena_biletu = cennik[4]
    suma_kosztow = cennik[4] * opcja_ilosc
elif opcja == 5:
    rodzaj_biletu = "40-minutowy"
    typ_biletu = "Ulgowy"
    cena_biletu = cennik[5]
    suma_kosztow = cennik[5] * opcja_ilosc
elif opcja == 6:
    rodzaj_biletu = "40-minutowy"
    typ_biletu = "Ulgowy"
    cena_biletu = cennik[6]
    suma_kosztow = cennik[6] * opcja_ilosc

print("---")

print("*Twój Koszyk*")
print("---")

print("|" + "ILOŚĆ" + "|" + "BILET" + "|" + "TYP"  + "|" + "WARTOŚĆ" + "|")
print("---")

print("|" + str(opcja_ilosc) + "x" + "|" + rodzaj_biletu + "|" + typ_biletu + "|" + str(cena_biletu) + "zł|")
print("---")

print("Do zapłacenia: " + str(suma_kosztow) + " zł")
print("---")
wybor = int(input("(1) Dalej, (2) Kontynuuj Zakupy, (3) Usun: "))

while wybor <=0 or wybor >=4:
    print("Niepoprawny numer")
    wybor = int(input("(1) Dalej, (2) Kontynuuj Zakupy, (3) Usun: "))

#to be continued...


