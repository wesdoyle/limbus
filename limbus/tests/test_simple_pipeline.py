import pytest

# noinspection PyUnusedLocal
from limbus.pipelines import NlpPipeline

# TODO Rewrite tests to isolate deps rather than internal function calls


# noinspection PyUnresolvedReferences,PyUnusedLocal
class TestNlpPipeline:
    @pytest.mark.parametrize(
        "input", [
            (["foo"]),
            (["foo", "sent_tokenize"]),
            (["foo", "bar"]),
        ]
    )
    def test_should_invoke_sentence_tokenizer(self, input):
        input_text = "foo! bar baz, and. quux?"
        features = ["foo"]
        sut = NlpPipeline(input_text, features)

        with pytest.raises(AttributeError):
            sut.run()
            sut.sent_tokenize.assert_called_once_with(input_text)

    def test_should_have_none_output_when_new(self):
        input_text = "foo! bar baz, and. quux?"
        features = ["sent_tokenize"]
        sut = NlpPipeline(input_text, features)
        assert sut.output is None

    def test_should_store_final_result_on_self_after_run(self):
        input_text = "foo! bar baz, and. quux?"
        features = ["sent_tokenize"]
        sut = NlpPipeline(input_text, features)
        sut.run()
        assert sut.output is not None

    def test_if_word_tokenize_receives_none_input_is_forwarded(self):
        features = ["word_tokenize"]
        sut = NlpPipeline(None, features)
        sut.run()
        assert sut.output is None

    def test_if_score_sentiment_receives_none_input_is_forwarded(self):
        features = ["score_sentiment"]
        sut = NlpPipeline(None, features)
        sut.run()
        assert sut.output is None

    def test_if_sent_tokenize_receives_none_input_is_forwarded(self):
        features = ["sent_tokenize"]
        sut = NlpPipeline(None, features)
        sut.run()
        assert sut.output is None

    @pytest.mark.parametrize(
        "input_text, expected",
        [
            ("Foo! foo? foO!!", 1),
            ("bar, bar, bar??? bar and bar or bar?", 1),
            ("Really nice bicycle. Excellent horrible feature", 6),
            ("", 0),
            ("and", 0),
            ("and or. but for be.", 0),
        ],
    )
    def test_pipeline_calculates_vocab_size(self, input_text, expected):
        features = ["sent_tokenize", "word_tokenize", "score_sentiment"]
        sut = NlpPipeline(input_text, features)
        sut.run()
        assert sut.vocab_size == expected
