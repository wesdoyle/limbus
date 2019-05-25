import pytest


# noinspection PyShadowingBuiltins
from bluebook.tokenizers import SentenceTokenizer


class TestSentenceTokenizer(object):
    @pytest.mark.parametrize("input, expected",
                             [
                                 ("baz! bang. foo.", ["baz", "bang", "foo"]),
                                 ("baz? bang! foo.", ["baz", "bang", "foo"]),
                                 ("baz. bang. foo.", ["baz", "bang", "foo"]),
                                 ("Foo bar baz. Quux bang foo", ["Foo bar baz", "Quux bang foo"]),
                                 ("Foo.", ["Foo"]),
                                 (".", []),
                                 ("", []),
                             ])
    def test_splits_sentence_strings_on_sentence_punctuation(self, input, expected):
        sent_tokenizer = SentenceTokenizer()
        result = sent_tokenizer.tokenize(input)
        assert expected == result

    @pytest.mark.parametrize("input, expected",
                             [
                                 ("Mr. Smith went home? Yes! WAT.",
                                  ["Mr. Smith went home", "Yes", "WAT"]),

                                 ("Foo bar? I didn't know that.",
                                  ["Foo bar", "I didn't know that"]),

                                 ("Mrs. Smith went home with Mr. Smith.",
                                  ["Mrs. Smith went home with Mr. Smith"]),

                                 ("Good. Really Good. What?",
                                  ["Good", "Really Good", "What"]),

                                 ('"What\'s wrong?" "Nothing at all."',
                                  ['What\'s wrong', 'Nothing at all']),

                                 ("The U.S. is the United. The U.K., the U.S.A. is...",
                                  ["The US is the United", "The UK, the USA is"]),

                                 ("!?....", []),
                                 ("Whoa!!!", ["Whoa"]),
                                 ("Whoa!!! What???", ["Whoa", "What"]),
                             ])
    def test_splits_sentence_strings_on_sentence_punctuation(self, input, expected):
        sent_tokenizer = SentenceTokenizer()
        result = sent_tokenizer.tokenize(input)
        assert expected == result
