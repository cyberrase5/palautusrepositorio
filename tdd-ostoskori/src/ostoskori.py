from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        pass
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.tuotteet = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

        count = 0
        for item in self.tuotteet:
            count += item.lukumaara()

        return count

    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

        count = 0
        for item in self.tuotteet:
            count += item.hinta()

        return count

    def lisaa_tuotea(self, lisattava: Ostos):
        # lisää tuotteen
        self.tuotteet.append(lisattava)

    def lisaa_tuote(self, lisattava: Tuote):
        # lisää tuotteen

        for item in self.tuotteet:
            if item.tuote._nimi == lisattava._nimi:
                item.muuta_lukumaaraa(1)
                return

        self.tuotteet.append(Ostos(lisattava))


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        for item in self.tuotteet:
            if item.tuote._nimi == poistettava._nimi:
                item.muuta_lukumaaraa(-1)
                if item.lukumaara() < 1:
                    self.tuotteet.remove(item)
                    return
                return

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on

        return self.tuotteet
