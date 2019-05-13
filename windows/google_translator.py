from googletrans import Translator
from langdetect import detect


def google_translate(link):
    translator = Translator()	 # Google Translate API 
    pystring = " ".join(link[1:-2])
    lang = detect(pystring)
    if link[-1] == "english":
        id = "en"
    elif link[-1] == "spanish":
        id = "es"
    elif link[-1] == "french":
        id = "fr"
    elif link[-1] == "german":
        id = "de"
    elif link[-1] == "italian":
        id = "it"
    elif link[-1] == "portugese" or link[-1] == "portuguese":
        id = "pt"
    else:
        id = "en"
    translated = translator.translate(pystring, src=lang, dest=id)	# To Translate the given language to the required language
    print(translated.text)	# Print the translated script
    try:
        speak.say("The translated text is "+translated.text)
        speak.runAndWait()
    except:
        print("Error speaking, here is the translated text: {}".format(translated.text))
