from Queue import Queue

tab = ["a", 2, 3.5]  # Tablica z danymi wpisywanymi do kolejki
aqueue = Queue(len(tab))  # Inicjalizacja kolejki

for item in tab:  # Dodawanie do kolejki
    aqueue.put(item)

# Pobieranie elementów z kolejki w kolejności: a, 2, 3.5
while not aqueue.is_empty():
    print(aqueue.get())
