from tokenizers import SimpleSentenceTokenizer

class SimplePipeline(object):
    """
    Provides a means for linking NLP classes together that transform text data
    """
    def __init__(self, raw_text, features):
        """
        :param: raw_text: string raw text document containing one or more sentences
        :param: features: list<string> features to run in pipeline

        """
        self.raw_text = raw_text
        self.features = features

    def run(self):
        try:
            for feature in self.features:
                getattr(self, feature)(self.raw_text)

        except AttributeError as e:
            print("SimplePipeline supports no feature named: {}"
                    .format(feature))

    def sent_tokenize(self, raw_text):
        st = SimpleSentenceTokenizer()
        st.tokenize(raw_text)
