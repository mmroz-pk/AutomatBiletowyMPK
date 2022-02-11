########################################################################
# Importujemy moduł, który pozwala na utworzenie interfejsu graficznego
########################################################################
import PySimpleGUI as gui

###############
# Wartość w zł
###############

# Dostępne nominały w automacie
automat = (0, 0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50)

# Cena biletów
cennik = (0, 2, 4, 6, 1, 2, 3)

###############################################################
# Ilośc poszczególnych monet/banknotów przechowane w Automacie
###############################################################

# Monety
# automat_1gr = open("./safe/monety/1gr", "w+")
ilosc_1gr = 0
ilosc_2gr = 0
ilosc_5gr = 0
ilosc_10gr = 0
ilosc_20gr = 0
ilosc_50gr = 0
ilosc_1zl = 0
ilosc_2zl = 0
ilosc_5zl = 0
ilosc_10zl = 0
ilosc_20zl = 0
ilosc_50zl = 0
# automat_2gr = open("./safe/monety/2gr", "w+")
# automat_5gr = open("./safe/monety/5gr", "w+")
# automat_10gr = open("./safe/monety/10gr", "w+")
# automat_20gr = open("./safe/monety/20gr", "w+")
# automat_50gr = open("./safe/monety/50gr", "w+")
# automat_1zl = open("./safe/monety/1zl", "w+")
# automat_2zl = open("./safe/monety/2zl", "w+")
# automat_5zl = open("./safe/monety/5zl", "w+")
# Banknoty
# automat_10zl = open("./safe/banknoty/10zl", "w+")
# automat_20zl = open("./safe/banknoty/20zl", "w+")
# automat_50zl = open("./safe/banknoty/50zl", "w+")

###############
# Suma kosztów
###############
suma = 0

###############################
# Suma osobno wrzuconych monet
###############################
suma_1gr = 0
suma_2gr = 0
suma_5gr = 0

suma_10gr = 0
suma_20gr = 0
suma_50gr = 0

suma_1zl = 0
suma_2zl = 0
suma_5zl = 0

suma_10zl = 0
suma_20zl = 0
suma_50zl = 0

#################################
# Ile jeszcze zostało do zapłaty
#################################
reszta_do_zaplaty = 0

################################
# Suma osobno wybranych biletów
################################
suma_20n = 0
suma_40n = 0
suma_60n = 0

suma_20u = 0
suma_40u = 0
suma_60u = 0

#########################
# Ilość 1 rodzaju biletu
#########################
ilosc = 0

######################
# Suma ilości biletów
######################
ilosc_suma = 0

###############################################
# Ilość poszczególnej wybranej monety/banknotu
###############################################
ilosc_waluty = 0

#################################
# Ilośc osobno wybranych biletow
#################################
ilosc_20n = 0
ilosc_40n = 0
ilosc_60n = 0

ilosc_20u = 0
ilosc_40u = 0
ilosc_60u = 0

#######################
# Główne Menu Automatu
#######################
layout = [
    [gui.Text("-- Automat MPK --")],
    [gui.Text("Bilet Normalny:")],
    [gui.Text("(1) 20-minutowy = 2 zł"), gui.Text(key='20n')],
    [gui.Text("(2) 40-minutowy = 4 zł"), gui.Text(key='40n')],
    [gui.Text("(3) 60-minutowy = 6 zł"), gui.Text(key='60n')],
    [gui.Text("---")],
    [gui.Text("Bilet Ulgowy (-50%):")],
    [gui.Text("(4) 20-minutowy = 1 zł"), gui.Text(key='20u')],
    [gui.Text("(5) 40-minutowy = 2 zł"), gui.Text(key='40u')],
    [gui.Text("(6) 60-minutowy = 3 zł"), gui.Text(key='60u')],
    [gui.Text("---")],
    [gui.Text("Wybierz bilet")],
    [gui.Button("1"), gui.Button("2"), gui.Button("3"), gui.Button("4"), gui.Button("5"), gui.Button("6")],
    [gui.Text("---")],
    [gui.Text("Ilość:"), gui.Text('0', key='-ILOSC-', size=(3, 1)), gui.Button("+"), gui.Button("-"),
     gui.Button("Zeruj")],
    [gui.Text("---")],
    [gui.Text("Suma:"), gui.Text('0', key='-SUMA-'), gui.Text("zł")],
    [gui.Text("---")],
    [gui.Button("Kup"), gui.Button("Wyzeruj"), gui.Button("Wyjdź")]
]
##############
# Stwórz okno
##############
window = gui.Window("Automat MPK", layout, size=(300, 540))

