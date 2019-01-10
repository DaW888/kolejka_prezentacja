# Plik główny
from kolejka import Kolejka

kolejeczka = Kolejka()

# Dodajemy dane do kolejki
kolejeczka.zakolejkuj("Ślażyński")
kolejeczka.zakolejkuj("Wajda")
kolejeczka.zakolejkuj("Mazur")
kolejeczka.zakolejkuj("Bobula")
kolejeczka.zakolejkuj("Gębski")

# Sprawdzamy pierwszy element kolejki
# Powinien być Ślażyński
print(kolejeczka.zerknij())

# Odkolejkowywujemy daną i sprawdzamy pierwszy element
kolejeczka.odkolejkuj()
print(kolejeczka.zerknij())

# I jeszcze pare razy dla testów
kolejeczka.odkolejkuj()
kolejeczka.odkolejkuj()
kolejeczka.odkolejkuj()
print(kolejeczka.zerknij())
