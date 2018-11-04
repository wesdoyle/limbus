import os
import re

class SimpleTokenizer(object):
    def __init__(self):
        self.stop_words = self._get_stopwords()

    def tokenize(self, sentence):
        lowered_sent = sentence.lower()
        clean_sentence = re.sub(r"[^a-z0-9 ]", "", lowered_sent)
        return [word for word in clean_sentence.split() if word not in self.stop_words]

    def _get_stopwords(self):
        stopwords_path = os.environ.get("STOPWORDS_LIST")
        stopwords = []
        with open(stopwords_path) as f:
            for line in f:
                stopwords.append(line.strip())
        return stopwords
