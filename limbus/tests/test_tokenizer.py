import pytest

from limbus.tokenizers import Tokenizer


class TestTokenizer:
    """
    Tokenizer unit tests
    """

    @pytest.mark.parametrize(
        "input, expected",
        [
            ("foo bar baz", ["foo", "bar", "baz"]),
            ("", []),
            ("foobarbaz", ["foobarbaz"]),
            (" ", []),
        ],
    )
    def test_tokenizer_splits_string_sent_on_whitespace(
        self, input, expected
    ):
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(input)
        assert expected == tokens

    def test_tokenizer_splits_string_sent_on_whitespace_case_insensitive(
        self,
    ):
        input_sent = "foO BAr bAZ"
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(input_sent)
        expected = ["foo", "bar", "baz"]
        assert expected == tokens

    def test_tokenizer_removes_non_alphanumeric_chars(self):
        input_sent = "foO!! BAr>? bAZ#$@"
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(input_sent)
        expected = ["foo", "bar", "baz"]
        assert expected == tokens

    def test_tokenizer_removes_stopwords(self):
        input_sent = "a foo is the are bar and baz"
        tokenizer = Tokenizer()
        tokens = tokenizer.tokenize(input_sent)
        expected = ["foo", "bar", "baz"]
        assert expected == tokens
