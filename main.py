import azure.cognitiveservices.speech as speechsdk
from Query import *
from text_to_speech import *
from random import randint
import nltk # librairie qui permet de couper les phrases avec des tokens

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

        word_list = ["gueule", "bonjour", "hey", "hi", "yo", "salut", "age", "mail", "prenom", "ville", "adresse",
                     "l'adresse", "habite", "naissance", "numero", "telephone", "nom", "astrologique", "signe",
                     "bye", "au revoir", "exit", "va", "ça", "ca", "vas", "comment", "anniversaire", "l'anniversaire",
                     "horoscope", "l'horoscope"]
        firstname_list = query.firstname_list()

        possible_response = ["Bien sur que non", "Je ne pense pas ", "No!",
                             "Arrete de poser des questions", "Qu'est-ce que j'en sais moi ?",
                             "Je suis ton père", "Arrete de dire des conneries stp", "Tu sors ou je te sors?",
                             "C'est qui la patronne?", "Nope", "Demandes à PL", "Demandes à Sumenia", "Plaît-il",
                             "pffffff", ":confused:", ":snake:", ":eye:", ":octopus:"
                             ]

        list_query = []  # initialisation de la liste des requêtes que l'on va effectuer
        firstname = ""  # init vide pour les demandes de prenoms non connu par la db
        answer = ""  # init le message que le bot va envoyer

        tokens = nltk.word_tokenize(result.text)  # permet de recupérer la réponse en tokens (mot par mot)

        for elt in tokens:  # parcourir tous les tokens
            if elt.capitalize() in firstname_list:  # si l'un des tokens est un prenom dans la liste des prenoms....
                firstname = elt.capitalize()  # le prenom devient cet élèment
            if elt.lower() in word_list:  # si un des tokens dans la liste des mots...
                list_query.append(elt.lower())  # on l'ajoute dans la liste des requêtes à effectuer

        for elt in list_query:  # on parcourt ttes les requ effectuées (les if...)
            if elt == "nom":
                answer += query.name(firstname) + '\n'
            elif elt == "naissance":
                answer += query.date(firstname) + '\n'
            elif elt == "anniversaire" or elt == "l'anniversaire":
                answer += query.anniversaire(firstname) + '\n'
            elif elt == "horoscope" or elt == "l'horoscope":
                answer += query.horoscope(firstname) + '\n'
            elif elt == "ville" or elt == "habite" or elt == "adresse" or elt == "l'adresse":
                answer += query.city(firstname) + '\n'
            elif elt == "numero" or elt == "telephone":
                answer += query.number(firstname) + '\n'
            elif elt == "age":
                answer += query.age(firstname) + '\n'
            elif elt == "mail":
                answer += query.mail(firstname) + '\n'
            elif elt == "astrologique" or elt == "signe":
                answer += "Son signe est " + query.zodiac_sign(firstname) + '\n'
            elif elt == "bye" or elt == "au revoir" or elt == "exit":
                answer += "See you soon loser!"
            elif elt == "bonjour" or elt == "hey" or elt == "yo" or elt == "salut" or elt == "hi":
                answer += "Bonjour ! Je suis Chit-Chat (: "
            elif elt == "gueule":
                if firstname != "":
                    if firstname == "Theo" or firstname == "Timothée":
                        answer += "Non, j'ai trop de respect pour lui, c'est l'un de mes créateurs"
                    elif firstname == "Caroline" or firstname == "Haikouhi":
                        answer += "Non, j'ai trop de respect pour elle, c'est l'une de mes créatrices"
                    else:
                        answer += "Ta gueule {}".format(firstname)
            elif elt == "va" or elt == "vas":
                if "ca" in list_query or "ça" in list_query or "comment" in list_query:
                    answer += "Je pète la forme"

        if len(list_query) == 0:  # si liste des Query = 0...

            index_response_picked = randint(0, len(
                possible_response) - 1)  # on tire au sort un index entre 0 et nombre-1...
            response = possible_response[index_response_picked]  # réponse choisie...
            answer += response  # et ajoutée !

        print(answer)
        subscription_key = "mettre subscription key"
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