class Queue:

    def __init__(self, size):  # Inicjalizacja
        self.size = size
        self.n = size + 1  # Faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # Pierwszy do pobrania
        self.tail = 0  # Pierwsze wolne

    def is_empty(self):  # Sprawdza czy pusta
        return self.head == self.tail

    def is_full(self):  # Sprawdza czy pełna
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):  # Dodaje do kolejki
        self.items[self.tail] = data
        self.tail = (self.tail + 1) % self.n

    def get(self):  # Pobiera z kolejki
        data = self.items[self.head]
        self.items[self.head] = None  # Usuwam nadmiar miejsc
        self.head = (self.head + 1) % self.n
        return data
