import re
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
			
	def to_lowercase(self, list_texts):
		for item in list_texts:
			item.lower()
		
		return list_texts
				
class MyApp:
	
	#initialize framework
	appFra = ApplicationFramework()
	
	#define list to receive tweet tokenized
	tweet_tokenized = []
	
	#tweet and stopword example
	tweet = ['RT @marcobonzanini: just an example! :D http://example.com #NLP']
	test_stopword = [':','!', 'RT']

	#to lowercase tweet
	tweet = appFra.to_lowercase(tweet)
	print "post lowercase"
	print tweet
	
	#tokenize tweet
	tweet_tokenized.append(appFra.tokenizer(tweet[0]))
	
	print(appFra.remove_stopwords(test_stopword, tweet_tokenized))
		
MyApp()