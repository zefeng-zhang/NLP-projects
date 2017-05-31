from common import *
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
import os


def tokenizer(text):
    tokens = tokenize(text)
    stems = stemwords(tokens)
    return stems # list of tokens (words)


def filelist(root):
    """
    Return a fully-qualified list of filenames under root directory
    """
    file_list = []
    for path, directories, filenames in os.walk(root):
        for filename in filenames:
            file_list.append(os.path.join(path, filename))
    return file_list


f = open(sys.argv[2], "r") # target file
xmltext = f.read()
f.close()
text = gettext(xmltext)
tokens = stemwords(tokenize(text))
data = Counter(tokens) # input keys as vocabulary

tfidf = TfidfVectorizer(input='filename', # argument to transform() is list of files
                        encoding='utf-8',
                        decode_error='ignore',
                        analyzer='word',
                        preprocessor=gettext, # convert xml to text
                        tokenizer=tokenizer,  # tokenize, stem
                        stop_words='english',
                        vocabulary=data.keys())

file_list = filelist(sys.argv[1]) # corpus
results = tfidf.fit_transform(file_list)

# find index of the target file in corpus
index = [i for i in range(len(file_list)) if file_list[i] == sys.argv[2]]
TFIDE = results[index,:]

non_zero = np.nonzero(TFIDE)[1]
myresult = [(data.keys()[i], TFIDE[0, i]) for i in non_zero]
myresult.sort(key=lambda x: x[1], reverse=True)
for i in range( len(myresult) ):
    if(myresult[i][1] > 0.09):
        print myresult[i][0], '%.3f' % myresult[i][1]


# Running commands:
# python tfidf.py ~/data/reuters-vol1-disk1-subset  ~/data/reuters-vol1-disk1-subset/33312newsML.xml
# ./testrig.sh ~/data/testing-reuters-vol1-disk1-subset ~/data/results-testing-reuters-vol1-disk1-subset