KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS): # OK
        
        self.kapasiteetti = kapasiteetti

        self.kasvatuskoko = kasvatuskoko


        self.luvut = [0] * self.kapasiteetti

        self.alkioiden_lkm = 0


    def kasvata_taulukkoa(self):

        uusi = [0] * (self.kapasiteetti + self.kasvatuskoko)
        self.kopioi_taulukko(self.luvut, uusi)
        self.kapasiteetti = self.kapasiteetti + self.kasvatuskoko

        return uusi


        # vanhat

    def paskaa(self, index): # shiftaa taulukkoa
        for i in range(index, len(self.luvut)):
            if self.luvut[i + 1] == 0:
                break

            self.luvut[i] = self.luvut[i + 1]

    def lisaa(self, n): # True jos lisättiin, muuten false
        
        if not self.kuuluu(n):
            
            if self.mahtavuus() == self.kapasiteetti:
                self.luvut = self.kasvata_taulukkoa()

            self.luvut[self.mahtavuus()] = n
            self.alkioiden_lkm += 1

            return True

        return False

    def poista(self, n):
        
        if self.kuuluu(n):
            for i in range(0, len(self.luvut)):
                if self.luvut[i] == n:
                    self.luvut[i] = 0
                    self.alkioiden_lkm -= 1

                    self.paskaa(i) # shiftaa taulukkoa

                    return True


        return False

    def kopioi_taulukko(self, a, b): # OK
        for i in range(0, len(a)):
            b[i] = a[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.luvut[i]

        return taulu

    @staticmethod
    def yhdiste(a, b):
        uusi_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            uusi_taulu.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            uusi_taulu.lisaa(b_taulu[i])

        return uusi_taulu

    @staticmethod
    def leikkaus(a, b):
        uusi_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            for j in range(0, len(b_taulu)):
                if a_taulu[i] == b_taulu[j]:
                    uusi_taulu.lisaa(b_taulu[j])

        return uusi_taulu

    @staticmethod
    def erotus(a, b):
        uusi_taulu = IntJoukko()
        a_taulu = a.to_int_list()
        b_taulu = b.to_int_list()

        for i in range(0, len(a_taulu)):
            uusi_taulu.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            uusi_taulu.poista(b_taulu[i])

        return uusi_taulu

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.luvut[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.luvut[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.luvut[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos


    # omat apufunktiot
    
    def kuuluu(self, etsittava):
        for i in self.luvut:
            if etsittava == i:
                return True

        return False
