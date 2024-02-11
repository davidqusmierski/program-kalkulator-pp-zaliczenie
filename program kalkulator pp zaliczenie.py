#wprowadzenie imienia użytkownika
name = input("Podaj swoje imię: ").lower()
print("Cześć ", name, " jak mogę ci dzisiaj pomóc?")
#zaczynam pętlę abym mógł do niej wracać po zakończeniu operacji
while True:
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Dzielenie")
    print("4. Mnożenie")
    print("5. Potęgowanie")
    print("6. Pierwiastkowanie")
    print("7. Quiz matematyczny")
    wybor = input("Wybierz numer operacji: ")
    if wybor == "1":
        #wprowadzam dodawanie i za pomocą funkcji float konwertuje liczby na zmiennoprzecinkowe
        while True:
            x = float(input("Wybierz liczbę pierwszą: "))
            y = float(input("Wybierz liczbę drugą: "))
            result = x + y 
            print("Wynik to ", result)
            wybor = input("Czy chcesz kontynuować?").lower()
            if wybor == "tak":
                continue
            elif wybor == "nie":
                break
    if wybor == "2":
            #wprowadzam odejmowanie
            while True:
                x = float(input("Wybierz liczbę pierwszą: "))
                y = float(input("Wybierz liczbę drugą: "))
                result = x - y 
                print("Wynik to ", result)
                wybor = input("Czy chcesz kontynuować?").lower()
                if wybor == "tak":
                    continue
                elif wybor == "nie":
                    break
    if wybor == "3":
        #wprowadzam dzielenie zachowując warunek że użytkownik nie może dzielić przez 0
        while True:
            x = float(input("Wybierz liczbę pierwszą: "))
            y = float(input("Wybierz liczbę drugą: "))
            if x == 0 or y == 0:
                print("Nie można dzielić przez 0")
                continue
            else:
                result = x/y 
                print("Wynik to ", result)
                wybor = input("Czy chcesz kontynuować?").lower()
                if wybor == "tak":
                    continue
                elif wybor == "nie":
                    break
    if wybor == "4":
        #wprowadzam mnożenie
        while True:
            x = float(input("Wybierz liczbę pierwszą: "))
            y = float(input("Wybierz liczbę drugą: "))
            result = x * y 
            print("Wynik to ", result)
            wybor = input("Czy chcesz kontynuować?").lower()
            if wybor == "tak":
                continue
            elif wybor == "nie":
                break
    if wybor == "5":
        #wprowadzam potęgę bez funkcji math korzystając ze wzoru matematycznego dodając warunek że jeżeli liczba zostanie podniesiona do potęgi 0 to wynik równa się 1
        while True:
            x = float(input("Wybierz liczbę: "))
            y = float(input("Wybierz potegę: "))
            result = x * ((y - 1) * x)
            if y == 0:
                result = 1
            print("Wynik to ", result)
            wybor = input("Czy chcesz kontynuować?").lower()
            if wybor == "tak":
                continue
            elif wybor == "nie":
                break
    if wybor == "6":
        #wprowadzam potegowanie za pomocą funkcji import math która wprowadza moduł matematyczny
        while True:
            import math
            x = float(input("Wybierz liczbę: "))
            #dodaje stopień pierwiastka dla użytkownika
            degree = float(input("Wybierz stopień: "))
            #dodaje działanie na pierwiastku wybranym przez użytkownika
            cube_root = x ** (1.0 / degree)
            print("Pierwiastek ", degree, "stopnia z ", x, " to ", cube_root)
            wybor = input("Czy chcesz kontynuować?").lower()
            if wybor == "tak":
                continue
            elif wybor == "nie":
                break
    if wybor == "7":
        #wprowadzam quiz matematyczny
        while True:
            #dodaje funkcje random żeby móc losować liczby do pytań
            import random
            wybor = input("Witaj w quizie matematycznym. Będziesz musiał rozwiązać 5 prostych przykładów z wyżej wymienionych dziedzin. Czy chcesz kontynuować?")
            if wybor == "tak":
                print("Powodzenia!")
                #za pomocą funkcji random.randint losuje liczby od 0-10
                x = random.randint(0,10)
                y = random.randint(0,10)
                #daje int żeby przy pytaniu pokazywało pełne liczby
                wybor = int(input(f"1. Ile to jest {x} dodać {y}: "))
                sum_result = x + y 
                if wybor != sum_result:
                    #dodaje cx gdzie c to zmienna a x to jej numer do liczenia punktów użytkownika
                    c1 = 0 
                if wybor == sum_result:
                    c1 = 1
                x = random.randint(0,10)
                y = random.randint(0,10)
                wybor = int(input(f"2. Ile to jest {x} odjąć {y}: "))
                result = x - y 
                if wybor != result:
                    c2 = 0 
                if wybor == result:
                    c2 = 1
                #za pomocą funkcji random choice wprowadzam losowanie liczb z wybranych z góry
                x = random.choice([1000,1020,1040,1060,80])
                y = random.choice([2,10])
                #wprowadzam założenie że x musi być większy od y
                while x>y:
                    wybor = int(input(f"3. Ile to jest {x} podzielić na {y}: "))
                    result = x/y 
                    if wybor != result:
                        c3 = 0 
                    if wybor == result:
                        c3 = 1
                    break
                x = random.randint(0,10)
                y = random.randint(0,10)
                wybor = int(input(f"4. Ile to jest {x} razy {y}: "))
                result = x * y 
                if wybor != result:
                    c4 = 0 
                if wybor == result:
                    c4 = 1
                import math
                #importuje funkcje math i wybieram liczby z których pierwiastek drugiego stopnia zawsze da liczbę całkowitą
                x = random.choice([4,9,16,25,81])
                y = random.choice([4,9,16,25,81])
                degree1 = 2
                degree2 = 2
                cube_root1 = x ** (1.0 / degree1)
                cube_root2 = y ** (1.0 / degree2)
                #wprowadzam działanie gdzie mnoże oba pierwiastki
                product_result = cube_root1 * cube_root2
                wybor = int(input(f"5. Ile to jest pierwiastek drugiego stopnia z {x} razy pierwiastek drugiego stopnia z {y}: "))
                if wybor == product_result:
                    c5 = 1 
                if wybor != product_result:
                    c5 = 0
                #dodaje całą punktację i w zależności od uzyskanych punktów daje inny komunikat
                sum_result = c1 + c2 + c3 + c4 + c5 
                if sum_result > 3 and sum_result != 5:
                    print(f"Gratulacje bardzo dobrze ci poszło, zdobyłeś {sum_result} punktów z możliwych 5")
                if sum_result < 4 and sum_result != 0:
                    print(f"Dobrze ci poszło ale musisz jeszcze nad tym popracować. Zdobyłeś {sum_result} punktów z możliwych 5")
                if sum_result == 5:
                    print("Wow jestem pod wrażeniem! Udało ci się zdobyć maksymalną ilość punktów")
                if sum_result == 0:
                    print("Widzę że masz duże zaległości. Zdobyłeś 0 punktów. Popracuj nad tym, nie poddawaj się!")
                    break
            #jeśli użytkownik nie chce kontynuować quizu przerywam pentle
            if wybor == "nie":
                break
    else:
        print("Zły komunikat, spróbuj jeszcze raz")
           
