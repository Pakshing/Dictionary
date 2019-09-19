import json
from difflib import get_close_matches

data = json.load ( open("data.json") )

def translate(word):
    word  = word.lower()
    if word in data:
        return data[word]
    elif word.upper() in data:
        return data[word.upper()]
    elif word.title() in data:
        return data[word.title()]
    elif len( get_close_matches(word,data.keys()) ) > 0:
        yn = input( "Did you mean %s? " %get_close_matches(word,data.keys())[0] )
        yn = yn.lower()
        if yn == "y":
            return data[ get_close_matches(word,data.keys())[0] ]
        elif yn == "n":
            return "The word doesn't exist. Please double check. "
        else:
            return "I don't understand your query"

    else:
        return "Word cannot find. "


word = input("Enter word: ")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print (output)


