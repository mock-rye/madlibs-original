import json
import random as rand
json_words = open('allWords.json', 'r')
json_languages = open('languages.json', 'r')
json_types = open('types.json', 'r')

words = json.load(json_words)
languages = json.load(json_languages)
types = json.load(json_types)

def out_format(strA, strB):
    return '{:>} {:<}'.format((strA + ': '), strB)

def print_dict(dict):
    for key in dict:
        print(out_format(key, dict[key]))
        
def print_keys(dict):
    for key in dict:
        print(str(key))

def getRandom(typ):
    return str(words[typ][rand.randint(0,len(words[typ]))])

def madlibs(phrase):
    for t in types:
        for i in range(phrase.count(t)): ## yes this has to be done, otherwise it just replaces all occurrences with the same word
            phrase = phrase.replace(t, ' ' + getRandom(types[t]) + ' ',1)
    return phrase.strip().replace('  ',' ') ## just doing some cleanup just in case :shrug:

def get_language():
    print('choose a language:')
    print_keys(languages)
    language = input('language:')
    return words[language]



words = get_language()
print('word types:')
print_dict(types)
while(True):
    print(madlibs(input()))
