# TextBlob notebook

## Setup

Use `virtualenv` please.

```shell
virtualenv env
source env/bin/activate

# nltk
sudo pip3 install -U nltk
# manually download and unzip data
git clone -b gh-pages https://github.com/nltk/nltk_data.git ~/nltk_data_root
cp -r ~/nltk_data_root/packages ~/nltk_data
find . -name "*.zip" | while read filename; do unzip -o -d "`dirname "$filename"`" "$filename"; done;

# textblob
pip3 install -U textblob
python3 -m textblob.download_corpora

# spacy, not worthy yet except for perf and entity
pip3 install -U spacy
python3 -m space.en.download

deactivate
```

Stanford NER, POSTagger, Parser. These files are freaking huge: ~600Mb in total.

```shell
curl -o ~/nltk_data/stanford-ner.zip -Lk http://nlp.stanford.edu/software/stanford-ner-2015-12-09.zip
curl -o ~/nltk_data/stanford-postagger-full.zip -Lk http://nlp.stanford.edu/software/stanford-postagger-full-2015-12-09.zip
curl -o ~/nltk_data/stanford-parser-full.zip -Lk http://nlp.stanford.edu/software/stanford-parser-full-2015-12-09.zip

unzip ~/nltk_data/stanford-ner.zip -d ~/nltk_data/stanford-ner && cd ~/nltk_data/stanford-ner/* && mv ./* ../ && rm ~/nltk_data/stanford-ner.zip && cd

unzip ~/nltk_data/stanford-postagger-full.zip -d ~/nltk_data/stanford-postagger-full && cd ~/nltk_data/stanford-postagger-full/* && mv ./* ../ && rm ~/nltk_data/stanford-postagger-full.zip && cd

unzip ~/nltk_data/stanford-parser-full.zip -d ~/nltk_data/stanford-parser-full && cd ~/nltk_data/stanford-parser-full/* && mv ./* ../ && rm ~/nltk_data/stanford-parser-full.zip && cd

echo '
# Stanford NLP
export CLASSPATH=~/nltk_data/stanford-ner/stanford-ner.jar:~/nltk_data/stanford-postagger-full/stanford-postagger.jar:~/nltk_data/stanford-parser-full/stanford-parser.jar:~/nltk_data/stanford-parser-full/stanford-parser-3.6.0-models.jar
export STANFORD_MODELS=~/nltk_data/stanford-ner/classifiers:~/nltk_data/stanford-postagger-full/models:' >> ~/.bash_profile
source ~/.bash_profile

```


## Ref

- [Pattern ref](http://www.clips.ua.ac.be/pages/pattern-en#parser)
- [Parser and POS tags ref](http://www.clips.ua.ac.be/pages/mbsp-tags)