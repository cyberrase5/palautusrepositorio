import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    
    # step 2
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        kaakao = Tuote("Kaakao", 5)
        self.kori.lisaa_tuote(kaakao)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_2tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        kaakao = Tuote("Kaakao", 5)
        self.kori.lisaa_tuote(kaakao)

        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        ostos = Ostos(Tuote("Maito", 3))
        ostos.muuta_lukumaaraa(1)
        
        self.kori.lisaa_tuotea(ostos)

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_tupla_hinta(self):
        ostos = Ostos(Tuote("Maito", 3))
        ostos.muuta_lukumaaraa(1)
        
        self.kori.lisaa_tuote(ostos)

        self.assertEqual(self.kori.hinta(), 6)

        # step 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        # testaa että metodin palauttaman listan pituus 1
        self.assertEqual(len(ostokset), 1)

        # step 9
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)

        ostos = self.kori.ostokset()[0]

        # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.

        self.assertEqual(ostos.tuote._nimi, "Maito")
        self.assertEqual(ostos.tuote._hinta, 3)

    def test_kaksi_eri_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        kaakao = Tuote("Kaakao", 5)
        self.kori.lisaa_tuote(kaakao)

        ostos1 = self.kori.ostokset()[0]
        ostos2 = self.kori.ostokset()[1]

        self.assertEqual(ostos1.tuote._nimi, "Maito")
        self.assertEqual(ostos1.tuote._hinta, 3)

        self.assertEqual(ostos2.tuote._nimi, "Kaakao")
        self.assertEqual(ostos2.tuote._hinta, 5)

    def test_2_samaa_tuotetta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostokset = self.kori.ostokset()

        self.assertEqual(len(ostokset), 1)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_2_samaa_tuotetta_nimi_ja_lukumaara2(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)

        ostos1 = self.kori.ostokset()[0]

        self.assertEqual(ostos1.tuote._nimi, "Maito")
        self.assertEqual(ostos1.lukumaara(), 2)

    def test_2_samaa_tuotetta_poistetaan_toinen(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)

        ostos1 = self.kori.ostokset()[0]
        
        self.assertEqual(ostos1.lukumaara(), 1)

    def test_poistettu_tuote_tyhja_lista(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.poista_tuote(maito)
        
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
