import PySimpleGUI as gui

cennik = [0, 2, 4, 6, 1, 2, 3]

suma = 0
ilosc_suma = 0

ilosc = 0
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
    [gui.Text("Ilość:"), gui.Text('0', key='-ILOSC-', size=(3, 1)), gui.Button("+"), gui.Button("-"), gui.Button("Zeruj")],
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
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "+":
        ilosc += 1
        window['-ILOSC-'].update(ilosc)

    if event == "-":
        ilosc += -1
        window['-ILOSC-'].update(ilosc)

    if event == "Zeruj":
        ilosc = 0
        window['-ILOSC-'].update(ilosc)
    # Bilet #1
    if event == "1":
        if ilosc == 0:
            suma += 0
            ilosc_suma += 0
            ilosc_20n += 0
            window['-SUMA-'].update(suma)
            gui.popup("Podaj ilość")
        if ilosc > 0:
            suma += cennik[1] * ilosc
            ilosc_suma += ilosc
            ilosc_20n += ilosc
            window['-SUMA-'].update(suma)
            # gui.popup("Dodano bilet #1")
            window['20n'].update(f"- (Wybrano {ilosc_20n} szt.)")
        if ilosc < 0:
            suma += cennik[1] * ilosc
            ilosc_suma += ilosc
            ilosc_20n += ilosc
            window['-SUMA-'].update(suma)
            # gui.popup("Dodano bilet #1")
            window['20n'].update(f"- (Wybrano {ilosc_20n} szt.)")
    # Bilet #2
    if event == "2":
        suma += cennik[2]
        ilosc_suma += 1
        ilosc_40n += 1
        window['-SUMA-'].update(suma)
        gui.popup("Dodano bilet #2")
        window['40n'].update(f"- (Wybrano {ilosc_40n} szt.)")
    # Bilet #3
    if event == "3":
        suma += cennik[3]
        ilosc_suma += 1
        ilosc_60n += 1
        window['-SUMA-'].update(suma)
        gui.popup("Dodano bilet #3")
        window['60n'].update(f"- (Wybrano {ilosc_60n} szt.)")
    # Bilet #4
    if event == "4":
        suma += cennik[4]
        ilosc_suma += 1
        ilosc_20u += 1
        window['-SUMA-'].update(suma)
        gui.popup("Dodano bilet #4")
        window['20u'].update(f"- (Wybrano {ilosc_20u} szt.)")
    # Bilet #5
    if event == "5":
        suma += cennik[5]
        ilosc_suma += 1
        ilosc_40u += 1
        window['-SUMA-'].update(suma)
        gui.popup("Dodano bilet #5")
        window['40u'].update(f"- (Wybrano {ilosc_40u} szt.)")
    # Bilet #6
    if event == "6":
        suma += cennik[6]
        ilosc_suma += 1
        ilosc_60u += 1
        window['-SUMA-'].update(suma)
        gui.popup("Dodano bilet #6")
        window['60u'].update(f"- (Wybrano {ilosc_60u} szt.)")
    # Wyzeruj wszystko
    if event == "Wyzeruj":
        suma = 0
        ilosc_suma = 0
        ilosc = 0
        window['20n'].update("")
        window['40n'].update("")
        window['60n'].update("")
        window['20u'].update("")
        window['40u'].update("")
        window['60u'].update("")
        window['-SUMA-'].update(suma)
        window['-ILOSC-'].update(ilosc)
        gui.popup("Wyzerowano!")
    # Wyjdź z Automatu
    if event == "Wyjdź" or event == gui.WIN_CLOSED:
        gui.popup("Do widzenia!")
        exit()
    # Kupujemy (w budowie)
    if event == "Kup":
        if ilosc_suma <= 0:
            gui.popup("Nie wybrano biletu!")
        elif ilosc_suma > 0:
            gui.popup("Płacimy :)")
            ######################
            # Podsumowanie
            ######################
            layout_two = [
                [gui.Text("-- Automat MPK --")],
                [gui.Text("---")],
                [gui.Text(f"Suma: {suma} zł", key='-SUMA-')],
                [gui.Button("1"), gui.Button("2"), gui.Button("3"), gui.Button("4"), gui.Button("5"), gui.Button("6")],
                [gui.Text("---")],
                [gui.Button("Zapłać"), gui.Button("Modyfikuj"), gui.Button("Wróć")]
            ]

            window_two = gui.Window("Automat MPK", layout_two)
            event, values = window_two.read()

            if event == "1":
               gui.popup("Awesome")
            if event == "Zapłać":
               gui.popup("Awesome")
            if event == "Wróć" or event == gui.WIN_CLOSED:
               gui.popup("Awesome")
               window_two.close()
