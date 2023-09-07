from pojisteny import Pojisteny
class Pojistovna:
    # Třída reprezentuje seznam pojištěných s možností vyhledat, vypsat a přidat.

    def __init__(self):
        self.seznam_pojistenych = [Pojisteny("Marek", "Novák", 23, 123456789),
                                   Pojisteny("Lukáš", "Marek", 34, 987654321),
                                   Pojisteny("Lucie", "Marková", 30, 774878493)]

    # Metoda přidá nového pojištěného.
    def pridat(self):
        jmeno = input("Zadejte jméno: ")
        prijmeni = input("Zadejte přijmení: ")
        vek = input("Zadejte věk: ")
        tel_cislo = input("Zadejte telefonní číslo: ")
        novy_pojistenec = Pojisteny(jmeno, prijmeni, vek, tel_cislo)
        self.seznam_pojistenych.append(novy_pojistenec)
        print("Data byla uložena, porkačujte libovolnou klávesou...")

    # Metoda vypíše seznam všech pojištěných..
    def vypis(self):
        for pojistenec in self.seznam_pojistenych:
            print(pojistenec)

    # Metoda vyhledá pojištěné podle jména nebo příjmení.
    def vyhledat(self):
        vstup = input("Zadejte jméno nebo přijmení: ")

        for pojistenec in self.seznam_pojistenych:
            if pojistenec.jmeno.lower() == vstup.lower() or pojistenec.prijmeni.lower() == vstup.lower():
                print(pojistenec)
        else:
            print("Další jméno nebo příjmení nelze nalést")
