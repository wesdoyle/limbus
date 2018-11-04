from sentiment_analyzer import SimpleSentimentAnalyzer

class TestSentimentAnalyzer:
    def test_sentiment_analyzer_should_return_plus_1_when_tokens_are_all_positive(self):
        # given three "positive sentiment" tokens, the score should be positive
        tokens = ['good', 'happy', 'wonderful']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 1

    def test_sentiment_analyzer_should_return_minus_1_when_tokens_are_all_negative(self):
        # given three "negative sentiment" tokens, the score should be negative
        tokens = ['bad', 'unfortunate', 'horrible']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == -1

    def test_sentiment_analyzer_should_return_zero_score_for_all_neutral_words(self):
        tokens = ['house', 'table', 'cat']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 0

    def test_sentiment_analyzer_returns_zero_if_token_len_is_zero(self):
        tokens = []
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 0

    def test_sentiment_analyzer_inverts_sentiment_if_tokens_contain_negation_word(self):
        tokens = ['not', 'good', 'happy', 'wonderful']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score < 0















