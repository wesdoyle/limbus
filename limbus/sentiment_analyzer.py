from .words.negation_words import negation_words
from .words.negative_words import negative_words
from .words.positive_words import positive_words


class SentimentAnalyzer(object):
    """
    Responsible for scoring the sentiment polarity a list of tokens
    """

    def __init__(self):
        pass

    @staticmethod
    def score(tokens):
        """
        Returns a sentiment score for a provided list of string tokens
        """
        score = 0
        negation_polarity = 1
        if tokens:
            for token in tokens:
                if token in negation_words:
                    negation_polarity *= -1
                if token in positive_words:
                    score += 1
                elif token in negative_words:
                    score -= 1
            score = score / len(tokens)
        return score * negation_polarity
