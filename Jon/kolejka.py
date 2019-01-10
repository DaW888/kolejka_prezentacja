from węzeł import Węzeł

# Klasa odpowiadająca za przeprowadzanie operacji na kolejce


class Kolejka:
    def __init__(self):
        # Inicjalizacja danych
        self.początek = None
        self.koniec = None

    def czyPusty(self):
        # Metoda odpowiadająca za sprawdzenie pierwszego elementu kolejki
        return not self.początek

    def odkolejkuj(self):
        # Metoda odpowiadająca za usunięcie danych z kolejki
        dane = self.początek.dane
        self.początek = self.początek.następny
        if self.czyPusty():         # Zabezpieczenie na wypadek braku następnego elementu
            self.koniec is None
        return dane

    def zakolejkuj(self, dane):
        # Metoda odpowiadająca za dodanie danych do kolejki
        nowe_dane = Węzeł(dane)
        if self.czyPusty():
            self.początek = self.koniec = nowe_dane
        else:
            self.koniec.następny = nowe_dane
            self.koniec = nowe_dane

    def zerknij(self):
        # Metoda odpowiadająca za zwrócenie pierwszego elementu kolejki
        return self.początek.dane
