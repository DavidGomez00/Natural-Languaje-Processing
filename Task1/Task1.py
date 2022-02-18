import pipenv
import nltk
import numpy as np
import io
import sys
from nltk.book import *
from difflib import SequenceMatcher


def similar(a, b):
	''' Similarity function.
	'''
	return SequenceMatcher(None, a, b).ratio()


if __name__ == "__main__":
	# nltk texts
	texts = [text1, text2, text3, text4, 
			 text5, text6, text7, text8, text9]

	# Ask for an input
	print('Type a word:')
	user_word = input()

	# Print the selected word
	print(f"You've typed the word {user_word}")

	# Define stdout types
	old_stdout = sys.stdout
	new_stdout = io.StringIO()


	# Search for similar words in each text
	for i, text in enumerate(texts):
		# Change standard output to strings
		sys.stdout = new_stdout

		# Obtain similar words
		text.similar(user_word)
		similar_words = {}
		similar_words = new_stdout.getvalue()

		# Change standard output to prints
		sys.stdout = old_stdout

		# Transform into an array
		similar_words = similar_words.replace('No matches', '').replace('\n', ' ').split()

		# Search for the most similar word
		max_similarity = 0
		for word in similar_words:
			s = similar(user_word, word)
			if(s > max_similarity):
				max_similarity = s
	
		# Add all words with the most similarity ratio
		final_words = []
		for word in similar_words:
			s = similar(user_word, word)
			if (s == max_similarity):
				final_words.append(word)

		# Change standard output to prints
		sys.stdout = old_stdout

		# Print the results for this text
		print("Text" + str(i + 1) + ": " + str(final_words))

