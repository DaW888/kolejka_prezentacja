from collections import deque

q = deque()  # deque(maxlen=3) - mozna rowniez podac max dlugosc kolejki

print(' from collections import deque '.center(70, '='))
print('')
print(' Dodawanie elementów do kolejki '.center(70, "-"))
q.append('raz')
q.append('dwa')  # dodawanie po kolei
q.append('trzy')
print(q)
q.appendleft('przed raz')  # dodawanie jako pierwszy lewy element
print(q)
print(len(q))  # ilosc elementow w kolejce

print('')
print(' Liczenie ile razy element wystąpił '.center(70, "-"))
print(q.count('raz'))  # jeśli jest taki element to wyświetli 1, jeśli nie to 0
q.append('raz')
print(q.count('raz'))
q.pop()
print(q)


print('')
print(' Rozszerzanie kolejki '.center(70, "-"))
print(q.popleft())  # pobieramy pierwszy dodany elemenet
print(q.popleft())
print(q)
q.extend(['cztery', 'piec'])  # rozszerzamy kolejkę o całą tablice
print(q)

print('')
print(' Znajdowanie konkretnego elementu w kolejce '.center(70, "-"))
q.extendleft(['raz'])
q.append('raz')
print(q)
print(q.index('raz'))
print(q.index('raz', 2, 6))
print(q.pop())
print(q)


print('')
print(' Odwracanie (revers) całej kolejki '.center(70, "-"))
print(q)
q.reverse()
print(q)
q.reverse()


print('')
print(' Wstawianie elementu w Konkretne miejsce kolejki '.center(70, "-"))
q.insert(1, 'jeden i pol')
print(q)


print('')
print(' Rotacja/Przesunięcie kolejki '.center(70, "-"))
q.rotate(1)
q.rotate(1)
print(q)


print('')
print(' Czyszczenie tablicy '.center(70, '-'))
print(q)
q.clear()
print(q)
