# recruitmentTask

Wyznacz medianę wydatków do pierwszej niedzieli (włącznie) każdego miesiąca (np. dla 2023-09 i 2023-10 są to dni 1, 2, 3 wrz i 1 paź).
Należy zastosować rozwiązanie zgodnie z poniższym pseudokodem.


Copy
expenses = {
    "2023-01": {
        "01": {
            "food": [ 22.11, 43, 11.72, 2.2, 36.29, 2.5, 19 ],
            "fuel": [ 210.22 ]
        },
        "09": {
            "food": [ 11.9 ],
            "fuel": [ 190.22 ]
        }
    },
    "2023-03": {
        "07": {
            "food": [ 20, 11.9, 30.20, 11.9 ]
        },
        "04": {
            "food": [ 10.20, 11.50, 2.5 ],
            "fuel": []
        }
    },
    "2023-04": {}
};

func solution(expenses) {
    result = null;
    // ...
    return result;
}
println(solution(expenses));

Uwagi
1. Należy użyć tylko funkcji/modułów ze standardowej biblioteki (np. math).
2. Po przesłaniu poprawnego wyniku:
   1. przesłany plik jest finalnym rozwiązaniem
   2. uruchomione zostaną testy automatyczne (na różnych danych) badające zużycie pamięci i procesora dla funkcji solution
3. Zadanie może zostać wykonane w języku Python lub JavaScript.
4. Wynik to jedna liczba dla danych spełniających kryteria lub null.
