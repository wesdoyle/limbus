from tokenizers import SimpleSentenceTokenizer
import pytest

class TestSimpleSentenceTokenizer(object):
    @pytest.mark.parametrize("input, expected",
            [
                ("baz! bang. foo.", ["baz", "bang", "foo"]),
                ("baz? bang! foo.", ["baz", "bang", "foo"]),
                ("baz. bang. foo.", ["baz", "bang", "foo"]),
                ("Foo bar baz. Quux bang foo", ["Foo bar baz", "Quux bang foo"]),
                ("Foo.", ["Foo"]),
                (".", []),
                ("", []),
            ]
        )
    def test_splits_sentence_strings_on_sentence_punctuation(self, input, expected):
        sent_tokenizer = SimpleSentenceTokenizer()
        result = sent_tokenizer.tokenize(input)
        assert expected == result

    @pytest.mark.parametrize("input, expected",
            [
                ("Mr. Smith went home? Yes! WAT.", ["Mr. Smith went home", "Yes", "WAT"]),
                ("Mrs. Smith went home with Mr. Smith.", ["Mrs. Smith went home with Mr. Smith"]),
                ("Good, eg. Really Good. What?", ["Good, eg. Really Good", "What"]),
                ("!?....", []),
                ("Whoa!!!", ["Whoa"]),
                ("Whoa!!! What???", ["Whoa", "What"]),
            ]
        )
    def test_splits_sentence_strings_on_sentence_punctuation(self, input, expected):
        sent_tokenizer = SimpleSentenceTokenizer()
        result = sent_tokenizer.tokenize(input)
        assert expected == result

