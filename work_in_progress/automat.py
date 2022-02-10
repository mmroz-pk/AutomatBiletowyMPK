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
ilosc_1gr = open("./safe/monety/1gr", "r+").read()
ilosc_2gr = open("./safe/monety/2gr", "r+").read()
ilosc_5gr = open("./safe/monety/5gr", "r+").read()
ilosc_10gr = open("./safe/monety/10gr", "r+").read()
ilosc_20gr = open("./safe/monety/20gr", "r+").read()
ilosc_50gr = open("./safe/monety/50gr", "r+").read()
ilosc_1zl = open("./safe/monety/1zl", "r+").read()
ilosc_2zl = open("./safe/monety/2zl", "r+").read()
ilosc_5zl = open("./safe/monety/5zl", "r+").read()
# Banknoty
ilosc_10zl = open("./safe/banknoty/10zl", "r+").read()
ilosc_20zl = open("./safe/banknoty/20zl", "r+").read()
ilosc_50zl = open("./safe/banknoty/50zl", "r+").read()

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
            ##########################
            # Wyświetlanie Okienka #2
            ##########################
            window_two = gui.Window("Automat MPK", layout_two)

            suma = float("{:.3f}".format(suma))
            reszta_do_zaplaty = suma

            while True:
                event, values = window_two.read()
                # Dodaj ilość
                if event == "+":
                    ilosc_waluty += 1
                    window_two['-ILOSC-WALUTY-'].update(ilosc_waluty)

                # Odejmuj ilość
                if event == "-":
                    ilosc_waluty += -1
                    if ilosc_waluty <= 0:
                        ilosc_waluty = 0
                    window_two['-ILOSC-WALUTY-'].update(ilosc_waluty)

                # Zeruj ilość
                if event == "Zeruj":
                    ilosc_waluty = 0
                    window_two['-ILOSC-WALUTY-'].update(ilosc_waluty)

                # Przycisk - 1gr
                if event == "1gr":
                    wrzucam = (automat[1] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_1gr += (automat[1] * ilosc_waluty)
                    suma_1gr = float("{:.3f}".format(suma_1gr))
                    print(f"{suma_1gr} - Wrzucono w sumie")

                    # suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_1gr += reszta_do_zaplaty
                        suma_1gr = float("{:.3f}".format(suma_1gr))
                        # Czy jest wystarczająco monet do wydania reszty
                        odczyt = float(ilosc_1gr) - float(ilosc_waluty)
                        if odczyt <= 0:
                            gui.popup(f"Brak monet 1gr do wydania, prosimy o wrzucić wyrównaną sumę - zwrócono resztę: {wrzucam} zł")
                            pass

                        #Dodaj do automatu
                        dodaj_do_automatu = float(ilosc_1gr) + float(ilosc_waluty)
                        ilosc_1gr.write(int(ilosc_waluty))
                        # Spradza co dzieje się dalej
                        print(suma_1gr)
                        print(suma)
                        print(reszta_do_zaplaty)

                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")
                # Koniec testu na 1gr

                # Przycisk - 2gr
                if event == "2gr":
                    wrzucam = (automat[2] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_2gr += (automat[2] * ilosc_waluty)
                    suma_2gr = float("{:.3f}".format(suma_2gr))
                    print(f"{suma_2gr} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_2gr += reszta_do_zaplaty
                        suma_2gr = float("{:.3f}".format(suma_2gr))
                        # Spradza co dzieje się dalej
                        print(suma_2gr)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 5gr
                if event == "5gr":
                    wrzucam = (automat[3] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_5gr += (automat[3] * ilosc_waluty)
                    suma_5gr = float("{:.3f}".format(suma_5gr))
                    print(f"{suma_5gr} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_5gr += reszta_do_zaplaty
                        suma_5gr = float("{:.3f}".format(suma_5gr))
                        # Spradza co dzieje się dalej
                        print(suma_5gr)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk 10gr
                if event == "10gr":
                    wrzucam = (automat[4] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_10gr += (automat[4] * ilosc_waluty)
                    suma_10gr = float("{:.3f}".format(suma_10gr))
                    print(f"{suma_10gr} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_10gr += reszta_do_zaplaty
                        suma_10gr = float("{:.3f}".format(suma_10gr))
                        # Spradza co dzieje się dalej
                        print(suma_10gr)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 20gr
                if event == "20gr":
                    wrzucam = (automat[5] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_20gr += (automat[5] * ilosc_waluty)
                    suma_20gr = float("{:.3f}".format(suma_20gr))
                    print(f"{suma_20gr} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_20gr += reszta_do_zaplaty
                        suma_20gr = float("{:.3f}".format(suma_20gr))
                        # Spradza co dzieje się dalej
                        print(suma_20gr)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 50gr
                if event == "50gr":
                    wrzucam = (automat[6] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_50gr += (automat[6] * ilosc_waluty)
                    suma_50gr = float("{:.3f}".format(suma_50gr))
                    print(f"{suma_50gr} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_50gr += reszta_do_zaplaty
                        suma_50gr = float("{:.3f}".format(suma_50gr))
                        # Spradza co dzieje się dalej
                        print(suma_50gr)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 1zł
                if event == "1zł":
                    wrzucam = (automat[7] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_1zl += (automat[7] * ilosc_waluty)
                    suma_1zl = float("{:.3f}".format(suma_1zl))
                    print(f"{suma_1zl} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_1zl += reszta_do_zaplaty
                        suma_1zl = float("{:.3f}".format(suma_1zl))
                        # Spradza co dzieje się dalej
                        print(suma_1zl)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 2zł
                if event == "2zł":
                    wrzucam = (automat[8] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_2zl += (automat[8] * ilosc_waluty)
                    suma_2zl = float("{:.3f}".format(suma_2zl))
                    print(f"{suma_2zl} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_2zl += reszta_do_zaplaty
                        suma_2zl = float("{:.3f}".format(suma_2zl))
                        # Spradza co dzieje się dalej
                        print(suma_2zl)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 5zł
                if event == "5zł":
                    wrzucam = (automat[9] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_5zl += (automat[9] * ilosc_waluty)
                    suma_5zl = float("{:.3f}".format(suma_5zl))
                    print(f"{suma_5zl} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_5zl += reszta_do_zaplaty
                        suma_5zl = float("{:.3f}".format(suma_5zl))
                        # Spradza co dzieje się dalej
                        print(suma_5zl)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 10zł
                if event == "10zł":
                    wrzucam = (automat[10] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_10zl += (automat[10] * ilosc_waluty)
                    suma_10zl = float("{:.3f}".format(suma_10zl))
                    print(f"{suma_10zl} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_10zl += reszta_do_zaplaty
                        suma_10zl = float("{:.3f}".format(suma_10zl))
                        # Spradza co dzieje się dalej
                        print(suma_10zl)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 20zł
                if event == "20zł":
                    wrzucam = (automat[11] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_20zl += (automat[11] * ilosc_waluty)
                    suma_20zl = float("{:.3f}".format(suma_20zl))
                    print(f"{suma_20zl} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_20zl += reszta_do_zaplaty
                        suma_20zl = float("{:.3f}".format(suma_20zl))
                        # Spradza co dzieje się dalej
                        print(suma_20zl)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")

                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                # Przycisk - 50zł
                if event == "50zł":
                    wrzucam = (automat[12] * ilosc_waluty)
                    wrzucam = float("{:.3f}".format(wrzucam))
                    suma_50zl += (automat[12] * ilosc_waluty)
                    suma_50zl = float("{:.3f}".format(suma_50zl))
                    print(f"{suma_50zl} - Wrzucono w sumie")

                    suma = float("{:.3f}".format(suma))
                    print(f"{suma} - Suma do zapłaty")

                    reszta_do_zaplaty -= wrzucam  # tu był edit
                    reszta_do_zaplaty = float("{:.3f}".format(reszta_do_zaplaty))
                    print(f"{reszta_do_zaplaty} - Reszta do zapłaty\n---\n")

                    # Weryfikuje czy za dużo monet
                    if reszta_do_zaplaty < 0:
                        reszta = reszta_do_zaplaty * (-1)
                        reszta = float("{:.3f}".format(reszta))
                        suma_50zl += reszta_do_zaplaty
                        suma_50zl = float("{:.3f}".format(suma_50zl))
                        # Spradza co dzieje się dalej
                        print(suma_50zl)
                        print(suma)
                        print(reszta_do_zaplaty)
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - zwrócono resztę: {reszta} zł")


                    if reszta_do_zaplaty > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_do_zaplaty)
                        # gui.popup(f"Wrzucono: {suma_1gr} zł")
                        gui.popup(f"Wrzucono: {wrzucam} zł")

                    if reszta_do_zaplaty == 0:
                        reszta_do_zaplaty = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Bilet został wydrukowany - Dziękujemy!")

                if event == "Wróć" or gui.WIN_CLOSED:
                    ilosc_waluty = 0
                    suma = reszta_do_zaplaty
                    window_two.close()
                    break
                if event == "Wyjdź":
                    gui.popup("Do widzenia!")
                    exit()
