from sentiment_analyzer import SimpleSentimentAnalyzer

class TestSentimentAnalyzer:
    def test_sentiment_analyzer_should_return_positive_score_for_all_pos_words(self):
        tokens = ['good', 'happy', 'wonderful']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 3

    def test_sentiment_analyzer_should_return_negative_score_for_all_neg_words(self):
        tokens = ['bad', 'unfortunate', 'horrible']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == -3

    def test_sentiment_analyzer_should_return_zero_score_for_all_neutral_words(self):
        tokens = ['house', 'table', 'cat']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 0
