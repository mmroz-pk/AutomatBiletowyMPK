import PySimpleGUI as gui

from data import Pieniadz


class Gui:

    def __init__(self):
        self.ilosc = 0
        self.suma = 0

        self.layout = [
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

        self.layout_two = [
            [gui.Text("-- Automat MPK --")],
            [gui.Text("Wyznacz wartość oraz ilość monet/banknot jakie zostaną wprowadzone do automatu")],
            [gui.Text("Uwaga! Automat nie wydaje reszty banknotom!")],
            [gui.Text("Prosimy o wprowadzenie wyliczonej sumy")],
            [gui.Text("---")],
            [gui.Text(f"Suma: {self.suma} zł", key='-SUMA-')],
            [gui.Text(f"Reszta do zapłaty:"), gui.Text(f"{self.suma}", key='-SUMA-ZMIENNA-'), gui.Text("zł")],
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

        self.evt = {"1": '20n', "2": '40n', "3": '60n', "4": '20u', "5": '40u', "6": '60u'}

        self.kasa = {"1": Pieniadz(2, "zl"), "2": Pieniadz(4, "zl"), "3": Pieniadz(6, "zl"),
                     "4": Pieniadz(1, "zl"), "5": Pieniadz(2, "zl"), "6": Pieniadz(3, "zl")}

        self.sztTMP = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}

        self.rozlicz = {"1gr": Pieniadz(0.01, "gr"),  "2gr": Pieniadz(0.02, "gr"), "5gr": Pieniadz(0.05, "gr"),
                        "10gr": Pieniadz(0.1, "gr"), "20gr": Pieniadz(0.2, "gr"), "50gr": Pieniadz(0.5, "gr"),
                        "1zł": Pieniadz(1, "gr"), "2zł": Pieniadz(2, "gr"), "5zł": Pieniadz(5, "gr"),
                        "10zł": Pieniadz(10, "gr"), "20zł": Pieniadz(20, "gr"), "50zł": Pieniadz(50, "gr")}

        self.window = gui.Window("Automat MPK", self.layout, size=(300, 540))
        self.window_two = None

        self.mainloop()

    def mainloop(self):
        while 1:
            event, values = self.window.read()
            if event == "Kup":
                self.platnosc()
            else:
                self.eventObsluga(event)

    def eventObsluga(self, ev):
        if ev == "Wyjdź":
            gui.popup("Do widzenia!")
            exit()

        if ev == gui.WIN_CLOSED:
            self.window.close()
            return

        if ev == "+":
            self.ilosc += 1
            self.zmien_ilosc_gui(self.ilosc)
            return

        if ev == "-":
            if self.ilosc == 0:
                return
            else:
                self.ilosc -= 1
                self.zmien_ilosc_gui(self.ilosc)
                return

        if ev == "Zeruj":
            self.ilosc = 0
            self.zmien_ilosc_gui(self.ilosc)
            return

        for x in self.evt.keys():
            if ev == x:
                tmp = self.ilosc - self.sztTMP.get(x)
                tmp_dict = {x: self.ilosc}
                self.sztTMP.update(tmp_dict)
                self.suma += self.kasa.get(x).wartosc * tmp
                self.window[self.evt.get(x)].update(f"{self.ilosc} szt.")
                self.window['-SUMA-'].update(self.suma)
                return
        return

    def platnosc(self):
        gui.Window("Automat MPK", self.layout_two, size=(300, 540))



    def zmien_ilosc_gui(self, ile):
        self.window['-ILOSC-'].update(ile)
