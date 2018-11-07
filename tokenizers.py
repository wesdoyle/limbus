import os
import re

class SimpleTokenizer(object):
    """
    Tokenizes words given a string
    """
    def __init__(self):
        self.stop_words = self._get_stopwords()

    def tokenize(self, sentence):
        """
        Tokenizes a sentence string
        :param sentence: string sentence to tokenize
        :return: List<string> tokens
        """
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

class SimpleSentenceTokenizer(object):
    """
    Tokenizes sentences given string
    """
    def __init__(self):
        # TODO: Expand list of abbrevs
        # https://en.wikipedia.org/wiki/Lists_of_abbreviations
        self.abbrevs = self._get_abbreviation_words()

    def tokenize(self, sents):
        """
        Tokenizes a string of sentences
        :param sentence: string sentences to tokenize
        :return: List<string> sentences
        """
        return [sent.strip() for sent in re.split(r"[.!?]", sents) if sent]

    def _get_abbreviation_words(self):
        words_path = os.environ.get("ABBREV_WORD_LIST")
        words = []
        with open(words_path) as f:
            for line in f:
                words.append(line.strip())
        return words




