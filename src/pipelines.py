from src.sentiment_analyzer import SimpleSentimentAnalyzer
from src.tokenizers import SimpleSentenceTokenizer, SimpleTokenizer


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
        self.output = None

    # noinspection PyUnusedLocal
    def run(self):
        """
        Execute the transformation methods on attrs in the pipeline
        """
        res = self.raw_text
        for feature in self.features:
            try:
                print("applying: {}".format(feature))
                res = getattr(self, feature)(res)

            except AttributeError as e:
                print(e)
                print("SimplePipeline supports no feature named: {}"
                      .format(feature))

        self.output = res

    @staticmethod
    def sent_tokenize(input_text):
        """
        Invokes the tokenize method on SimpleSentenceTokenizer
        :param input_text: string text to tokenize
        """
        st = SimpleSentenceTokenizer()
        return st.tokenize(input_text)

    @staticmethod
    def word_tokenize(input_texts):
        """
        Invokes the tokenize method on SimpleWordTokenizer
        :param input_text: string text to tokenize
        """
        st = SimpleTokenizer()
        return [st.tokenize(text) for text in input_texts]

    @staticmethod
    def score_sentiment(input_texts):
        """
        Invokes the score method on the SimpleSentimentAnalyzer
        :param input_text: string text to sentiment score
        """
        sa = SimpleSentimentAnalyzer()
        return [sa.score(text) for text in input_texts]
