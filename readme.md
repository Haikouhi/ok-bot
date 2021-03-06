# Creating a vocal command bot 

## Speech-to-text : 

Speech-to-text enables real-time transcription of audio streams into text. 
By default, the speech-to-text service uses the Universal language [model](https://en.wikipedia.org/wiki/Unified_Modeling_Language). This model was trained using Microsoft-owned data and is deployed the cloud. 

For further info click [here :](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-to-text)

**Prerequisites :** 
- Azure subscription key 
- Python 3 and up
- Python Speech SDK Package 

**Steps :** 
- create a main.py and import SDK 
- create an instance of a speech config with specified subscription key and service region
- create a recognizer with the given settings
- the code starts speech recognition, and returns after a single utterance is recognized. 
- the end of a single utterance is determined by listening for silence at the end or until a maximum of 15 seconds of audio is processed

*Note: Since recognize_once() returns only a single utterance, it is suitable only for single shot recognition like command or query. For long-running multi-utterance recognition, use start_continuous_recognition() instead.* : 
result = speech_recognizer.recognize_once()


## Text-to-speech

Text-to-speech enables devices to convert text into natural human-like synthesized speech. 

There are three types of voices :

- Standard voices

     - created using Statistical Parametric Synthesis and/or Concatenation Synthesis techniques. 
     - highly intelligible and sound quite natural
     - speak in more than 45 languages, with a wide range of voice options
     - voices provide high pronunciation accuracy, including support for abbreviations...

- Neural voices

    - uses deep neural networks to overcome the limits of traditional text-to-speech systems in matching the patterns of stress and intonation in spoken language, and in synthesizing the units of speech into a computer voice
    - neural capability does prosody prediction and voice synthesis simultaneously
    - more fluid and natural-sounding voice
    - can be used to make interactions with chatbots and virtual assistants more natural and engaging, convert digital texts such as e-books into audiobooks and enhance in-car navigation systems. With the human-like natural prosody and clear articulation of words
    - neural voices significantly reduce listening fatigue when you interact with AI systems
    - to learn more about neural voices, see [here](https://azure.microsoft.com/blog/microsoft-s-new-neural-text-to-speech-service-helps-machines-speak-like-people/)

- Custom voices

    - creates a recognizable, one-of-a-kind voice for your brand
    - make a studio recording and upload the associated scripts as the training data
    - service then creates a unique voice model tuned to your recording


The request body is structured as Speech Synthesis Markup Language (SSML), which allows us to choose the voice and language of the [response](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/speech-synthesis-markup).


For further info click [here :](https://docs.microsoft.com/en-us/azure/cognitive-services/speech-service/quickstart-python-text-to-speech)

**Steps :**
- pip install requests
- create main.py and import modules (requests and ElementTree), there are used to write the speech response to a file with a timestamp, construct the HTTP request, and call the text-to-speech API
- start by adding some code that makes sure this sample will work with Python 2.7.x and 3.x
-  create a class where we'll put our methods for token exchange, and calling the text-to-speech API
- get an access token
- make a request and save the response
    - first, we need to set the base_url and path
    - we need to add required headers for the request
    - construct the request body using Speech Synthesis Markup Language (SSML)
    - finally, we'll make a request to the service. If the request is successful, and a 200 status code is returned, the speech response is written to a timestamped file
- instantiate the class and call the functions
- from the command line (or terminal session), navigate to the project directory and run the main.py file


### Using OpenWeatherAPI - a Python program to find current weather details of any city using openweathermap api 

- import required modules 
- enter API key  
- base_url variable to store url 
- give city name 
- complete_url variable to store 
- complete url address 
- get method of requests module 
- return response object 
- json method of response object 
- convert json format data into 
- python format data 
- now x contains list of nested dictionaries 
- check the value of "cod" key is equal to 
- "404", means city is found otherwise, 
- city is not found 

For further details, click [here](https://www.geeksforgeeks.org/python-find-current-weather-of-any-city-using-openweathermap-api/)



## Continuous Integration with Travis CI :

- Go to Travis-ci.com and Sign up with GitHub 
- Accept the Authorization of Travis CI and you’ll be redirected to GitHub.
- Click the green Activate button, and select the repositories you want to use with Travis CI
- Add a .travis.yml file to your repository to tell Travis CI what to do
- Add the .travis.yml file to git, commit and push, to trigger a Travis CI build
- Check the build status page to see if your build passes or fails, according to the return status of the build command by visiting the Travis CI and selecting your repository



## Creating shell scripts :
- create a folder to hold all .sh files
### The virtual environment :
- in the folder add file by writing the command *emacs script_name.sh* (you can use any Text Editor) 
- once inside the file write *#!bin/bash*
- add the necessary components
- save file
- go to the shell script vault (folder we fist created)
- type *ls -l script_name.sh* to see and change rights to the file 
- type *chmod +x script_name.sh*
- to test script, execute it by typing *./script_name.sh*
- *bash -x script_name.sh* 
- in order for the script to execute properly we need to move it in a particular file *sudo mv script_name.sh /usr/local/bin*
- to test, type in *script_name.sh*
### The Dependencies :
- install pip
- install git 
- git clone
- create virtual env.
- activate virtual env.
- install requirements 


## Présentation :
- contexte
- demonstration
- limitations (POC)
- perspectives