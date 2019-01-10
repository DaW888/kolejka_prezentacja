# Klasa odpowiadająca za utworzenie objektu z danymi.


class Węzeł:
    def __init__(self, dane):
        self.dane = dane      # inicjalizacja nowej danej
        self.następny = None  # utworzenie odnośnika do następnej danej
