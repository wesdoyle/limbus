from os import cpu_count

from limbus.sentiment_analyzer import SentimentAnalyzer
from limbus.tokenizers import SentenceTokenizer, Tokenizer
from multiprocessing import Pool


class NlpPipeline(object):
    """
    Provides a means for linking NLP classes together that transform text data
    """

    def __init__(self, raw_text, features):
        """
        :param: input_text: string raw text document of one or more sents
        :param: features: list<string> features to run in pipeline

        """
        self.raw_text = raw_text
        self.features = features

        self.tokenized_sents = None
        self.tokenized_words = None
        self.sent_scores = None
        self.vocab_size = 0

        self.output = None

        self.pool = Pool(cpu_count())

    # noinspection PyUnusedLocal
    def run(self):
        """
        Execute the transformation methods on attrs in the pipeline
        """
        res = self.raw_text

        for feature in self.features:
            try:
                res = getattr(self, feature)(res)

            except AttributeError as e:
                print(e)
                print(
                    "SimplePipeline supports no feature named: {}".format(
                        feature
                    )
                )

        self.output = res

        if self.tokenized_words:
            flat_list = [
                item for sublist in self.tokenized_words for item in sublist
            ]
            self.vocab_size = len(set(flat_list))

    def sent_tokenize(self, input_text):
        """
        Invokes the tokenize method on SimpleSentenceTokenizer
        :param input_text: string text to tokenize
        """
        st = SentenceTokenizer()
        sents = st.tokenize(input_text)
        self.tokenized_sents = sents
        return sents

    def word_tokenize(self, input_texts):
        """
        Invokes the tokenize method on SimpleWordTokenizer
        :param input_texts: list<string> text to tokenize
        """
        st = Tokenizer()
        if input_texts:
            all_words = self.pool.map(func=st.tokenize, iterable=input_texts)
            self.tokenized_words = all_words
            return all_words
        else:
            return input_texts

    def score_sentiment(self, input_texts):
        """
        Invokes the score method on the SimpleSentimentAnalyzer
        :param input_texts: list<string> text to sentiment score
        """
        sa = SentimentAnalyzer()

        if input_texts:
            sent_scores = self.pool.map(func=sa.score, iterable=input_texts)
            self.sent_scores = sent_scores
            return sent_scores

        else:
            return input_texts
