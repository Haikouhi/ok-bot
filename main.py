# coding: utf8

import azure.cognitiveservices.speech as speechsdk

from QueryClass import *
from constantes import *
from chatbot import *

# librairie qui permet de couper les phrases avec des tokens

write_speech_key()
speech_key = get_speech_key()

nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')

speech_config = speechsdk.SpeechConfig(subscription=speech_key, region=service_region, speech_recognition_language="fr-FR")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config)

continuer = True

while continuer:

    speak_answer(speech_key, "Dit quelquechose...")
    print("Dit quelquechose...")

    result = speech_recognizer.recognize_once()

    if result.reason == speechsdk.ResultReason.RecognizedSpeech:

        query = Query()

        firstname_list = query.firstname_list()

        """list_query = []  # initialisation de la liste des requêtes que l'on va effectuer
        firstname = ""  # init vide pour les demandes de prenoms non connu par la db
        answer = ""  # init le message que le bot va envoyer"""


        list_query, firstname = get_list_query_and_firstname(result, firstname_list, word_dict)

        list_query = query_ca_va(list_query)

        list_query = set(list_query)

        answer = make_queries(query, list_query, firstname)
        speak_answer(speech_key, answer)

        continuer = stop(list_query)

        list_query = reinitialize_query(list(list_query))


    elif result.reason == speechsdk.ResultReason.NoMatch:
        print("Je n'ai pas entendu")

    elif result.reason == speechsdk.ResultReason.Canceled:
        cancellation_details = result.cancellation_details
        print("Speech Recognition canceled: {}".format(cancellation_details.reason))
        if cancellation_details.reason == speechsdk.CancellationReason.Error:
            print("Error details: {}".format(cancellation_details.error_details))


os.remove("azure_key.txt")

