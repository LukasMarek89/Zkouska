class Pojisteny:
    # Třída reprezenuje pojištěného jednotlivce.

    def __init__(self, jmeno, prijmeni, vek, tel_cislo):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.vek = vek
        self.tel_cislo = tel_cislo

    def __str__(self):
        return f"{self.jmeno} \t   {self.prijmeni} \t {self.vek} let \t {self.tel_cislo}"
