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

                        automat_2gr = open("./safe/monety/2gr", "r").read()  # czytamy ilość 2gr w automacie
                        dodaj_do_automatu = float(automat_2gr) + float(ilosc_2gr)  # dodajemy z,do automatu
                        dodaj_do_automatu = float("{:.3f}".format(dodaj_do_automatu))
                        zapisz_automat_2gr = open("./safe/monety/2gr", "w")  # zmienna do zapisu
                        zapisz_automat_2gr.write(str(int(dodaj_do_automatu)))  # zapisz nową ilość 2gr do automatu
                        zapisz_automat_2gr.close()  # zamknij plik

                        print(f"{int(ilosc_2gr)} - dodano do automatu o nominale 2gr")
                        print(f"{int(dodaj_do_automatu)} - łączna ilość 2gr w automacie")


                        reszta_do_zaplaty = 0  # zeruj resztę
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                        window_two.close()  # zamknij okno
                # Koniec testu na 1gr

                #################
                # Przycisk - 2gr
                #################
                if event == "2gr":
                    print("under_edit")

                #################
                # Przycisk - 5gr
                #################
                if event == "5gr":
                    print("under_edit")

                #################
                # Przycisk - 20gr
                #################
                if event == "20gr":
                    print("under_edit")

                #################
                # Przycisk - 50gr
                #################
                if event == "50gr":
                    print("under_edit")

                #################
                # Przycisk - 1zł
                #################
                if event == "1zł":
                    print("under_edit")

                #################
                # Przycisk - 2zł
                #################
                if event == "2zł":
                    print("under_edit")

                #################
                # Przycisk - 5zł
                #################
                if event == "5zł":
                    print("under_edit")

                #################
                # Przycisk - 10zł
                #################
                if event == "10zł":
                    print("under_edit")

                #################
                # Przycisk - 20zł
                #################
                if event == "20zł":
                    print("under_edit")

                #################
                # Przycisk - 50zł
                #################
                if event == "50zł":
                    print("under_edit")

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
