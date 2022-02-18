import unittest

from data import Wyplatomat, Pieniadz
from gui import Gui

# Testy według poleceń z PDF

class KodTest(unittest.TestCase):

    def test_test1(self):
        wypl1 = Wyplatomat()

        # odliczona kwota
        wypl1.reszta(10, 10)

        buf = 0.0
        result = [buf := buf + num.wartosc for num in wypl1.przechowalnia]

        assert (0.0 == buf)

    def test_test2(self):
        wypl2 = Wyplatomat()

        # oczekiwana reszta
        wypl2.reszta(12, 10)

        buf = 0.0
        result = [buf := buf + num.wartosc for num in wypl2.przechowalnia]

        assert (2.0 == buf)

    def test_test3(self):
        wypl3 = Wyplatomat()

        # oczekiwany blad - Exception
        try:
            wypl3.reszta(19424112, 10)
        except Exception:
            assert (True)

    def test_test4(self):
        wypl4 = Wyplatomat()
        wypl4.przechowalnia = [Pieniadz(0.01, "gr")]
        wypl4.reszta(1.01, 0.01)

        buf = 0.00
        result = [buf := buf + num.wartosc for num in wypl4.przechowalnia]
        assert (1.01 == buf)

    def test_test5(self):
        gui5 = Gui()

        gui5.ilosc = 1
        gui5.oblicz_sume("3")
        gui5.oblicz_sume("6")

        assert (9 == gui5.suma)

    def test_test6(self):
        gui6 = Gui()

        gui6.ilosc = 1
        gui6.ilosc2 = 1
        gui6.oblicz_sume("3")
        gui6.zlicz_gotowke("5zł")
        gui6.zlicz_gotowke("1zł")

        gui6.oblicz_sume("6")
        gui6.zlicz_gotowke("1zł")
        gui6.zlicz_gotowke("2zł")

        assert (0 == (gui6.suma_wprowadzona_gotowka - gui6.suma))

    def test_test7(self):
        gui7 = Gui()

        try:
            gui7.wyplatomat.reszta(-1, -2)
        except Exception:
            assert (True)


if __name__ == '__main__':
    unittest.main()
