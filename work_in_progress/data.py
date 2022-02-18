class Pieniadz:
    def __init__(self, w: float, t: str):
        self.wartosc = w
        self.typ = t

    def wartosc(self):
        return self.wartosc


class Bilet:
    def __init__(self, c: str, k: float):
        self.czas = c
        self.koszt = k


class PrzechowywaczMonet:
    def __init__(self):
        self.lista_monet = [Pieniadz(50, "zł"), Pieniadz(20, "zł"), Pieniadz(10, "zł"), Pieniadz(5, "zł"),
                            Pieniadz(2, "zł"), Pieniadz(1, "zł"), Pieniadz(0.5, "gr"), Pieniadz(0.2, "gr"),
                            Pieniadz(0.1, "gr"), Pieniadz(0.05, "gr"), Pieniadz(0.02, "gr"), Pieniadz(0.01, "gr")]

        self.przechowalnia = []

    def dodaj(self, pieniadz: Pieniadz):
        self.przechowalnia.append(pieniadz)

    def wypisz(self):
        for y in self.przechowalnia:
            if y.typ == "gr":
                print(str(y.wartosc * 100) + " " + y.typ)
            else:
                print(str(y.wartosc) + " " + y.typ)
