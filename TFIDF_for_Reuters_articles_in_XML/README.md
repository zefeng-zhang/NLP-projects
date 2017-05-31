TFIDF for Reuters Articles in XML
=================================

Description
------------

This project reads 9194 Reuters articles in the XML format and finds the commen words in the target file using TFIDF:
* extract titles and paragraphs from the XML files using ElementTree
* tokenize and stem all strings with NLTK
* find the most common words using TfidfVectorizer


How to use
----------

Run the following command in your
```
python tfidf.py your_folder_path/reuters-vol1-disk1-subset  your_folder_path/reuters-vol1-disk1-subset/33312newsML.xml

```
