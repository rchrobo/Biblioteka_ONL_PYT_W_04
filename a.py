opcje = """
1 - dodaj uzytkownika
2 - wyświetl Uzytkownikow
3 - usun uzytkownikow
4 - wyjdz
"""
while True:
    opcja = input(opcje)

    if opcja == '4':
        break
    if opcja == '1':
        print("tutaj bede robił dodawanie użytkownika")
    elif opcja == '2':
        print("tutaj bede robił wyświetlanie uzytkownikow")
    elif opcja == '3':
        print("tutaj bede robił kasowanie użytkownika")