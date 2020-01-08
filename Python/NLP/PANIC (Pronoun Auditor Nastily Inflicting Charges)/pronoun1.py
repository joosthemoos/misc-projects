import nltk
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import state_union
import speech_recognition as sr

train_text = state_union.raw("2005-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)


# recognizing the speech from the mic, used to translate the stuff into string
def recognize_speech_from_mic(recognizer, microphone):
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("'recognizer' must be a 'Recognizer' instance")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("'microphone' must be a 'Microphone' instance")

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    response = {
        "success": True,
        "failure": None,
        "transcription": None,
    }

    try:
        response["transcription"] = recognizer.recognize_google(audio)
    except sr.RequestError:
        # unreachable API, unresponsive
        response["success"] = False
        response["failure"] = "API unavailable"
    except sr.UnknownValueError:
        # unintelligible speech
        response["error"] = "Unable to recognize speech. Try again"

    return response


def process_content(to_process):
    processed = []
    try:
        words = nltk.word_tokenize(to_process)
        tagged = nltk.pos_tag(words)
        print(tagged)
        for word in tagged:
            strinn, word_type = word
            print(word)
            if word_type in ('NNP', 'JJ'):
                print('it got to here')
                processed.append(strinn)
        return processed
    except Exception as e:
        print(str(e))


if __name__ == "__main__":
    enby_names = []
    name_in_question = None
    stop = True
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    while stop:
        print('Test your pronoun skills!')
        message = recognize_speech_from_mic(recognizer, microphone)
        phrase_to_parse = message["transcription"]
        print(phrase_to_parse)
        word_list = phrase_to_parse.split()
        # this stops listening and correcting once someone says "stop this"
        if word_list[0] == 'stop' and word_list[1] == 'this':
            break
        # add something in here about adding nonbinary names to list
        phrase_parsed = custom_sent_tokenizer.tokenize(phrase_to_parse)
        parsed_again = process_content(phrase_to_parse)
        # print(parsed_again)
        counter = 0
        for word in parsed_again:
            # print('get to here')
            # put some shit here! use corpora to det. type of thing
            in_something = False
            if word in enby_names:
                name_in_question = 'nb_plur'
                in_something = True
            if in_something is False:
                # print("hello")
                with open('male.txt') as f:
                    if word in f.read():
                        print("male")
                        name_in_question = 'mal'
                        in_something = True
                with open('female.txt') as g:
                    if word in g.read():
                        print("female")
                        name_in_question = 'fem'
                        in_something = True
            if counter == 1 and in_something is True:
                name_in_question = 'nb_plur'
            counter += 1
            # stuff is questionable! TYPE STUFF HERE DAMNIT

        print("next sentence: ")
        message2 = recognize_speech_from_mic(recognizer, microphone)
        pronoun_container = message2["transcription"]
        word_list_pn = pronoun_container.split()
        print(pronoun_container)
        comp_type = None
        for word in word_list_pn:
            if word == "she" or word == "her" or word == "hers":
                comp_type = 'fem'
                break
            elif word == "he" or word == "him" or word == "his":
                comp_type = 'mal'
                break
            elif word == "they" or word == "them" or word == "theirs":
                comp_type = 'nb_plur'
                break
            print(word, comp_type)
        print(name_in_question)
        if comp_type == name_in_question:
            print("You heckin did it u nerd")
        else:
            print("Ya dun hecked up! The pronoun should be different!")  # fix
