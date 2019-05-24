import re

from .words.stopwords import stopwords
from .words.abbreviation_words import abbreviation_words


class SimpleTokenizer(object):
    """
    Tokenizes words given a string
    """

    def __init__(self):
        pass

    @staticmethod
    def tokenize(sentence):
        """
        Tokenizes a sentence string
        :param sentence: string sentence to tokenize
        :return: List<string> tokens
        """
        lowered_sent = sentence.lower()
        clean_sentence = re.sub(r"[^a-z0-9 ]", "", lowered_sent)
        return [word for word in clean_sentence.split() if word not in stopwords]


class SimpleSentenceTokenizer(object):
    """
    Tokenizes sentences given string
    """

    def __init__(self):
        pass

    def tokenize(self, sents):
        """
        Tokenizes a string of sentences
        :return: List<string> sentences
        """
        splitter = r"(?i)" \
                   + self._build_neg_lookbehind_predicate() \
                   + r"[^\w \n\(\)\`\'\,\;\{\}\[\]\&\^\%\$\#\@\*\/\\\-\’\‘]"

        if sents:
            # prep = [re.sub("\n", " ", sent) for sent in sents]
            return [re.sub("\n", " ", sent.strip()) for sent in re.split(splitter, sents) if sent.strip()]

        else:
            return None

    @staticmethod
    def _build_neg_lookbehind_predicate():
        """
        Builds a string of negative lookbehinds for the list of
        abbreviated words on this sentence tokenizer
        """
        neg_lookbehind_predicate = r""

        for abbrev in abbreviation_words:
            neg_lookbehind_predicate += r"(?<!{})".format(abbrev)

        return neg_lookbehind_predicate

