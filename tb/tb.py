# import nltk
# s = """At eight o'clock on Thursday morning. 
# Arthur didn't feel very good."""
# tokens = nltk.word_tokenize(s)
# print(tokens)

# tagged = nltk.pos_tag(tokens)
# print(tagged)

# print(nltk.tokenize.sent_tokenize(s))
# print(nltk.tokenize.word_tokenize(s))

# print(nltk.chunk.ne_chunk(tagged))

# def bag_of_words(words):
# 	return dict([(word, True) for word in words])

# feats = bag_of_words(nltk.word_tokenize('great movie'))
# nltk.download('classifier')
# import nltk.data
# classifier = nltk.data.load('classifier/movie_reviews_NaiveBayes.pickle')
# classifier.classify(feats)


from textblob import TextBlob

text = '''
The titular threat of The Blob has always struck me as the ultimate movie
monster: an insatiably hungry, amoeba-like mass able to penetrate
virtually any safeguard, capable of--as a doomed doctor chillingly
describes it--"assimilating flesh on contact.
Snide comparisons to gelatin be damned, it's a concept with the most
devastating of potential consequences, not unlike the grey goo scenario
proposed by technological theorists fearful of
artificial intelligence run rampant.
'''

blob = TextBlob(text)
print(blob.tags)
print(blob.noun_phrases)
print(blob.words)
print(blob.sentences)

# for sentence in blob.sentences:
#   print(sentence)
#   print(sentence.sentiment.polarity)


# print(blob.translate(to="zh-CN"))



# Lemmatization
from textblob import Word

w = Word("sees")
print(w.lemmatize("v"))
w = Word("saw")
print(w.lemmatize("v"))
w = Word("seen")
print(w.lemmatize("v"))
w = Word("seeing")
print(w.lemmatize("v"))


# WordNet
from textblob import Word
from textblob.wordnet import VERB
word = Word("see")
# set of "synonyms"
print(word.synsets)
print(word.get_synsets(pos=VERB))

print(word.definitions)

# Autocorrect, based on Norvig. 70% right
b = TextBlob("I havv goood speling!")
print(b.correct())


# Google translate
chinese_blob = TextBlob(u"美丽优于丑陋")
print(chinese_blob.translate(to="en"))
print(chinese_blob.detect_language())

b = TextBlob("And now for something completely different.")
print(b.parse())


# Python string
zen = TextBlob("Beautiful is better than ugly")
print(zen[0:19])
print(zen.upper())
print(zen.find("is"))

# n-grams
print(zen.ngrams(n=3))