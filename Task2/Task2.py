import nltk
from nltk.corpus import names


if __name__ == "__main__":
	female_names = names.words('female.txt')
	male_names = names.words('male.txt')

	cfd = nltk.ConditionalFreqDist((name, males)
								for name in males
								for )