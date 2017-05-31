import sys
import re
from sklearn.feature_extraction.stop_words import ENGLISH_STOP_WORDS
import xml.etree.cElementTree as ET
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
from collections import Counter
import nltk
# nltk.download('punkt')

def gettext(xmltext):
    """
    Parse xmltext and return the text from <title> and <text> tags
    """
    root = ET.fromstring(xmltext)
    title = root.find("title").text
    body = []
    for child in root.find("text").iterfind('p'):
        body += [child.text]
    body = " ".join(body)
    return title + " " + body


def tokenize(text):
    """
    Tokenize text and return a non-unique list of tokenized words
    found in the text. Normalize to lowercase, strip punctuation,
    remove stop words, drop words of length < 3.
    """
    text = text.lower()
    non_alphabet = re.compile('[^A-Za-z ]+')
    new = re.sub(non_alphabet, ' ', text)
    words = word_tokenize(new)
    words = [word for word in words if len(word) >= 3]
    words = [word for word in words if word not in ENGLISH_STOP_WORDS]
    return words


def stemwords(words):
    """
    Given a list of tokens/words, return a new list with each word
    stemmed using a PorterStemmer.
    """
    stemmer = PorterStemmer()
    words = [stemmer.stem(word) for word in words]
    return words


if __name__=="__main__":
    f = open(sys.argv[1], "r")
    xmltext = f.read() # input string for gettext
    f.close()
    text = gettext(xmltext)
    tokens = stemwords(tokenize(text))
    counts = Counter(tokens).most_common(10)
    for count in counts:
        print count[0], count[1]


# Running commands:
# python common.py reuters-vol1-disk1-subset/131705newsML.xml