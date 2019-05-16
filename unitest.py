# coding: utf8

import unittest
import chatbot
from Query import *

class Test_make_queries(unittest.TestCase):

    def setUp(self):
        self.query = Query()

    def test_base(self):
        self.assertEqual(chatbot.make_queries(self.query, ["mail"], "Theo"),
                         "Son adresse email est flaus.theo69@gmail.com\n")
        self.assertEqual(chatbot.make_queries(self.query, ["salut", "ça_va"], " "),
                         "Bonjour ! Je suis Alfred\nJe pète la forme\n")

    def test_unknown_person(self):
        self.assertEqual(chatbot.make_queries(self.query, ["age"], ""),
                         "Huuum, je ne connais pas cette personne !\n")

    def test_empty_query(self):
        self.assertEqual(chatbot.make_queries(self.query, [], "Caroline"),
                         "Je n'ai pas compris ce que vous vouliez")

if __name__ == "__main__":
     unittest.main()




