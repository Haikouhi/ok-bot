# coding: utf8

import azure.cognitiveservices.speech as speechsdk
import argparse

from Query import *
from text_to_speech import *
from constantes import *

import nltk # librairie qui permet de couper les phrases avec des tokens

def get_speech_key():
    parser = argparse.ArgumentParser()
    parser.add_argument("speech_key")
    args = parser.parse_args()
    return args.speech_key

def get_list_query_and_firstname(speeched_voice, firstname_list, word_dict):

    firstname = ""
    tokens = nltk.word_tokenize(speeched_voice.text)

    for elt in tokens:
        if elt.capitalize() in firstname_list:
            firstname = elt.capitalize()
        for k, v in word_dict.items():
            if elt.lower() in v:
                list_query.append(k.lower())

    return list_query, firstname

def make_queries(list_query, firstname):

    answer = ""

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
            answer += "Bonjour ! Je suis Alfred "
        elif elt == "ça_va":
            answer += "Je pète la forme"

    return answer





speech_key = get_speech_key()

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language="fr-FR")

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

continuer = True

while continuer:

    print("Dit quelquechose...")

    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:

        query = Query()

        firstname_list = query.firstname_list()


        list_query = []  # initialisation de la liste des requêtes que l'on va effectuer
        firstname = ""  # init vide pour les demandes de prenoms non connu par la db
        answer = ""  # init le message que le bot va envoyer


        list_query, firstname = get_list_query_and_firstname(result, firstname_list, word_dict)

        temp = 0
        for elt in list_query:
            if elt == "ça_va":
                temp += 1
        if temp ==1:
            list_query.remove("ça_va")

        list_query = set(list_query)
        answer = make_queries(list_query, firstname)


        if len(list_query) == 0:  # si liste des Query = 0...

            answer += "Je n'ai pas compris ce que vous vouliez"

        print(answer)
        app = TextToSpeech(speech_key, answer)
        app.get_token()
        app.save_audio()

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))