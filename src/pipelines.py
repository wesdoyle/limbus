from tokenizers import SimpleSentenceTokenizer
from sentiment_analyzer import SimpleSentimentAnalyzer

class SimplePipeline(object):
    """
    Provides a means for linking NLP classes together that transform text data
    """
    def __init__(self, raw_text, features):
        """
        :param: input_text: string raw text document containing one or more sentences
        :param: features: list<string> features to run in pipeline

        """
        self.raw_text = raw_text
        self.features = features

    def run(self):
        """
        Execute the transformation methods on attrs in the pipeline
        """
        try:
            res = self.raw_text
            for feature in self.features:
                res = getattr(self, feature)(res)

        except AttributeError as e:
            print("SimplePipeline supports no feature named: {}"
                    .format(feature))

    def sent_tokenize(self, input_text):
        """
        Invokes the tokenize method on SimpleSentenceTokenizer
        :param input_text: string text to tokenize
        """
        st = SimpleSentenceTokenizer()
        return st.tokenize(input_text)

    def word_tokenize(self, input_text):
        """
        Invokes the tokenize method on SimpleWordTokenizer
        :param input_text: string text to tokenize
        """
        st = SimpleTokenizer()
        return st.tokenize(input_text)

    def score_sentiment(self, input_text):
        """
        Invokes the score method on the SimpleSentimentAnalyzer
        :param input_text: string text to sentiment score
        """
        sa = SimpleSentimentAnalyzer()
        return sa.score(input_text)













