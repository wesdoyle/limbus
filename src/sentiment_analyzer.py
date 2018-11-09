import os

class SimpleSentimentAnalyzer(object):
    """
    Responsible for scoring the sentiment polarity a list of tokens
    """
    def __init__(self):
        self.pos_words = self._get_words("POS_WORD_LIST")
        self.neg_words = self._get_words("NEG_WORD_LIST")
        self.negation_words = self._get_words("NEGATION_WORD_LIST")

    def score(self, tokens):
        """
        Returns a sentiment score for a provided list of string tokens
        # TODO: account for tokens that invert the sentment polarity
        # not, never, etc...
        """
        score = 0
        negation_polarity = 1
        if tokens:
            for token in tokens:
                if token in self.negation_words:
                    negation_polarity *= -1
                if token in self.pos_words:
                    score += 1
                elif token in self.neg_words:
                    score -= 1
            score = score / len(tokens)
        return score * negation_polarity

    def _get_words(self, path):
        words = []
        with open(os.environ.get(path)) as f:
            for line in f:
                words.append(line.strip())
        return words
