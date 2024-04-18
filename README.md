# Iris Classification
# Algorytm k-najbliższych sąsiadów (k-NN)

Ten program implementuje algorytm k-najbliższych sąsiadów (k-NN) w celu klasyfikacji przykładów. 
Algorytm wykorzystuje odległość euklidesową do obliczenia odległości między wektorami oraz głosowanie 
większościowe na podstawie klas najbliższych sąsiadów.

## Opis działania

1. Wczytywanie danych:
   - Dane treningowe i testowe są wczytywane z plików tekstowych.
   - Plik `iris_training.txt` zawiera dane treningowe.
   - Plik `iris_test.txt` zawiera dane testowe.

2. Obliczanie odległości:
   - Dla każdego przykładu z danych testowych, obliczana jest odległość euklidesowa między tym przykładem a każdym przykładem z danych treningowych.
   - Odległości są sortowane od najmniejszej do największej.

3. Wybór najbliższych sąsiadów:
   - Na podstawie posortowanych odległości wybierane jest k najbliższych sąsiadów.
   - Liczba k jest określana przez użytkownika.

4. Klasyfikacja:
   - Obliczana jest klasa, do której należy większość wybranych sąsiadów (głosowanie większościowe).
   - Klasyfikowana klasa jest porównywana z rzeczywistą klasą przykładu z danych testowych.

5. Dokładność klasyfikacji:
   - Obliczana jest dokładność klasyfikacji na podstawie liczby poprawnie sklasyfikowanych przykładów.
   - Wynik jest wyrażany jako procent.

## Instrukcja użytkowania

1. Upewnij się, że masz zainstalowany interpreter Python w wersji 3.x.

2. Pobierz pliki `iris_training.txt`, `iris_test.txt` oraz `knn_classifier.py` do tego samego folderu.

3. Uruchom program poprzez uruchomienie pliku `knn_classifier.py` w interpreterze Python.

4. Postępuj zgodnie z instrukcjami wyświetlanymi na ekranie.
   - Podaj wartość parametru k (liczba całkowita większa od zera).
   - Wynik dokładności klasyfikacji zostanie wyświetlony na ekranie.

5. Możesz powtarzać proces klasyfikacji, podając różne wartości parametru k.

---

Ten program został stworzony w celach edukacyjnych. Implementuje algorytm k-NN jako prosty przykład klasyfikacji.
