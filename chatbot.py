# coding: utf8

import argparse
from text_to_speech import *
import nltk
from constantes import *

def write_speech_key():
    parser = argparse.ArgumentParser()
    parser.add_argument("speech_key")
    args = parser.parse_args()
    with open(path_file, "w+") as file:
        file.write(args.speech_key)

def get_speech_key(path_file):
    if os.path.exists(path_file):
        with open(path_file, "r") as file:
            return file.readline()

def get_list_query_and_firstname(speeched_voice, firstname_list, word_dict):

    list_query = []
    firstname = ""
    tokens = nltk.word_tokenize(speeched_voice.text)

    for elt in tokens:
        if elt.capitalize() in firstname_list:
            firstname = elt.capitalize()
        for k, v in word_dict.items():
            if elt.lower() in v:
                list_query.append(k.lower())

    return list_query, firstname

def make_queries(query, list_query, firstname):

    answer = ""

    if len(list_query) == 0:  # si liste des Query = 0...

        answer += "Je n'ai pas compris ce que vous vouliez"
    else:

        for elt in list_query:
            if elt == "nom":
                answer += query.name(firstname) + '\n'
            elif elt == "date":
                answer += query.date(firstname) + '\n'
            elif elt == "anniversaire":
                answer += query.anniversaire(firstname) + '\n'
            elif elt == "horoscope":
                answer += query.horoscope(firstname) + '\n'
            elif elt == "adresse":
                answer += query.city(firstname) + '\n'
            elif elt == "numero":
                answer += query.number(firstname) + '\n'
            elif elt == "age":
                answer += query.age(firstname) + '\n'
            elif elt == "mail":
                answer += query.mail(firstname) + '\n'
            elif elt == "signe":
                answer += "Son signe est " + query.zodiac_sign(firstname) + '\n'
            elif elt == "bye":
                answer += "See you soon loser!"
            elif elt == "salut":
                answer += "Bonjour ! Je suis Alfred" + '\n'
            elif elt == "ça_va":
                answer += "Je pète la forme" + '\n'
            elif elt == "meteo":
                answer += query.meteo()

    return answer

def stop(list_query):
    if len(list_query) > 0:
        for elt in list_query:
            if elt == "bye":
                return False
            else:
                return True
    else:
        return True

def speak_answer(speech_key, answer):

    print(answer)
    app = TextToSpeech(speech_key, answer)
    app.get_token()
    app.save_audio()

def query_ca_va(list_query):

    temp = 0
    for elt in list_query:
        if elt == "ça_va":
            temp += 1
    if temp == 1:
        list_query.remove("ça_va")

    return list_query

def reinitialize_query(list_query):

    del list_query[:]
    return list_query
