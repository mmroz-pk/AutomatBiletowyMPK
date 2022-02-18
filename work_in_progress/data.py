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
