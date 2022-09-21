import json
from difflib import get_close_matches
import time
import googletrans
from googletrans import Translator

with open("wordsdict.json") as file:
    words = json.load(file)

def main():
    print("Hello, there! Welcome to DictHelp!")
    time.sleep(0.5)
    search = input("Which word definition are you looking for? ")
    response = checkword(search)
    if type(response) != list:
        print(f"{search} cannot be found")
    else:
        while True:
            try:
                trans = input("Do you want the definition to be translated? Enter yes/no: ")
                if trans == "yes":
                    while True:
                        try:
                            lang = input("Which language do you want the definition to be in? ")
                            reply = translate(response, lang)
                            if reply == False:
                                print(f"Sorry, {lang} is currently not supported")
                                # if language is not found, promt the user again
                            else:
                                print("Definition:")
                                print(reply)
                                break
                        except EOFError:
                            print()
                            break
                        except:
                            print(f"Sorry, {lang} is currently not supported")
                            # if language is not found, promt the user again
                    break
                elif trans == "no":
                    print("Definition:")
                    print(response[0])
                    break
                # else, if trans is not yes or no, promt the user again
            except EOFError:
                print()
                break
    while True:
        try:
            again = input("Would you like to continue? Enter yes/no: ")
            value = searchagain(again)
            if value == False:
                print("Thank you for using DictHelp")
                break
            elif value == True:
                main()
                break
        except EOFError:
            print()
            break


def checkword(word):
    word = word.lower().strip()
    if word in words:
        return words[word]
    elif word.upper() in words:
        return words[word.upper()]
    elif word.title() in words:
        return words[word.title()]
    else:
        closematch = get_close_matches(word, words.keys())
        if closematch:
            possiwords = list(map(str, closematch))
            while True:
                try:
                    select = input("Do you mean %s ? Enter yes/no: " %possiwords)
                    if select == "yes":
                        choose = int(input("Enter the position of the word: "))
                        return words[closematch[choose-1]]
                    elif select == "no":
                        return None
                    # if select is not yes/no, promt user again
                except:
                    return None
        else:
            return None


def searchagain(again):
    if again == "yes":
        return True
    elif again == "no":
        return False
    else:
        return None

def translate(response, lang):
        if lang in googletrans.LANGUAGES or googletrans.LANGCODES:
            translator = Translator()
            translate = translator.translate(response[0], dest=lang)
            text = translate.text
            return text
        else:
            return False


if __name__ == "__main__":
    main()
