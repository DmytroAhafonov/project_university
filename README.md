Projekt: System zarządzania użytkownikami

Ten projekt został stworzony dla zarządzania użytkownikami przy użyciu Flask (Python) oraz MongoDB.
Funkcjonalności:
1. Dodawanie nowych użytkowników (POST /users)
2. Wyświetlanie listy wszystkich użytkowników (GET /users)
3. Usuwanie użytkownika po ID (DELETE /users/<user_id>)

Struktura projektu:
- main.py – główny plik aplikacji, w którym znajdują się wszystkie endpointy API.
- database.py – konfiguracja połączenia z bazą MongoDB i inicjalizacja.
- models.py – modele danych zdefiniowane przy użyciu Pydantic i Beanie.
- test_api.py – testy API w Pytest.
- index.html – prosty interfejs webowy w HTML + JavaScript umożliwiający testowanie API bez Postmana.
- .env – plik z danymi konfiguracyjnymi.

Dlaczego MongoDB?
MongoDB jest bazą NoSQL, co pozwala na elastyczne przechowywanie danych w formacie dokumentów. W tym projekcie przechowujemy informacje o użytkownikach (imię, email) w kolekcji „users”.

Jak działa aplikacja:
Po uruchomieniu serwera Flask API udostępnia endpointy, które można wywoływać z poziomu przeglądarki (index.html) lub narzędzi typu Postman. Dzięki dodaniu CORS możliwe jest wysyłanie zapytań bezpośrednio z pliku HTML uruchomionego lokalnie.

Dodatkowo w interfejsie HTML mamy trzy sekcje:
- formularz do dodawania użytkowników,
- przycisk do wyświetlania wszystkich użytkowników,
- pole i przycisk do usuwania użytkowników po ID.

Całość pozwala w prosty sposób przetestować działanie bazy i API.
