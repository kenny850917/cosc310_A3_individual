# -*- coding: utf-8 -*-
'''
'''
from nltk import sent_tokenize, word_tokenize, pos_tag, ne_chunk
# import nltk
# nltk.download('punkt')
# nltk.download('averaged_perceptron_tagger')
# nltk.download('maxent_ne_chunker')
# nltk.download('words')


class NER:

	def extract_entities(text):
		entities = []
		for sentence in sent_tokenize(text):
			chunks = ne_chunk(pos_tag(word_tokenize(sentence)))
		entities.extend([chunk for chunk in chunks if hasattr(chunk, 'label')])
		return entities


if __name__ == '__main__':
	text = """
Hi, my name is Kenny I would like a car
"""

print(NER.extract_entities(text))
