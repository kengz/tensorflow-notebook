# # import nltk
# # s = """At eight o'clock on Thursday morning. 
# # Arthur didn't feel very good."""
# # tokens = nltk.word_tokenize(s)
# # print(tokens)

# # tagged = nltk.pos_tag(tokens)
# # print(tagged)

# # print(nltk.tokenize.sent_tokenize(s))
# # print(nltk.tokenize.word_tokenize(s))

# # print(nltk.chunk.ne_chunk(tagged))

# # def bag_of_words(words):
# # 	return dict([(word, True) for word in words])

# # feats = bag_of_words(nltk.word_tokenize('great movie'))
# # nltk.download('classifier')
# # import nltk.data
# # classifier = nltk.data.load('classifier/movie_reviews_NaiveBayes.pickle')
# # classifier.classify(feats)


# from textblob import TextBlob

# text = '''
# The titular threat of The Blob has always struck me as the ultimate movie
# monster: an insatiably hungry, amoeba-like mass able to penetrate
# virtually any safeguard, capable of--as a doomed doctor chillingly
# describes it--"assimilating flesh on contact.
# Snide comparisons to gelatin be damned, it's a concept with the most
# devastating of potential consequences, not unlike the grey goo scenario
# proposed by technological theorists fearful of
# artificial intelligence run rampant.
# '''

# blob = TextBlob(text)
# print(blob.tags)
# print(blob.noun_phrases)
# print(blob.words)
# print(blob.sentences)

# # for sentence in blob.sentences:
# #   print(sentence)
# #   print(sentence.sentiment.polarity)


# # print(blob.translate(to="zh-CN"))



# # Lemmatization
# from textblob import Word

# w = Word("sees")
# print(w.lemmatize("v"))
# w = Word("saw")
# print(w.lemmatize("v"))
# w = Word("seen")
# print(w.lemmatize("v"))
# w = Word("seeing")
# print(w.lemmatize("v"))


# # WordNet
# from textblob import Word
# from textblob.wordnet import VERB
# word = Word("see")
# # set of "synonyms"
# print(word.synsets)
# print(word.get_synsets(pos=VERB))

# print(word.definitions)

# # Autocorrect, based on Norvig. 70% right
# b = TextBlob("I havv goood speling!")
# print(b.correct())


# # Google translate
# chinese_blob = TextBlob(u"美丽优于丑陋")
# print(chinese_blob.translate(to="en"))
# print(chinese_blob.detect_language())

# b = TextBlob("And now for something completely different.")
# print(b.parse())


# # Python string
# zen = TextBlob("Beautiful is better than ugly")
# print(zen[0:19])
# print(zen.upper())
# print(zen.find("is"))

# # n-grams
# print(zen.ngrams(n=3))



# # classifier
# from textblob.classifiers import NaiveBayesClassifier

# # train naive bayes classifier
# # with open('train.csv', 'r') as fp:
# # 	print(fp)
# # 	cl = NaiveBayesClassifier(fp, format='csv')

# import csv
# fp = open('train.csv', 'r')
# print(fp)
# cl = NaiveBayesClassifier(fp, format='csv')
# print(cl.classify("This is an amazing library!"))

# prob_dist = cl.prob_classify("This is an amazing library!")
# print(prob_dist.max())
# print(round(prob_dist.prob("pos"), 2))

# # use trained cl in textblob
# from textblob import TextBlob
# b = TextBlob("The beer is good. But the hangover is horrible.", classifier=cl)
# print(b.classify())

# # evaluate
# test = open('test.csv', 'r')
# print(cl.accuracy(test))
# cl.show_informative_features(5)

# # Update classifier
# new_data = [('She is my best friend.', 'pos'),
# ("I'm happy to have a new friend.", 'pos'),
# ("Stay thirsty, my friend.", 'pos'),
# ("He ain't from around here.", 'neg')]

# cl.update(new_data)
# test = open('test.csv', 'r')
# print(cl.accuracy(test))



# Advanced usage: slight cuztomizations

from textblob import TextBlob
# from textblob.sentiments import NaiveBayesAnalyzer

# blob = TextBlob("I love this library", analyzer=NaiveBayesAnalyzer())
# print(blob.sentiment)


# from textblob import TextBlob

# # tokenizer
# from nltk.tokenize import TabTokenizer
# tokenizer = TabTokenizer()
# blob = TextBlob("This is\ta rather tabby\tblob.", tokenizer=tokenizer)
# print(blob.tokens)

# blob2 = TextBlob("That is\talso a tabby\tblob.")
# print(blob2.tokenize(tokenizer))


# # noun_phrases extractor
# from textblob.np_extractors import ConllExtractor
# extractor = ConllExtractor()
# blob = TextBlob("Python is a high-level programming language.", np_extractor=extractor)
# print(blob.noun_phrases)


# # POS tagger
# from textblob.taggers import NLTKTagger
# nltk_tagger = NLTKTagger()
# blob = TextBlob("Tag! You're It!", pos_tagger=nltk_tagger)
# print(blob.pos_tags)


# # Parsers
# from textblob.parsers import PatternParser
# blob = TextBlob("Parsing is fun.", parser=PatternParser())
# print(blob.parse())


# # DRY usage
# from textblob import Blobber
# from textblob.taggers import NLTKTagger
# # custom TextBlob constructor
# tb = Blobber(pos_tagger=NLTKTagger(), np_extractor=extractor)
# blob1 = tb("Python is a high-level programming language.")
# blob2 = tb("Nodejs is a high-level programming language.")
# print(blob1.noun_phrases)
# print(blob1.pos_tags)




# Stanford NLP with hacks from https://gist.github.com/alvations/e1df0ba227e542955a8a

import nltk
nltk.__version__
from nltk.tag import StanfordNERTagger
st = StanfordNERTagger('english.all.3class.distsim.crf.ser.gz')
print(st._stanford_jar)
stanford_dir = st._stanford_jar.rpartition('/')[0]
from nltk.internals import find_jars_within_path
stanford_jars = find_jars_within_path(stanford_dir)
print(":".join(stanford_jars))
st._stanford_jar = ':'.join(stanford_jars)
print(st._stanford_jar)
res = st.tag('Rami Eid is studying at Stony Brook University in NY'.split())
print(res)



from nltk.internals import find_jars_within_path
from nltk.tag import StanfordPOSTagger
st = StanfordPOSTagger('english-bidirectional-distsim.tagger')
print(st._stanford_jar)
stanford_dir = st._stanford_jar.rpartition('/')[0]
stanford_jars = find_jars_within_path(stanford_dir)
st._stanford_jar = ':'.join(stanford_jars)
st.tag('What is the airspeed of an unladen swallow ?'.split())


from nltk.internals import find_jars_within_path
from nltk.parse.stanford import StanfordParser
parser=StanfordParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
parser._classpath
stanford_dir = parser._classpath[0].rpartition('/')[0]
stanford_dir
parser._classpath = tuple(find_jars_within_path(stanford_dir))
parser._classpath
list(parser.raw_parse("the quick brown fox jumps over the lazy dog"))

from nltk.internals import find_jars_within_path
from nltk.parse.stanford import StanfordDependencyParser
dep_parser=StanfordDependencyParser(model_path="edu/stanford/nlp/models/lexparser/englishPCFG.ser.gz")
stanford_dir = dep_parser._classpath[0].rpartition('/')[0]
dep_parser._classpath = tuple(find_jars_within_path(stanford_dir))

print(next(dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")))

print([parse.tree() for parse in dep_parser.raw_parse("The quick brown fox jumps over the lazy dog.")])
