class Biblioteka:
    lista_ksiazek = []
    lista_egzemplarzy = []
    lista_ostateczna = []
    czy_jest_w_liscie = False
    lista_czytelnikow = []

    def __init__(self, limit_wypozyczen):
        self.limit_wypozyczen = limit_wypozyczen

    def dodaj_egzemplarz_ksiazki(self, ksiazka):
        self.lista_ksiazek.append(ksiazka)
        return True

    def wypozycz(self, czytelnik, tytul):
        if len(czytelnik.lista_ksiazek_czytelnika) < 3:
            for ksiazkaa in self.lista_ksiazek:
                if ksiazkaa.tytul == tytul:
                    for ksiazka_czytelnika in czytelnik.lista_ksiazek_czytelnika:
                        if ksiazka_czytelnika.tytul == tytul:
                            return False
                    czytelnik.lista_ksiazek_czytelnika.append(ksiazkaa)
                    self.lista_ksiazek.remove(ksiazkaa)
                    return True
        return False

    def oddaj(self, nazwisko, tytul):
        for czytelnik in self.lista_czytelnikow:
            if czytelnik.nazwisko == nazwisko:
                for ksiazka_czytelnika in czytelnik.lista_ksiazek_czytelnika:
                    if ksiazka_czytelnika.tytul == tytul:
                        self.lista_ksiazek.append(ksiazka_czytelnika)
                        czytelnik.lista_ksiazek_czytelnika.remove(ksiazka_czytelnika)
                        return True
        return False


class Ksiazka:

    def __init__(self, tytul, autor, rok):
        self.tytul = tytul
        self.autor = autor
        self.rok = rok


class Egzemplarz:

    def __init__(self, rok_wydania, wypozyczony):
        self.rok_wydania = rok_wydania
        self.wypozyczony = wypozyczony


class Czytelnik:

    def __init__(self, nazwisko, lista_ksiazek_czytelnika):
        self.nazwisko = nazwisko
        self.lista_ksiazek_czytelnika = lista_ksiazek_czytelnika

liczba_krotek = input().strip()
n = int(liczba_krotek)
liczba_krotek = [input().strip(' ') for krotka in range(n)]
splitter = []
biblioteka = Biblioteka(10)

for ksiazkaInput in liczba_krotek:
    usun_nawias = ksiazkaInput.replace("(", "")
    usun_nawias2 = usun_nawias.replace(")", "")
    usun_cudzyslow = usun_nawias2.replace("\"", "")
    splitter = usun_cudzyslow.split(", ")
    if splitter[0].strip() == "dodaj":
        ksiazka = Ksiazka(tytul=splitter[1].strip(), autor=splitter[2].strip(), rok=splitter[3].strip())
        print(biblioteka.dodaj_egzemplarz_ksiazki(ksiazka))
    if splitter[0].strip() == "wypozycz":
        jest_juz_czytelnik = False
        tytul = splitter[2].strip()
        for czytelnik in biblioteka.lista_czytelnikow:
            if czytelnik.nazwisko == splitter[1].strip():
                jest_juz_czytelnik = True
                print(biblioteka.wypozycz(czytelnik, tytul))
                break
        if not jest_juz_czytelnik:
            nowy_czytelnik = Czytelnik(splitter[1].strip(), [])
            biblioteka.lista_czytelnikow.append(nowy_czytelnik)
            print(biblioteka.wypozycz(nowy_czytelnik, tytul))
    if splitter[0].strip() == "oddaj":
        nazwisko = splitter[1].strip()
        tytul = splitter[2].strip()
        print(biblioteka.oddaj(nazwisko, tytul))
