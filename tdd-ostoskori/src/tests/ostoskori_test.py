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
        self.kori.lisaa_tuote(Ostos(maito))

        self.assertEqual(self.kori.tavaroita_korissa(), 1)

    def test_yhden_tuotteen_lisaamisen_jalkeen_korin_hinta_tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(Ostos(maito))

        self.assertEqual(self.kori.hinta(), 3)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(Ostos(maito))
        kaakao = Tuote("Kaakao", 5)
        self.kori.lisaa_tuote(Ostos(kaakao))

        self.assertEqual(self.kori.tavaroita_korissa(), 2)

    def test_kahden_tuotteen_lisaamisen_jalkeen_korin_hinta_2tuotteen_hinta(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(Ostos(maito))
        kaakao = Tuote("Kaakao", 5)
        self.kori.lisaa_tuote(Ostos(kaakao))

        self.assertEqual(self.kori.hinta(), 8)

    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_tavaraa(self):
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
