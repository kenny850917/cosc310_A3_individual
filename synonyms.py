# First, you're going to need to import wordnet:
import nltk
from nltk.corpus import wordnet
# Let's compare the noun of "ship" and "boat:"
synonyms = []
antonyms = []

for syn in wordnet.synsets("car"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))


w1 = wordnet.synset('car.n.01') # v here denotes the tag verb
w2 = wordnet.synset('truck.n.01')
print(w1.wup_similarity(w2))
