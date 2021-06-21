# import nltk
from nltk.corpus import wordnet
from PyDictionary import PyDictionary


# nltk.download('wordnet')


def get_wordnet_synonym(word):
    try:
        synonyms = wordnet.synsets(word)
        return set([name for item in synonyms for name in item.lemma_names()])
    except:
        return set()


def get_py_dictionary_synonym(word):
    try:
        dictionary = PyDictionary()
        return set(dictionary.synonym(word))
    except:
        return set()


train_words = ["sleep", "sweater", "boring"]
for element in train_words:
    wordnet_synonyms = get_wordnet_synonym(element)
    py_dictionary_synonyms = get_py_dictionary_synonym(element)
    print(element)
    print("WordNet: ", wordnet_synonyms)
    print("py-dictionary: ", py_dictionary_synonyms)
    print("Intersection: " + str(wordnet_synonyms.intersection(py_dictionary_synonyms)) + "\n")
