# Using text2 from the nltk book corpa, create your own version of the
# MadLib program.  

# Requirements:
# 1) Only use the first 150 tokens
# 2) Pick 5 parts of speech to prompt for, including nouns
# 3) Replace nouns 15% of the time, everything else 10%

# Deliverables:
# 1) Print the orginal text (150 tokens)
# 1) Print the new text
print("START*******")

import random
import nltk
from nltk.book import *
from nltk import word_tokenize,sent_tokenize


debug = False

if debug:
	print ("Getting information from text2...\n")

original_text = (text2[:151])
paragraph = " ".join(original_text)
print("Original Text:")
print (paragraph)

tokens = nltk.word_tokenize(paragraph)
# print("TOKENS")
# print(tokens[:151])
tagged_tokens = nltk.pos_tag(tokens) # gives us a tagged list of tuples
# print("TAGGED TOKENS")
# print(tagged_tokens[:151])

# if debug:
# 	print ("First few tagged tokens are:")
# 	for tup in tagged_tokens[:151]:
# 		print (tup)

tagmap = {"NN":"a noun","NNS":"a plural noun","VB":"a verb","JJ":"an adjective", "PRP":"a preposition"}
substitution_probabilities = {"NN":.15,"NNS":.10,"VB":.10,"JJ":.10, "PRP":.10}

def spaced(word):
 	if word in [",", ".", "?", "!", ":"]:
 		return word
 	else:
 		return " " + word

final_words = []

for (word, tag) in tagged_tokens:
 	if tag not in substitution_probabilities or random.random() > substitution_probabilities[tag]:
 		final_words.append(spaced(word))
 	else:
 		new_word = input("Please enter %s:\n" % (tagmap[tag]))
 		final_words.append(spaced(new_word))
		

final_text = "".join(final_words)				
print("New Text:")
print (final_text)

print("\n\nEND*******")
