import PySimpleGUI as gui


# Klasa przechowuje wartość oraz typ pieniądza
class Pieniadz:
    def __init__(self, w: float, t: str):
        self.wartosc = w
        self.typ = t

    def get_wartosc(self):
        return self.wartosc

    def get_typ(self):
        return self.typ


# Klasa przechowuje czas ważności oraz koszt biletów
class Bilet:
    def __init__(self, c: str, k: float):
        self.czas = c
        self.koszt = k


# Klasa przechowująca listę monet/banknotów
class PrzechowywaczMonet:
    def __init__(self):
        self.lista_monet = [Pieniadz(50, "zł"), Pieniadz(20, "zł"), Pieniadz(10, "zł"), Pieniadz(5, "zł"),
                            Pieniadz(2, "zł"), Pieniadz(1, "zł"), Pieniadz(0.5, "gr"), Pieniadz(0.2, "gr"),
                            Pieniadz(0.1, "gr"), Pieniadz(0.05, "gr"), Pieniadz(0.02, "gr"), Pieniadz(0.01, "gr")]

        self.przechowalnia = []

    def dodaj(self, pieniadz: Pieniadz):

        y = (lambda x: True if not (self.lista_monet.__contains__(pieniadz)) else False)

        if y(pieniadz):
            raise Exception("nie znaleziono takiej monety!")

        else:
            self.przechowalnia.append(pieniadz)

    def wypisz(self):
        for y in self.przechowalnia:
            if y.typ == "gr":
                print(str(y.wartosc * 100) + " " + y.typ)
            else:
                print(str(y.wartosc) + " " + y.typ)

    def get_reszta(self):
        return self.przechowalnia


# Klasa dziedzicząca po PrzechowywaczMonet, wypłaca monety/banknoty
class Wyplatomat(PrzechowywaczMonet):
    def __init__(self):
        super().__init__()

        # maksymalmna liczba monet
        self.max = 100

    # funkcja wyliczająca resztę
    def reszta(self, suma_wprowadzona_gotowka, suma):

        if suma_wprowadzona_gotowka < 0 or suma < 0:
            raise Exception()

        print(f"Reszta: {round((suma_wprowadzona_gotowka - suma), 3)}")

        tmpVal = round((suma_wprowadzona_gotowka - suma), 3)

        self.oblicz_reszte(self, tmpVal)

        if len(self.przechowalnia) > self.max:
            raise Exception()

        self.wypisz()
        gui.popup(f"Bilety zostały wydrukowane! - Zwrócono: {round((suma_wprowadzona_gotowka - suma), 3)} zł")

    # Funkcja statyczna wyliczająca resztę
    @staticmethod
    def oblicz_reszte(przech: PrzechowywaczMonet, koszt: float):
        while koszt > 0.0:
            for i in przech.lista_monet:
                if i.wartosc <= koszt:
                    przech.dodaj(i)
                    koszt -= i.wartosc
                    break
                if koszt < 0.01:
                    koszt = 0

        return przech
