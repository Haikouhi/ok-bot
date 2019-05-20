# coding: utf8

import unittest
import QueryClass

class Test_query_class(unittest.TestCase):

    def setUp(self):
        self.connexion = QueryClass.pymysql.connect(host='localhost',
                                         user='foobar',
                                         password='foobar',  # add password
                                         db='chit_chat',
                                         charset='utf8mb4',
                                         cursorclass=QueryClass.pymysql.cursors.DictCursor
                                         )
        self.curseur = self.connexion.cursor()
        self.query = QueryClass.Query()

    def test_name(self):
        self.assertEqual(self.query.name('Théo'), 'Son nom est Flaus')
        self.assertEqual(self.query.name(''), 'Huuum, je ne connais pas cette personne ! ')
        self.assertRaises(TypeError, self.query.name, 'Bertrand')

    def test_date(self):
        self.assertEqual(self.query.date('Arthur'), 'Il est né le 01/04/1995')
        self.assertEqual(self.query.date('Caroline'), 'Elle est née le 29/12/1997')
        self.assertEqual(self.query.date('Théo'), 'Il est né le 16/09/1996')
        self.assertEqual(self.query.date(''), 'Huuum, je ne connais pas cette personne ! ')
        self.assertRaises(TypeError, self.query.date, 'Alice')

    def test_city(self):
        self.assertEqual(self.query.city('Théo'), 'Il habite à Lagnieu')
        self.assertEqual(self.query.city('Haikouhi'), 'Elle habite à Villeurbanne')
        self.assertEqual(self.query.city(''), 'Huuum, je ne connais pas cette personne ! ')
        self.assertRaises(TypeError, self.query.city, 'Alice')

    def test_number(self):
        self.assertEqual(self.query.number('Théo'), 'Son numéro de téléphone est 06 95 31 19 89')
        self.assertEqual(self.query.number('Haikouhi'), 'Son numéro de téléphone est 06 58 17 58 07')
        self.assertEqual(self.query.number(''), 'Huuum, je ne connais pas cette personne ! ')
        self.assertRaises(TypeError, self.query.number, 'Alice')

    def test_age(self):
        self.assertEqual(self.query.age('Théo'), 'Il a 22 ans')
        self.assertEqual(self.query.age('Haikouhi'), 'Elle a 29 ans')
        self.assertEqual(self.query.age(''), 'Huuum, je ne connais pas cette personne !')
        self.assertRaises(TypeError, self.query.mail, 'Alice')

    def test_mail(self):
        self.assertEqual(self.query.mail('Théo'), 'Son adresse email est flaus.theo69@gmail.com')
        self.assertEqual(self.query.mail('Haikouhi'), 'Son adresse email est h.oroudjian@protonmail.com')
        self.assertEqual(self.query.mail(''), 'Huuum, je ne connais pas cette personne !')
        self.assertRaises(TypeError, self.query.mail(''), 'Alice')


    def test_zodiac_sign(self):
        self.assertEqual(self.query.zodiac_sign('Théo'), 'Son signe est Vierge')
        self.assertEqual(self.query.zodiac_sign('Bachir'), 'Son signe est Cancer')
        self.assertEqual(self.query.zodiac_sign(''), 'Huuum, je ne connais pas cette personne ! ')
        self.assertRaises(TypeError, self.query.zodiac_sign, 'Alice')

    def test_anniversaire(self):
        self.assertEqual(self.query.anniversaire('Théo'), 'Son anniversaire est le 16 Septembre')
        self.assertEqual(self.query.anniversaire('Timothée'), 'Son anniversaire est le 3 Septembre')
        self.assertEqual(self.query.anniversaire(''), 'Huuum, je ne connais pas cette personne ! ')
        self.assertRaises(TypeError, self.query.anniversaire, 'Alice')

if __name__ == '__main__':

    unittest.main()