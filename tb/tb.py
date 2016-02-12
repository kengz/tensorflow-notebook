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

for sentence in blob.sentences:
  print(sentence)
  print(sentence.sentiment.polarity)


print(blob.translate(to="zh-CN"))