while True:
    event, values = window.read()

    # Dodaj ilość o 1
    if event == "+":
        ilosc += 1
        window['-ILOSC-'].update(ilosc)

    # Odejmuj ilość o 1
    if event == "-":
        ilosc += -1
        if ilosc <= 0:
            ilosc = 0
        window['-ILOSC-'].update(ilosc)

    # Zeruj ilość
    if event == "Zeruj":
        ilosc = 0
        window['-ILOSC-'].update(ilosc)

    # Przycisk - Bilet #1
    if event == "1":
        if suma_20n >= 1:
            suma -= suma_20n
            # UWAGA #1: Popraw floaty tak jak poniżej
        if ilosc_waluty <= 0 and suma_20n != 0:
            ilosc_waluty = 0
            suma_20n = 0

        suma_20n = cennik[1] * ilosc
        suma += suma_20n

        ilosc_suma += ilosc
        ilosc_20n = ilosc
        window['-SUMA-'].update(suma)
        window['20n'].update(f"- (Wybrano {ilosc_20n} szt.)")

    # Przycisk - Bilet #2
    if event == "2":
        if suma_40n > 0:
            suma -= suma_40n

        suma_40n = cennik[2] * ilosc
        suma += suma_40n

        ilosc_suma += ilosc
        ilosc_40n = ilosc
        window['-SUMA-'].update(suma)
        window['40n'].update(f"- (Wybrano {ilosc_40n} szt.)")

    # Przycisk - Bilet #3
    if event == "3":
        if suma_60n > 0:
            suma -= suma_60n

        suma_60n = cennik[3] * ilosc
        suma += suma_60n

        ilosc_suma += ilosc
        ilosc_60n = ilosc
        window['-SUMA-'].update(suma)
        window['60n'].update(f"- (Wybrano {ilosc_60n} szt.)")

    # Przycisk - Bilet #4
    if event == "4":
        if suma_20u > 0:
            suma -= suma_20u

        suma_20u = cennik[4] * ilosc
        suma += suma_20u

        ilosc_suma += ilosc
        ilosc_20u = ilosc
        window['-SUMA-'].update(suma)
        window['20u'].update(f"- (Wybrano {ilosc_20u} szt.)")

    # Przycisk - Bilet #5
    if event == "5":
        if suma_40u > 0:
            suma -= suma_40u

        suma_40u = cennik[5] * ilosc
        suma += suma_40u

        ilosc_suma += ilosc
        ilosc_40u = ilosc
        window['-SUMA-'].update(suma)
        window['40u'].update(f"- (Wybrano {ilosc_40u} szt.)")

    # Przycisk - Bilet #6
    if event == "6":
        if suma_60u > 0:
            suma -= suma_60u

        suma_60u = cennik[6] * ilosc
        suma += suma_60u

        ilosc_suma += ilosc
        ilosc_60u = ilosc
        window['-SUMA-'].update(suma)
        window['60u'].update(f"- (Wybrano {ilosc_60u} szt.)")

    # Przycisk - Wyzeruj wszystko
    if event == "Wyzeruj":
        suma = 0
        suma_20n = 0
        suma_40n = 0
        suma_60n = 0
        suma_20u = 0
        suma_40u = 0
        suma_60u = 0
        ilosc = 0
        ilosc_suma = 0
        ilosc_20n = 0
        ilosc_40n = 0
        ilosc_60n = 0
        ilosc_20u = 0
        ilosc_40u = 0
        ilosc_60u = 0
        window['20n'].update("")
        window['40n'].update("")
        window['60n'].update("")
        window['20u'].update("")
        window['40u'].update("")
        window['60u'].update("")
        window['-SUMA-'].update(suma)
        window['-ILOSC-'].update(ilosc)
        gui.popup("Wyzerowano!")

    # Przycisk - Wyjdź z Automatu
    if event == "Wyjdź" or event == gui.WIN_CLOSED:
        gui.popup("Do widzenia!")
        exit()

    # Przycisk - Kup
    if event == "Kup":
        if ilosc_suma == 0:
            gui.popup("Nie wybrano biletu")
        elif suma <= 0:
            suma = 0
            ilosc_suma = 0
            ilosc = 0
            ilosc_20n = 0
            ilosc_40n = 0
            ilosc_60n = 0
            ilosc_20u = 0
            ilosc_40u = 0
            ilosc_60u = 0
            window['20n'].update("")
            window['40n'].update("")
            window['60n'].update("")
            window['20u'].update("")
            window['40u'].update("")
            window['60u'].update("")
            window['-SUMA-'].update(suma)
            window['-ILOSC-'].update(ilosc)
            gui.popup("Nie można kontynuować z negatywną sumą")

        ###################
        # Bramka Płatności
        ###################
        elif ilosc_suma > 0:
            layout_two = [
                [gui.Text("-- Automat MPK --")],
                [gui.Text("Wyznacz wartość oraz ilość monet/banknot jakie zostaną wprowadzone do automatu")],
                [gui.Text("Uwaga! Automat nie wydaje reszty - Prosimy o wprowadzenie wyliczonej sumy")],
                [gui.Text("---")],
                [gui.Text(f"Suma: {suma} zł", key='-SUMA-')],
                [gui.Text(f"Reszta do zapłaty:"), gui.Text(f"{suma}", key='-SUMA-ZMIENNA-'), gui.Text("zł")],
                [gui.Button("1gr"), gui.Button("2gr"), gui.Button("5gr"), gui.Button("10gr"), gui.Button("20gr"),
                 gui.Button("50gr")],
                [gui.Button("1zł"), gui.Button("2zł"), gui.Button("5zł"), gui.Button("10zł"), gui.Button("20zł"),
                 gui.Button("50zł")],
                [gui.Text("---")],
                [gui.Text("Ilość:"), gui.Text('0', key='-ILOSC-WALUTY-', size=(3, 1)), gui.Button("+"),
                 gui.Button("-"), gui.Button("Zeruj")],
                [gui.Text("---")],
                [gui.Button("Wróć"), gui.Button("Wyjdź")]
            ]
            # *#*#*#*#*#*#*#*#*#*#*#*#
            # Wyświetlanie Okienka #2
            # *#*#*#*#*#*#*#*#*#*#*#*#
            window_two = gui.Window("Automat MPK", layout_two)

            suma = float("{:.3f}".format(suma))
            reszta_do_zaplaty = suma

            while True:
                event, values = window_two.read()

                #################
                # Dodaj ilość
                #################
                if event == "+":
                    ilosc_waluty += 1
                    window_two['-ILOSC-WALUTY-'].update(ilosc_waluty)

                ################
                # Odejmuj ilość
                ################
                if event == "-":
                    ilosc_waluty += -1
                    if ilosc_waluty <= 0:
                        ilosc_waluty = 0
                    window_two['-ILOSC-WALUTY-'].update(ilosc_waluty)

                ##############
                # Zeruj ilość
                ##############
                if event == "Zeruj":
                    ilosc_waluty = 0
                    window_two['-ILOSC-WALUTY-'].update(ilosc_waluty)

                #################
                # Przycisk - 1gr
                #################
                if event == "1gr":
                    wrzucam = (automat[1] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_1gr += (automat[1] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_1gr = float("{:.3f}".format(suma_1gr))
                    print(f"{suma_1gr} zł - Wrzucono w sumie")  # log

                    ilosc_1gr += ilosc_waluty  # zapisujemy łączną ilość 1gr, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_1gr -= reszta  # zapisujemy łączną ilość 1gr, która została wrzucona (pętla)
                        suma_1gr = float("{:.3f}".format(suma_1gr))

                        # teraz zwroc klientowi reszta_1gr
                        reszta_1gr = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_1gr = float(ilosc_1gr) - float(reszta_1gr)

                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_1gr) + float(zysk_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_1gr)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 1gr wyrównał płatności

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 2gr
                #################
                if event == "2gr":
                    wrzucam = (automat[2] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_2gr += (automat[2] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_2gr = float("{:.3f}".format(suma_2gr))
                    print(f"{suma_2gr} zł - Wrzucono w sumie")  # log

                    ilosc_2gr += ilosc_waluty  # zapisujemy łączną ilość 2gr, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_2gr -= reszta  # zapisujemy łączną ilość 2gr, która została wrzucona (pętla)
                        suma_2gr = float("{:.3f}".format(suma_2gr))

                        # teraz zwroc klientowi reszta_2gr
                        reszta_2gr = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_2gr = float(ilosc_2gr) - float(reszta_2gr)

                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_2gr) + float(zysk_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_2gr)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_2gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 2gr wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 5gr
                #################
                if event == "5gr":
                    wrzucam = (automat[3] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_5gr += (automat[3] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_5gr = float("{:.3f}".format(suma_5gr))
                    print(f"{suma_5gr} zł - Wrzucono w sumie")  # log

                    ilosc_5gr += ilosc_waluty  # zapisujemy łączną ilość 5gr, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_5gr -= reszta  # zapisujemy łączną ilość 5gr, która została wrzucona (pętla)
                        suma_5gr = float("{:.3f}".format(suma_5gr))

                        # teraz zwroc klientowi reszta_5gr
                        reszta_5gr = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_5gr = float(ilosc_5gr) - float(reszta_5gr)

                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_5gr) + float(zysk_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_5gr)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_5gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 5gr wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 10gr
                #################
                if event == "10gr":
                    wrzucam = (automat[4] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_10gr += (automat[4] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_10gr = float("{:.3f}".format(suma_10gr))
                    print(f"{suma_10gr} zł - Wrzucono w sumie")  # log

                    ilosc_10gr += ilosc_waluty  # zapisujemy łączną ilość 10gr, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_10gr -= reszta  # zapisujemy łączną ilość 10gr, która została wrzucona (pętla)
                        suma_10gr = float("{:.3f}".format(suma_10gr))

                        # teraz zwroc klientowi reszta_10gr
                        reszta_10gr = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_10gr = float(ilosc_10gr) - float(reszta_10gr)

                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_10gr) + float(zysk_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_10gr)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_10gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 10gr wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 20gr
                #################
                if event == "20gr":
                    wrzucam = (automat[5] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_20gr += (automat[5] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_20gr = float("{:.3f}".format(suma_20gr))
                    print(f"{suma_20gr} zł - Wrzucono w sumie")  # log

                    ilosc_20gr += ilosc_waluty  # zapisujemy łączną ilość 20gr, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_20gr -= reszta  # zapisujemy łączną ilość 20gr, która została wrzucona (pętla)
                        suma_20gr = float("{:.3f}".format(suma_20gr))

                        # teraz zwroc klientowi reszta_20gr
                        reszta_20gr = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_20gr = float(ilosc_20gr) - float(reszta_20gr)

                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_20gr) + float(zysk_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_20gr)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_20gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 20gr wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 50gr
                #################
                if event == "50gr":
                    wrzucam = (automat[6] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_50gr += (automat[6] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_50gr = float("{:.3f}".format(suma_50gr))
                    print(f"{suma_50gr} zł - Wrzucono w sumie")  # log

                    ilosc_50gr += ilosc_waluty  # zapisujemy łączną ilość 50gr, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_50gr -= reszta  # zapisujemy łączną ilość 50gr, która została wrzucona (pętla)
                        suma_50gr = float("{:.3f}".format(suma_50gr))

                        # teraz zwroc klientowi reszta_50gr
                        reszta_50gr = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_50gr = float(ilosc_50gr) - float(reszta_50gr)

                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_50gr) + float(zysk_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_50gr)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_50gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 50gr wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 1zł
                #################
                if event == "1zł":
                    wrzucam = (automat[7] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_1zl += (automat[7] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_1zl = float("{:.3f}".format(suma_1zl))
                    print(f"{suma_1zl} zł - Wrzucono w sumie")  # log

                    ilosc_1zl += ilosc_waluty  # zapisujemy łączną ilość 1zl, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_1zl -= reszta  # zapisujemy łączną ilość 1zl, która została wrzucona (pętla)
                        suma_1zl = float("{:.3f}".format(suma_1zl))

                        # teraz zwroc klientowi reszta_1zl
                        reszta_1zl = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_1zl = float(ilosc_1zl) - float(reszta_1zl)

                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_1zl) + float(zysk_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_1zl)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_1zl} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 1zl wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 2zł
                #################
                if event == "2zł":
                    wrzucam = (automat[8] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_2zl += (automat[8] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_2zl = float("{:.3f}".format(suma_2zl))
                    print(f"{suma_2zl} zł - Wrzucono w sumie")  # log

                    ilosc_2zl += ilosc_waluty  # zapisujemy łączną ilość 2zl, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_2zl -= reszta  # zapisujemy łączną ilość 2zl, która została wrzucona (pętla)
                        suma_2zl = float("{:.3f}".format(suma_2zl))

                        # teraz zwroc klientowi reszta_2zl
                        reszta_2zl = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_2zl = float(ilosc_2zl) - float(reszta_2zl)

                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_2zl) + float(zysk_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_2zl)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_2zl} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 2zl wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 5zł
                #################
                if event == "5zł":
                    wrzucam = (automat[9] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_5zl += (automat[9] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_5zl = float("{:.3f}".format(suma_5zl))
                    print(f"{suma_5zl} zł - Wrzucono w sumie")  # log

                    ilosc_5zl += ilosc_waluty  # zapisujemy łączną ilość 5zl, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_5zl -= reszta  # zapisujemy łączną ilość 5zl, która została wrzucona (pętla)
                        suma_5zl = float("{:.3f}".format(suma_5zl))

                        # teraz zwroc klientowi reszta_5zl
                        reszta_5zl = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_5zl = float(ilosc_5zl) - float(reszta_5zl)

                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_5zl) + float(zysk_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_5zl)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_5zl} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 5zl wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 10zł
                #################
                if event == "10zł":
                    wrzucam = (automat[10] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_10zl += (automat[10] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_10zl = float("{:.3f}".format(suma_10zl))
                    print(f"{suma_10zl} zł - Wrzucono w sumie")  # log

                    ilosc_10zl += ilosc_waluty  # zapisujemy łączną ilość 10zl, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_10zl -= reszta  # zapisujemy łączną ilość 10zl, która została wrzucona (pętla)
                        suma_10zl = float("{:.3f}".format(suma_10zl))

                        # teraz zwroc klientowi reszta_10zl
                        reszta_10zl = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_10zl = float(ilosc_10zl) - float(reszta_10zl)

                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_10zl) + float(zysk_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_10zl)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj banknoty 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_10zl} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 10zl wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj banknoty 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 20zł
                #################
                if event == "20zł":
                    wrzucam = (automat[11] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_20zl += (automat[11] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_20zl = float("{:.3f}".format(suma_20zl))
                    print(f"{suma_20zl} zł - Wrzucono w sumie")  # log

                    ilosc_20zl += ilosc_waluty  # zapisujemy łączną ilość 20zl, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_20zl -= reszta  # zapisujemy łączną ilość 20zl, która została wrzucona (pętla)
                        suma_20zl = float("{:.3f}".format(suma_20zl))

                        # teraz zwroc klientowi reszta_20zl
                        reszta_20zl = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_20zl = float(ilosc_20zl) - float(reszta_20zl)

                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_20zl) + float(zysk_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_20zl)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj banknoty 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_20zl} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 20zl wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj banknoty 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 50zl
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno

                #################
                # Przycisk - 50zł
                #################
                if event == "50zł":
                    wrzucam = (automat[12] * ilosc_waluty)  # ile wrzucam
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_50zl += (automat[12] * ilosc_waluty)  # suma jaką wrzuciłem
                    suma_50zl = float("{:.3f}".format(suma_50zl))
                    print(f"{suma_50zl} zł - Wrzucono w sumie")  # log

                    ilosc_50zl += ilosc_waluty  # zapisujemy łączną ilość 50zl, która została wrzucona

                    print(f"{suma} zł - Suma do zapłaty")  # log

                    reszta_do_zaplaty -= wrzucam  # od reszty do zapłaty odejmujemy wrzuconą wartość monety
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} zł - Reszta do zapłaty\n---\n")  # log

                    # Warunki po wrzuceniu monety
                    if reszta_do_zaplaty < 0:  # jeśli wrzucimy więcej niż potrzeba
                        reszta = reszta_do_zaplaty * (-1)  # ujemną liczbę mnożymy przez (-1), aby stała się zwrotna
                        reszta = float("{:.3f}".format(reszta))
                        suma_50zl -= reszta  # zapisujemy łączną ilość 50zl, która została wrzucona (pętla)
                        suma_50zl = float("{:.3f}".format(suma_50zl))

                        # teraz zwroc klientowi reszta_50zl
                        reszta_50zl = float(reszta) / float(automat[1])  # obliczam jaka jest ilość tej reszty

                        # dodaj do automatu twoją działke
                        zysk_50zl = float(ilosc_50zl) - float(reszta_50zl)

                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu

                        dodaj_do_automatu = float(automat_50zl) + float(zysk_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_waluty)} - dodano do automatu")  # log
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")  # log

                        # Spradza co dzieje się dalej
                        print(suma_50zl)  # log
                        print(suma)  # log
                        print(reszta_do_zaplaty)  # log

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                        # Należy tu jeszcze wsadzić funkcje, które doda pozostałe monety do ich zbiorników

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj banknoty 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        window_two.close()  # zamknij okno
                        break

                    if reszta_do_zaplaty > 0:  # jeśli jest reszta do zapłaty
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)  # aktualizuj sumę
                        # gui.popup(f"Wrzucono: {suma_50zl} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:  # jeśli wrzucono odliczoną ilość
                        automat_50zl = open("./safe/banknoty/50zl", "r").read()  # czytamy ilość 50zl w automacie
                        dodaj_do_automatu = float(automat_50zl) + float(ilosc_50zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50zl = open("./safe/banknoty/50zl", "w")  # zmienna do zapisu
                        zapisz_automat_50zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50zl do automatu
                        zapisz_automat_50zl.close()  # zamknij plik

                        print(f"{int(ilosc_50zl)} - dodano do automatu o nominale 50zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50zl w automacie")

                        # Zapisujemy resztę monet do ich zbiorników, po tym jak 50zl wyrównał płatności

                        # Dodaj monety 1gr
                        automat_1gr = open("./safe/monety/1gr", "r").read()  # czytamy ilość 1gr w automacie
                        dodaj_do_automatu = float(automat_1gr) + float(ilosc_1gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1gr = open("./safe/monety/1gr", "w")  # zmienna do zapisu
                        zapisz_automat_1gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1gr do automatu
                        zapisz_automat_1gr.close()  # zamknij plik

                        print(f"{int(ilosc_1gr)} - dodano do automatu o nominale 1gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1gr w automacie")

                        # Dodaj monety 2gr
                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")

                        # Dodaj monety 5gr
                        automat_5gr = open("./safe/monety/5gr", "r").read()  # czytamy ilość 5gr w automacie
                        dodaj_do_automatu = float(automat_5gr) + float(ilosc_5gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5gr = open("./safe/monety/5gr", "w")  # zmienna do zapisu
                        zapisz_automat_5gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5gr do automatu
                        zapisz_automat_5gr.close()  # zamknij plik

                        print(f"{int(ilosc_5gr)} - dodano do automatu o nominale 5gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5gr w automacie")

                        # Dodaj monety 10gr
                        automat_10gr = open("./safe/monety/10gr", "r").read()  # czytamy ilość 10gr w automacie
                        dodaj_do_automatu = float(automat_10gr) + float(ilosc_10gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10gr = open("./safe/monety/10gr", "w")  # zmienna do zapisu
                        zapisz_automat_10gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10gr do automatu
                        zapisz_automat_10gr.close()  # zamknij plik

                        print(f"{int(ilosc_10gr)} - dodano do automatu o nominale 10gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10gr w automacie")

                        # Dodaj monety 20gr
                        automat_20gr = open("./safe/monety/20gr", "r").read()  # czytamy ilość 20gr w automacie
                        dodaj_do_automatu = float(automat_20gr) + float(ilosc_20gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20gr = open("./safe/monety/20gr", "w")  # zmienna do zapisu
                        zapisz_automat_20gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20gr do automatu
                        zapisz_automat_20gr.close()  # zamknij plik

                        print(f"{int(ilosc_20gr)} - dodano do automatu o nominale 20gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20gr w automacie")

                        # Dodaj monety 50gr
                        automat_50gr = open("./safe/monety/50gr", "r").read()  # czytamy ilość 50gr w automacie
                        dodaj_do_automatu = float(automat_50gr) + float(ilosc_50gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_50gr = open("./safe/monety/50gr", "w")  # zmienna do zapisu
                        zapisz_automat_50gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 50gr do automatu
                        zapisz_automat_50gr.close()  # zamknij plik

                        print(f"{int(ilosc_50gr)} - dodano do automatu o nominale 50gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 50gr w automacie")

                        # Dodaj monety 1zl
                        automat_1zl = open("./safe/monety/1zl", "r").read()  # czytamy ilość 1zl w automacie
                        dodaj_do_automatu = float(automat_1zl) + float(ilosc_1zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_1zl = open("./safe/monety/1zl", "w")  # zmienna do zapisu
                        zapisz_automat_1zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 1zl do automatu
                        zapisz_automat_1zl.close()  # zamknij plik

                        print(f"{int(ilosc_1zl)} - dodano do automatu o nominale 1zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 1zl w automacie")

                        # Dodaj monety 2zl
                        automat_2zl = open("./safe/monety/2zl", "r").read()  # czytamy ilość 2zl w automacie
                        dodaj_do_automatu = float(automat_2zl) + float(ilosc_2zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2zl = open("./safe/monety/2zl", "w")  # zmienna do zapisu
                        zapisz_automat_2zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2zl do automatu
                        zapisz_automat_2zl.close()  # zamknij plik

                        print(f"{int(ilosc_2zl)} - dodano do automatu o nominale 2zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2zl w automacie")

                        # Dodaj banknoty 5zl
                        automat_5zl = open("./safe/monety/5zl", "r").read()  # czytamy ilość 5zl w automacie
                        dodaj_do_automatu = float(automat_5zl) + float(ilosc_5zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_5zl = open("./safe/monety/5zl", "w")  # zmienna do zapisu
                        zapisz_automat_5zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 5zl do automatu
                        zapisz_automat_5zl.close()  # zamknij plik

                        print(f"{int(ilosc_5zl)} - dodano do automatu o nominale 5zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 5zl w automacie")

                        # Dodaj banknoty 10zl
                        automat_10zl = open("./safe/banknoty/10zl", "r").read()  # czytamy ilość 10zl w automacie
                        dodaj_do_automatu = float(automat_10zl) + float(ilosc_10zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_10zl = open("./safe/banknoty/10zl", "w")  # zmienna do zapisu
                        zapisz_automat_10zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 10zl do automatu
                        zapisz_automat_10zl.close()  # zamknij plik

                        print(f"{int(ilosc_10zl)} - dodano do automatu o nominale 10zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 10zl w automacie")

                        # Dodaj banknoty 20zl
                        automat_20zl = open("./safe/banknoty/20zl", "r").read()  # czytamy ilość 20zl w automacie
                        dodaj_do_automatu = float(automat_20zl) + float(ilosc_20zl)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_20zl = open("./safe/banknoty/20zl", "w")  # zmienna do zapisu
                        zapisz_automat_20zl.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 20zl do automatu
                        zapisz_automat_20zl.close()  # zamknij plik

                        print(f"{int(ilosc_20zl)} - dodano do automatu o nominale 20zl")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 20zl w automacie")

                        # Koniec dodawania

                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno
                
                #################
                # Przycisk - Wróć
                #################
                if event == "Wróć":
                    ilosc_waluty = 0
                    suma = reszta_do_zaplaty
                    window_two.close()
                    break

                #################
                # Przycisk - Wyjdź
                #################
                if event == "Wyjdź":
                    gui.popup("Do widzenia!")
                    exit()

                #################
                # Przycisk - "X" - Okienka
                #################
                if event == gui.WIN_CLOSED:
                    window_two.close()
                    break
