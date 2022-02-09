import PySimpleGUI as gui

# Wartość w groszach
automat = (0, 1, 2, 5, 10, 20, 50, 100, 200, 500, 1000, 2000, 5000)
cennik = (0, 200, 400, 600, 100, 200, 300)

######################
# Pieniądze przechowane w Automacie
######################

# Pobieranie informacji o ilości Monet
ilosc_1gr = open("./safe/monety/1gr").read()
ilosc_2gr = open("./safe/monety/2gr").read()
ilosc_5gr = open("./safe/monety/5gr").read()
ilosc_10gr = open("./safe/monety/10gr").read()
ilosc_20gr = open("./safe/monety/20gr").read()
ilosc_50gr = open("./safe/monety/50gr").read()
ilosc_1zl = open("./safe/monety/1zl").read()
ilosc_2zl = open("./safe/monety/2zl").read()
ilosc_5zl = open("./safe/monety/5zl").read()

# Pobieranie informacji o ilości Banknot
ilosc_10zl = open("./safe/banknoty/10zl").read()
ilosc_20zl = open("./safe/banknoty/20zl").read()
ilosc_50zl = open("./safe/banknoty/50zl").read()

suma = 0

suma_1gr = 0

suma_20n = 0
suma_40n = 0
suma_60n = 0

suma_20u = 0
suma_40u = 0
suma_60u = 0

ilosc = 0
ilosc_suma = 0
ilosc_waluty = 0

ilosc_20n = 0
ilosc_40n = 0
ilosc_60n = 0

ilosc_20u = 0
ilosc_40u = 0
ilosc_60u = 0

######################
# Główne Menu Automatu
######################
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
######################
# Stwórz okno
######################
window = gui.Window("Automat MPK", layout, size=(300, 540))

######################
# Pętla z warunkami
######################

