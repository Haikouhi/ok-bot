import pymysql # language sql
import datetime # gestion des dates
from bs4 import BeautifulSoup
import requests

class Query(): # gère toutes les req

    def __init__(self): # initialisation où l'on se connecte à notre db

        self.connexion = pymysql.connect(host='localhost',
                                    user='foobar',
                                    password='foobar', # add password
                                    db='chit_chat',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor
                                    )
        self.curseur = self.connexion.cursor()

    def firstname_list(self): # renvoie la liste des prenoms dans la db

        list = [] # init de la liste que l'on va return

        sql = "SELECT firstname FROM class" # cmd sql...
        self.curseur.execute(sql) # on l'execute...
        data = self.curseur.fetchall() # on stock le resultat...
        for person in data: # on parcourt...
            list.append(person["firstname"]) # on ajoute la réponse dans la liste

        return list


    def name(self, firstname):  # pour recup' le nom


        if firstname != "": # on s'assure que firstname n'est pas nul
            sql = "SELECT lastname, gender FROM class WHERE firstname = '{}'".format(firstname) # req sql avec prenom en param...
            self.curseur.execute(sql) # on execute...
            output = self.curseur.fetchone() # on recup le output...
            if output["gender"] == "M":
                return "Son nom est " + output["lastname"]
            else:
                return "Son nom est " + output["lastname"]
        else: # si firstname n'est pas dans db :
            return "Huuum, je ne connais pas cette personne ! "

# defining birthdate for any chosen name:
    def date(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            date_courte = output["birthdate"]
            d = date_courte.day
            m = date_courte.month
            y = date_courte.year
            if output["gender"] == "M":
                return "Il est né le " + str(d) + "/" + "0" + str(m) + "/" + str(y)
            else:
                return "Elle est née le" + str(d) + "/" + "" + str(m) + "/" + str(y)
        else:
            return "Huuum, je ne connais pas cette personne ! "


# defining city for any chosen name:
    def city(self, firstname):

        if firstname != "":
            sql = "SELECT city, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            if output["gender"] == "M":
                return "Il habite à " + str(output["city"])
            else:
                return "Elle habite à " + str(output["city"])
        else:
            return "Huuum, je ne connais pas cette personne ! "


# defining phone number for any chosen name:
    def number(self, firstname):

        if firstname != "":
            sql = "SELECT phone_number, gender FROM class WHERE firstname ='{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            if output["gender"] == "M":
                return "Son numéro de téléphone est +33" + str(output["phone_number"])
            else:
                return "Son numéro de téléphone est +33" + str(output["phone_number"])

        else:
            return "Huuum, je ne connais pas cette personne ! "

    def age(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            date = output["birthdate"]

            now = datetime.datetime.now()

            if date.month <= now.month:
                if date.day <= now.day:
                    person_age = now.year - date.year
            else:
                person_age = now.year - date.year - 1

            if output["gender"] == "M":
                return "Il a {} ans".format(person_age)
            else:
                return "Elle a {} ans".format(person_age)

        else:
            return "Huuum, je ne connais pas cette personne !"

    def mail(self, firstname):

        if firstname != "":
            sql = "SELECT email, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            if output["gender"] == "M":
                return "Son adresse email est " + str(output["email"])
            else:
                return "Son adresse email est " + str(output["email"])
        else:
            return "Huuum, je ne connais pas cette personne !"

    def zodiac_sign(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            date = output["birthdate"]

            if (date.month == 3 and date.day >= 21) or (date.month == 4 and date.day <= 19):
                sign = "Belier"
            elif (date.month == 4 and date.day >= 20) or (date.month == 5 and date.day <= 20):
                sign = "Taureau"
            elif (date.month == 5 and date.day >= 21) or (date.month == 6 and date.day <= 20):
                sign = "Gémeaux"
            elif (date.month == 6 and date.day >= 21) or (date.month == 7 and date.day <= 22):
                sign = "Cancer"
            elif (date.month == 7 and date.day >= 23) or (date.month == 8 and date.day <= 23):
                sign = "Lion"
            elif (date.month == 8 and date.day >= 24) or (date.month == 9 and date.day <= 22):
                sign = "Vierge"
            elif (date.month == 9 and date.day >= 23) or (date.month == 10 and date.day <= 22):
                sign = "Balance"
            elif (date.month == 10 and date.day >= 23) or (date.month == 11 and date.day <= 21):
                sign = "Scorpion"
            elif (date.month == 11 and date.day >= 22) or (date.month == 12 and date.day <= 21):
                sign = "Sagittaire"
            elif (date.month == 12 and date.day >= 22) or (date.month == 1 and date.day <= 19):
                sign = "Capricorne"
            elif (date.month == 1 and date.day >= 20) or (date.month == 2 and date.day <= 19):
                sign = "Verseau"
            else:
                sign = "Poisson"

            if output["gender"] == "M":
                return sign
            else:
                return sign

        else:
            return "Huuum, je ne connais pas cette personne ! "

    def anniversaire(self, firstname):

        if firstname != "":
            sql = "SELECT birthdate, gender FROM class WHERE firstname = '{}'".format(firstname)
            self.curseur.execute(sql)
            output = self.curseur.fetchone()
            date_courte = output["birthdate"]
            d = date_courte.day
            m = date_courte.month
            y = date_courte.year
            if output["gender"] == "M":
                return "Son anniversaire est le " + str(d) + "/" + "0" + str(m)
            else:
                return "Son anniversaire est le " + str(d) + "/" + "0" + str(m)
        else:
            return "Huuum, je ne connais pas cette personne ! "


    def horoscope(self, firstname):
        requete = requests.get("https://www.20minutes.fr/horoscope/")
        page = requete.content
        soup = BeautifulSoup(page, "html.parser")

        signe = soup.find_all("h2", {"class": "titleblock-titles-title"})

        p = soup.find_all("p", {"class": "mb2"})

        horoscope = {}

        for i in range(len(signe)):
            horoscope[signe[i].string.replace("Horoscope ", "")] = p[i * 2].string + p[i * 2 + 1].string

        person_sign = self.zodiac_sign(firstname)
        return horoscope[person_sign]

    def meteo(self):

        with open("key2.txt", "r") as file:
            weather_key = file.readline()
            weather_key = weather_key[:-1]

        s = requests.Session()

        URL = "http://api.openweathermap.org/data/2.5/forecast/daily?" \
              "lat=45.76&lon=4.84&cnt=14&mode=json&units=metric&lang=fr"

        params = {"APPID": weather_key}

        requete = s.get(url=URL, params=params)
        data = requete.json()
        print(data)