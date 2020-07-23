import sys
import json
from SPARQLWrapper import SPARQLWrapper, JSON

endpoint_url = "https://query.wikidata.org/sparql"
file = open('allWords.json','w+')

json_languages = open('languages.json', 'r')
json_categories = open('categories.json', 'r')

languages = json.load(json_languages)
categories = json.load(json_categories)


query_base = """SELECT ?lexeme ?lemma WHERE {
  ?lexeme dct:language wd:$LANGUAGE.
  ?lexeme wikibase:lexicalCategory wd:$CATEGORY.
  ?lexeme wikibase:lemma ?lemma.
}"""


def get_results(endpoint_url, query):
    user_agent = "WDQS-example Python/%s.%s" % (sys.version_info[0], sys.version_info[1])
    # TODO adjust user agent; see https://w.wiki/CX6
    sparql = SPARQLWrapper(endpoint_url, agent=user_agent)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
##  [i]['lemma']['value']
    out = sparql.query().convert()['results']['bindings']
    out = [out[i]['lemma']['value'] for i in range(len(out))]
    return out
    
def process_query(languageID, categoryID):
    query = query_base.replace('$LANGUAGE', languageID)
    query = query.replace('$CATEGORY', categoryID)
    print(query)
    return query


results = {}
for lang in languages:
    results[lang] = {}
    for cat in categories:
        langID = languages[lang]
        catID = categories[cat]
        results[lang][cat] = get_results(endpoint_url, process_query(langID, catID))

json.dump(results, file, indent=4)
file.close()
exit()
