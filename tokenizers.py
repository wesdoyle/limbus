import re

class SimpleTokenizer(object):
    def __init__(self):
        self.stop_words = self._get_stopwords()

    def tokenize(self, sentence):
        lowered_sent = sentence.lower()
        clean_sentence = re.sub(r"[^a-z0-9 ]", "", lowered_sent)
        return clean_sentence.split()

    def _get_stopwords(self):
        pass
