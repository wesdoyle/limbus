import pytest

from limbus.sentiment_analyzer import SentimentAnalyzer


class TestSentimentAnalyzer:
    def test_should_return_plus_1_when_tokens_are_all_positive(self):
        # given three "positive sentiment" tokens, the score should be positive
        tokens = ["good", "happy", "wonderful"]
        sa = SentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 1

    def test_should_return_minus_1_when_tokens_are_all_negative(self):
        # given three "negative sentiment" tokens, the score should be negative
        tokens = ["bad", "unfortunate", "horrible"]
        sa = SentimentAnalyzer()
        score = sa.score(tokens)
        assert score == -1

    def test_should_return_zero_score_for_all_neutral_words(self):
        tokens = ["house", "table", "cat"]
        sa = SentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 0

    def test_returns_zero_if_token_len_is_zero(self):
        tokens = []
        sa = SentimentAnalyzer()
        score = sa.score(tokens)
        assert score == 0

    @pytest.mark.parametrize(
        "tokens, expected",
        [
            (["not", "good", "happy", "wonderful"], True),
            (["not", "not", "good", "happy", "wonderful"], False),
            (["not", "not", "not", "good"], True),
            (["nor", "not", "not", "good"], True),
            (["nor", "not", "good"], False),
        ],
    )
    def test_inverts_sentiment_if_tokens_contain_negation_word(
        self, tokens, expected
    ):
        sa = SentimentAnalyzer()
        score = sa.score(tokens)
        if expected is True:
            assert score < 0
        elif expected is False:
            assert score > 0
        else:
            assert score == 0

    @pytest.mark.parametrize(
        "tokens, expected", [(["nor"], 0), (["nor", "foo"], 0), ]
    )
    def test_if_sentiment_is_neutral_and_contains_neg_tok_score_is_neutral(
        self, tokens, expected
    ):
        sa = SentimentAnalyzer()
        score = sa.score(tokens)
        assert score == expected

    @pytest.mark.parametrize(
        "tokens, expected",
        [
            (["good", "excellent", "awesome", "foo"], 0.75),
            (["bad", "terrible", "annoying", "foo"], -0.75),
            (["not", "bad", "terrible", "annoying", "foo"], 0.6),
        ],
    )
    def test_score_is_fractional_for_tokens_with_non_unity_net_sentiment(
        self, tokens, expected
    ):
        sa = SentimentAnalyzer()
        score = sa.score(tokens)
        assert score == expected
