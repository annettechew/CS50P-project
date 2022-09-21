# DictHelp
#### Video Demo: https://youtu.be/Gqc9k0Gu1nE
#### Description
DictHelp is a simple dictionary programme designed to extract the definition of a word from a JSON file which contains the meanings of different words. The programme also includes a translation function which allows users to translate the definition of the word to the language of their choice.
The JSON file is obtained from https://raw.githubusercontent.com/diljeet1994/Python_Tutorials/master/Blog%20Work/Dictionary/Interactive%20Dictionary/words.json.

1) The programme will first ask the user for an input.
2) If the word is found in the JSON file, the programme will retrieve the definition of the word and return it to the user.
3) Suppose a typo was made, the programme will return the user a list of close matches to the word that the user has inputted. If the intended word is found in the list, the user will need to input "yes" and will be able to enter the position of the word to retrieve it's definition. If the intended word is not found in the list, it means that the word cannot be found in the JSON file.
4) If the word is found, the user is asked whether he/she would like the translated version of the definitionl. If "yes", the programme ask the user for language input.
5) If the language is supported by googletrans, the definition will be printed out. If the language is not supported, an error message will be printed out and continue promting the user until the user inputs a language that is supported or press control-d to exit.
6) The user is now prompted with a choice of searching again. If yes, steps 1 to 5 will be repeated. If not, the programme will end with a Thank you message.