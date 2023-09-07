from pojistovna import Pojistovna

# Vytvoření instance Pojišťovny
moje_pojistovna = Pojistovna()

# Úvodní zobrazení
print("____________________")
print("Evidence pojištěných")
print("____________________")
print()
print("Vyberte si akci:")
print("1 - Přidat nového pojištěného")
print("2 - Vypsat všechny pojištěné")
print("3 - Vyhledat pojištěného")
print("0 - Konec")

# Zadaní volby
while True:
    volba = input("Zadejte číslo akce: ")
    if volba == "1":
        moje_pojistovna.pridat()
    elif volba == "2":
        moje_pojistovna.vypis()
    elif volba == "3":
        moje_pojistovna.vyhledat()
    elif volba == "0":
        break
    else:
        print("Tento znak nevede k žádné akci.")
