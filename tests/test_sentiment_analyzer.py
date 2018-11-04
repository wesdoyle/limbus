from sentiment_analyzer import SimpleSentimentAnalyzer
import pytest

class TestSentimentAnalyzer:
    def test_should_return_plus_1_when_tokens_are_all_positive(self):
        # given three "positive sentiment" tokens, the score should be positive
        tokens = ['good', 'happy', 'wonderful']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 1

    def test_should_return_minus_1_when_tokens_are_all_negative(self):
        # given three "negative sentiment" tokens, the score should be negative
        tokens = ['bad', 'unfortunate', 'horrible']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == -1

    def test_should_return_zero_score_for_all_neutral_words(self):
        tokens = ['house', 'table', 'cat']
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 0

    def test_returns_zero_if_token_len_is_zero(self):
        tokens = []
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 0

    @pytest.mark.parametrize("tokens, expected",
            [
                (['not', 'good', 'happy', 'wonderful'], True),
                (['not', 'not', 'good', 'happy', 'wonderful'], False),
                (['not', 'not', 'not', 'good'], True),
            ])
    def test_inverts_sentiment_if_tokens_contain_negation_word(self, tokens, expected):
        sa = SimpleSentimentAnalyzer()
        score = sa.score(tokens)
        if expected:
            assert score < 0
        else:
            assert score > 0