######################
# Uwaga #1: Popraw weryfikatora, który dodaje ujemną liczbę sztuk biletów do automatu (testowano na bilecie #1) - done
# Uwagi #2: Jak dodasz funkcji dodania oraz odejmowania ilości, zacznij nad bramką płatności - done
# Uwagi #3: Jak będzie wszystko działać, spróbuj po troche modyfikować kod tak aby spełniał wymogi Pana Wojtasa - later
######################
while True:
    event, values = window.read()

    # Dodaj ilość
    if event == "+":
        ilosc += 1
        window['-ILOSC-'].update(ilosc)

    # Odejmuj ilość
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
            suma //= 100  # podziel przez 100
        suma_20n = cennik[1] * ilosc
        suma += suma_20n
        suma //= 100  # podziel przez 100
        ilosc_suma += ilosc
        ilosc_20n = ilosc
        window['-SUMA-'].update(suma)
        window['20n'].update(f"- (Wybrano {ilosc_20n} szt.)")

    # Przycisk - Bilet #2
    if event == "2":
        if suma_40n > 0:
            suma -= suma_40n
            suma //= 100  # podziel przez 100
        suma_40n = cennik[2] * ilosc
        suma += suma_40n
        suma //= 100  # podziel przez 100
        ilosc_suma += ilosc
        ilosc_40n = ilosc
        window['-SUMA-'].update(suma)
        window['40n'].update(f"- (Wybrano {ilosc_40n} szt.)")

    # Przycisk - Bilet #3
    if event == "3":
        if suma_60n > 0:
            suma -= suma_60n
            suma //= 100  # podziel przez 100
        suma_60n = cennik[3] * ilosc
        suma += suma_60n
        suma //= 100  # podziel przez 100
        ilosc_suma += ilosc
        ilosc_60n = ilosc
        window['-SUMA-'].update(suma)
        window['60n'].update(f"- (Wybrano {ilosc_60n} szt.)")

    # Przycisk - Bilet #4
    if event == "4":
        if suma_20u > 0:
            suma -= suma_20u
            suma //= 100  # podziel przez 100
        suma_20u = cennik[4] * ilosc
        suma += suma_20u
        suma //= 100  # podziel przez 100
        ilosc_suma += ilosc
        ilosc_20u = ilosc
        window['-SUMA-'].update(suma)
        window['20u'].update(f"- (Wybrano {ilosc_20u} szt.)")

    # Przycisk - Bilet #5
    if event == "5":
        if suma_40u > 0:
            suma -= suma_40u
            suma //= 100  # podziel przez 100
        suma_40u = cennik[5] * ilosc
        suma += suma_40u
        suma //= 100  # podziel przez 100
        ilosc_suma += ilosc
        ilosc_40u = ilosc
        window['-SUMA-'].update(suma)
        window['40u'].update(f"- (Wybrano {ilosc_40u} szt.)")

    # Przycisk - Bilet #6
    if event == "6":
        if suma_60u > 0:
            suma -= suma_60u
            suma //= 100  # podziel przez 100
        suma_60u = cennik[6] * ilosc
        suma += suma_60u
        suma //= 100  # podziel przez 100
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

    ######################
    # Przycisk - Kup (bramka płatności w trakcie budowy)
    ######################
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
        elif ilosc_suma > 0:
            ######################
            # Podsumowanie
            ######################
            layout_two = [
                [gui.Text("-- Automat MPK --")],
                [gui.Text("Wyznacz wartość oraz ilość monet/banknot jakie zostaną wprowadzone do automatu")],
                [gui.Text("Uwaga! Automat nie wydaje reszty - Prosimy wprowadź wyliczoną sumę")],
                [gui.Text("---")],
                [gui.Text(f"Suma: {suma} zł", key='-SUMA-')],
                [gui.Text(f"Do zapłaty:"), gui.Text(f"{suma} zł", key='-SUMA-ZMIENNA-')],
                [gui.Button("1gr"), gui.Button("2gr"), gui.Button("5gr"), gui.Button("10gr"), gui.Button("20gr"),
                 gui.Button("50gr")],
                [gui.Button("1zł"), gui.Button("2zł"), gui.Button("5zł"), gui.Button("10zł"), gui.Button("50zł")],
                [gui.Text("---")],
                [gui.Text("Ilość:"), gui.Text('0', key='-ILOSC-WALUTY-', size=(3, 1)), gui.Button("+"),
                 gui.Button("-")],
                [gui.Text("---")],
                [gui.Button("Zapłać"), gui.Button("Wróć")]
            ]

            ######################
            # Uwaga #4: Ustaw wartości float tak, aby nie wyświetlało więcej niż 2 cyfry po przecinku
            # Uwaga #5: Warunek if, który sprawdza czy ilość przekracza resztę do zapłaty należy naprawić, bo blokuje
            # Uwaga #6: Po przyciśnięciu "Zapłać", zweryfikuj ilośc monet/banknotów oraz zapisz je do safe'u
            # Uwaga #7: Napraw problem, gdzie bramka płatności nie chce działać po kliknięciu "Wróc" i poten "Kup"
            #####################

            window_two = gui.Window("Automat MPK", layout_two)
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
                    suma_1gr += (automat[1] * ilosc_waluty)
                    # suma_1gr //= 10  # podziel przez 10
                    suma_zmienna = suma  # nie trzeba dzielic, bo suma juz podzielona przez 100
                    reszta_suma_zmienna = suma_zmienna - suma_1gr

                    # Nie pobieraj jeśli reszta do zapłaty jest ujemna
                    if reszta_suma_zmienna < 0:
                        # Spradza co dzieje się dalej
                        print(suma_1gr)
                        print(suma_zmienna)
                        print(reszta_suma_zmienna)
                        gui.popup("Wprowadz wyliczoną sumę")
                    if reszta_suma_zmienna > 0:
                        window_two['-SUMA-ZMIENNA-'].update(reszta_suma_zmienna)
                        gui.popup(f"Wrzucono: {suma_1gr} zł")
                    if reszta_suma_zmienna == 0:
                        reszta_suma_zmienna = 0
                        window_two['-SUMA-ZMIENNA-'].update("zapłacono")
                        gui.popup(f"Zapłacono całą sumę")
                
                # draft
                if event == "2gr":
                    gui.popup("Awesome")
                if event == "5gr":
                    gui.popup("Awesome")
                if event == "10gr":
                    gui.popup("Awesome")
                if event == "20gr":
                    gui.popup("Awesome")
                if event == "50gr":
                    gui.popup("Awesome")
                if event == "1zł":
                    gui.popup("Awesome")
                if event == "2zł":
                    gui.popup("Awesome")
                if event == "5zł":
                    gui.popup("Awesome")
                if event == "10zł":
                    gui.popup("Awesome")
                if event == "20zł":
                    gui.popup("Awesome")
                if event == "50zł":
                    gui.popup("Awesome")

                if event == "Zapłać":
                    gui.popup("Awesome")
                if event == "Wróć" or event == gui.WIN_CLOSED:
                    window_two.close()
                    break
