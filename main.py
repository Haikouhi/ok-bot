import azure.cognitiveservices.speech as speechsdk

from Query import *
from text_to_speech import *
from constantes import *

from random import randint
import nltk # librairie qui permet de couper les phrases avec des tokens
import difflib

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Creates an instance of a speech config with specified subscription key and service region.
# Replace with your own subscription key and service region (e.g., "westus").
speech_key, service_region = "subscription_key", "francecentral"
speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language="fr-FR")

# Creates a recognizer with the given settings
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

while 1:

    print("Dit quelquechose...")

    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:

        query = Query()

        firstname_list = query.firstname_list()


        list_query = []  # initialisation de la liste des requêtes que l'on va effectuer
        firstname = ""  # init vide pour les demandes de prenoms non connu par la db
        answer = ""  # init le message que le bot va envoyer

        tokens = nltk.word_tokenize(result.text)  # permet de recupérer la réponse en tokens (mot par mot)

        for elt in tokens:
            if elt.capitalize() in firstname_list:
                firstname = elt.capitalize()
            for k, v in word_dict.items():
                if elt.lower() in v:
                    list_query.append(k.lower())

        temp = 0
        for elt in list_query:
            if elt == "ça_va":
                temp += 1
        if temp ==1:
            list_query.remove("ça_va")

        list_query = set(list_query)
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
                answer += "Bonjour ! Je suis Chit-Chat (: "
            elif elt == "ça_va":
                answer += "Je pète la forme"

        if len(list_query) == 0:  # si liste des Query = 0...

            answer += "Je n'ai pas compris ce que vous vouliez"

        print(answer)
        subscription_key = speech_key
        app = TextToSpeech(subscription_key, answer)
        app.get_token()
        app.save_audio()

    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("No speech could be recognized: {}".format(result.no_match_details))
    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))