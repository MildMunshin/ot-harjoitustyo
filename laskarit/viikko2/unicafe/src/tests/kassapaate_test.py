import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassan_saldo_alussa_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)     
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_kateisosto_toimii_edullisten_lounaiden_kohdalla(self):
        self.kassapaate.syo_edullisesti_kateisella(300) == 60
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_kateisosto_toimii_maukkaiden_lounaiden_kohdalla(self):
        self.kassapaate.syo_maukkaasti_kateisella(500) == 100
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_kateisosto_edullisten_lounaiden_kohdalla_jos_maksu_ei_riittava(self):
        self.kassapaate.syo_edullisesti_kateisella(200) == 200
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kateisosto_maukkaiden_lounaiden_kohdalla_jos_maksu_ei_riittava(self):
        self.kassapaate.syo_maukkaasti_kateisella(300) == 300
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_edullisten_lounaiden_kohdalla(self):
        self.maksukortti = Maksukortti(1000)
        assert self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) == True
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_korttiosto_toimii_maukkaiden_lounaiden_kohdalla(self):
        self.maksukortti = Maksukortti(1000)
        assert self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) == True
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000,0)

    def test_korttiosto_edullisten_lounaiden_kohdalla_jos_maksu_ei_riita(self):
        self.maksukortti = Maksukortti(200)
        assert self.kassapaate.syo_edullisesti_kortilla(self.maksukortti) == False
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000,0)

    def test_korttiosto_maukkaiden_lounaiden_kohdalla_jos_maksu_ei_riita(self):
        self.maksukortti = Maksukortti(300)
        assert self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti) == False
        self.assertEqual(self.maksukortti.saldo, 300)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000,0)

    def test_kortille_rahaa_ladattaessa_kortin_saldo_muuttuu_kassan_kasvaa_samalla_mitalla(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 200)
        self.assertEqual(self.maksukortti.saldo, 400)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1002,0)

    def test_kortille_rahaa_ladattaessa_ladataan_negatiivinen_arvo(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -200)
        self.assertEqual(self.maksukortti.saldo, 200)
        self.assertEqual(self.kassapaate.kassassa_rahaa_euroina(), 1000,0)