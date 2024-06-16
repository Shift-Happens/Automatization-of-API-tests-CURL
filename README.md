# cw_03

## Opis
To repozytorium zawiera rozwiązania dwóch zadań z Listy 3:
1. Automatyzacja testów API z wykorzystaniem curl.
2. Automatyzacja procesów z wykorzystaniem Makefile.

## Struktura Projektu

```
cw_03
├── zadanie_1
│ └── api_test.py 
├── zadanie_2
│ ├── app.py
│ ├── test_app.py
│ ├── requirements.txt
│ └── Makefile
└── README.md
```

## Zadanie 1: Automatyzacja testów API z wykorzystaniem curl

### Opis
Ten skrypt automatyzuje testowanie endpointów API za pomocą curl. Skrypt wysyła żądania HTTP do wybranej publicznej API (w tym przypadku JSONPlaceholder) i sprawdza, czy odpowiedzi są poprawne (statusy HTTP i kluczowe elementy w odpowiedziach JSON).

### Uruchomienie
1. Upewnij się, że masz zainstalowany `curl`.
2. Przejdź do katalogu `zadanie_1`:
    ```sh
    cd zadanie_1
    ```
3. Uruchom skrypt:
    ```sh
    python api_test.py
    ```

### Wyniki
Skrypt wyświetla wyniki w formacie:
Test 1: PASSED
Test 2: FAILED - Response: ...

### Pliki
- `api_test.py`: Skrypt do testowania API.

### Kod

```
import subprocess
import json

def run_curl(url):
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
    return result.stdout.decode('utf-8')

def test_api(url, key_elements):
    response = run_curl(url)
    try:
        json_response = json.loads(response)
        if all(key in json_response for key in key_elements):
            return True, json_response
        else:
            return False, json_response
    except json.JSONDecodeError:
        return False, response

def main():
    tests = [
        {"url": "https://jsonplaceholder.typicode.com/posts/1", "keys": ["userId", "id", "title", "body"]},
        {"url": "https://jsonplaceholder.typicode.com/users/1", "keys": ["id", "name", "username", "email"]},
        {"url": "https://jsonplaceholder.typicode.com/comments/1", "keys": ["postId", "id", "name", "email", "body"]},
    ]

    for i, test in enumerate(tests, 1):
        passed, response = test_api(test["url"], test["keys"])
        if passed:
            print(f"Test {i}: PASSED")
        else:
            print(f"Test {i}: FAILED - Response: {response}")

if __name__ == "__main__":
    main()
```

## Zadanie 2: Automatyzacja procesów z wykorzystaniem Makefile

### Opis
Ten Makefile automatyzuje procesy testowania i uruchamiania aplikacji w Pythonie.

### Reguły
- `install`: Instaluje zależności (jeśli są).
- `test`: Uruchamia testy jednostkowe.
- `run`: Uruchamia aplikację.

### Uruchomienie
1. Przejdź do katalogu `zadanie_2`:
    ```sh
    cd zadanie_2
    ```
2. Instalacja zależności:
    ```sh
    make install
    ```
3. Uruchomienie testów:
    ```sh
    make test
    ```
4. Uruchomienie aplikacji:
    ```sh
    make run
    ```

### Pliki
- `app.py`: Prosta aplikacja w Pythonie.
- `test_app.py`: Testy jednostkowe dla aplikacji.
- `Makefile`: Makefile do automatyzacji procesów.

###Kod

app.py
```
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    print(hello())
```

test_app.py
```
import unittest
from app import hello

class TestApp(unittest.TestCase):

    def test_hello(self):
        self.assertEqual(hello(), "Hello, World!")

if __name__ == "__main__":
    unittest.main()
```

## Dokumentacja

### Zadanie 1: api_test.py
Skrypt `api_test.py` testuje trzy endpointy z API JSONPlaceholder, wysyłając żądania GET i sprawdzając, czy odpowiedzi zawierają wymagane kluczowe elementy. Wyniki są wyświetlane w czytelny sposób.

### Zadanie 2: Makefile
Makefile zawiera trzy główne reguły:
- `install`: Reguła do instalacji zależności.
- `test`: Reguła do uruchamiania testów jednostkowych.
- `run`: Reguła do uruchamiania aplikacji.

## Wymagania
- Python 3.x
- curl
- make

## Instalacja
1. Sklonuj to repozytorium:
    ```sh
    git clone https://github.com/twoj_login/cw_03.git
    ```
2. Postępuj zgodnie z instrukcjami uruchomienia dla każdego zadania.

## Autor
Arkadiusz Kubiszewski
