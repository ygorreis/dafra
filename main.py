import re
import unicodedata
from nltk.corpus import stopwords

class ApplicationFramework:
	
	#GLOBAL VAR AREA	
	global language_stopwords, regex
	
	language_stopwords = set(stopwords.words('english'))	
	regex = [
		r'<[^>]+>',
		r'(?:@[\w_]+)',
		r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",
		r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',	 
		r'(?:(?:\d+,?)+(?:\.?\d+)?)',
		r"(?:[a-z][a-z'\-_]+[a-z])",
		r'(?:[\w_]+)',
		r'(?:\S)'
	]
	#END GLOBAL VAR AREA
	
	#METHODS
	def tokenizer(self, tweet):
		tokens_re = re.compile(r'('+'|'.join(regex)+')', re.VERBOSE | re.IGNORECASE)
		tokens = tokens_re.findall(tweet)
		return tokens
		
	def remove_stopwords(self, stopword, list_tokens):		
		for item in list_tokens:
			for token in item:
				if token in stopword or token in language_stopwords:
					item.remove(token)
	
		return list_tokens
			
	def to_lowercase(self, texts):
		return texts.lower()
				
				
	def remove_special_chars(char):
		# https://gist.github.com/boniattirodrigo/67429ada53b7337d2e79
		# Unicode normalize transforma um caracter em seu equivalente em latin.
		
		nfkd = unicodedata.normalize('NFKD', char)
		new_char = u"".join([c for c in nfkd if not unicodedata.combining(c)])

		# Usa expressão regular para retornar a palavra apenas com números, letras e espaço
		return re.sub('[^a-zA-Z0-9 \\\]', '', new_char)
		
		
class MyApp:
	
	#initialize framework
	appFra = ApplicationFramework()
	
	#define list to receive tweet tokenized
	tweet_tokenized = []
	
	#tweet and stopword example
	tweet = ['RT @marcobonzanini: just an example! :D http://example.com #NLP']
	test_stopword = [':','!', 'rt']

	#to lowercase tweet
	#change to pass and receive list
	tweet[0] = appFra.to_lowercase(tweet[0])
	
	#tokenize tweet
	tweet_tokenized.append(appFra.tokenizer(tweet[0]))
	
	#remove stopwords
	tweet = appFra.remove_stopwords(test_stopword, tweet_tokenized)
	
	print tweet
		
MyApp()