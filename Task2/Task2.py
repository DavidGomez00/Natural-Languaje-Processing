import nltk
from nltk.corpus import brown


if __name__ == "__main__":

	for c in brown.categories():
		count = 0
		words = brown.words(categories = c)
		print(c)
		for word in words:
			if word == "fawn": count += 1
			if count > 2: break
		print(count)
