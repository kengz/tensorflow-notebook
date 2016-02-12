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

# spacy
pip3 install -U spacy
python3 -m space.en.download

deactivate
```


## Ref

- [Pattern ref](http://www.clips.ua.ac.be/pages/pattern-en#parser)
- [Parser and POS tags ref](http://www.clips.ua.ac.be/pages/mbsp-tags)