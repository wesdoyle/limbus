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

    @staticmethod
    def _get_stopwords():
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
        :return: List<string> sentences
        """
        splitter = r"(?i)" + self._build_neg_lookbehind_predicate() + r"[^\w\ `\'\,\;\{\}\[\]\&\^\%\$\#\@\*\/\\]"

        if sents:
            return [sent.strip() for sent in re.split(splitter, sents) if sent.strip()]

        else:
            return None

    def _build_neg_lookbehind_predicate(self):
        """
        Builds a string of negative lookbehinds for the list of
        abbreviated words on this sentence tokenizer
        """
        neg_lookbehind_predicate = r""

        for abbrev in self.abbrevs:
            neg_lookbehind_predicate += r"(?<!{})".format(abbrev)

        return neg_lookbehind_predicate

    @staticmethod
    def _get_abbreviation_words():
        """
        Returns file containing abbreviated words as a Python list of those words
        """
        words_path = os.environ.get("ABBREV_WORD_LIST")
        words = []
        with open(words_path) as f:
            for line in f:
                words.append(line.strip())
        return words
