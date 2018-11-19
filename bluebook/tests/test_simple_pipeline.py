from mock import patch
import pytest

# noinspection PyUnusedLocal
from src.pipelines import SimplePipeline


# noinspection PyUnresolvedReferences,PyUnusedLocal
class TestSimplePipeline:

    @patch('src.pipelines.SimplePipeline.sent_tokenize')
    def test_should_invoke_sentence_tokenizer(self, mock_st):
        input_text = "foo! bar baz, and. quux?"
        features = ['sent_tokenize']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.sent_tokenize.assert_called_once_with(input_text)

    @patch('src.pipelines.SimplePipeline.word_tokenize')
    def test_should_invoke_word_tokenizer(self, mock_wt):
        input_text = "foo! bar baz, and. quux?"
        features = ['word_tokenize']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.word_tokenize.assert_called_once_with(input_text)

    @patch('src.pipelines.SimplePipeline.score_sentiment')
    def test_should_invoke_score_sentiment(self, mock_ss):
        input_text = "Good stuff"
        features = ['score_sentiment']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.score_sentiment.assert_called_once_with(input_text)

    @patch('src.pipelines.SimplePipeline.word_tokenize')
    @patch('src.pipelines.SimplePipeline.sent_tokenize')
    def test_should_invoke_two_features_in_order(self, mock_st, mock_wt):
        mock_st.return_value = "foo"
        input_text = "foo! bar baz, and. quux?"
        features = ['sent_tokenize', 'word_tokenize']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.sent_tokenize.assert_called_once_with(input_text)
        sut.word_tokenize.assert_called_once_with("foo")

    @patch('src.pipelines.SimplePipeline.score_sentiment')
    @patch('src.pipelines.SimplePipeline.word_tokenize')
    @patch('src.pipelines.SimplePipeline.sent_tokenize')
    def test_should_invoke_three_features_in_order(self, mock_st, mock_wt, mock_ss):
        mock_st.return_value = "foo"
        mock_wt.return_value = 1234
        input_text = "foo! bar baz, and. quux?"
        features = ['sent_tokenize', 'word_tokenize', 'score_sentiment']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.sent_tokenize.assert_called_once_with(input_text)
        sut.word_tokenize.assert_called_once_with("foo")
        sut.score_sentiment.assert_called_once_with(1234)

    @pytest.mark.parametrize("input",
                             [
                                 (['foo']),
                                 (['foo', 'sent_tokenize']),
                                 (['foo', 'bar']),
                             ]
                             )
    def test_should_invoke_sentence_tokenizer(self, input):
        input_text = "foo! bar baz, and. quux?"
        features = ['foo']
        sut = SimplePipeline(input_text, features)

        with pytest.raises(AttributeError):
            sut.run()
            sut.sent_tokenize.assert_called_once_with(input_text)


    def test_should_have_none_output_when_new(self):
        input_text = "foo! bar baz, and. quux?"
        features = ['sent_tokenize']
        sut = SimplePipeline(input_text, features)
        assert sut.output is None

    def test_should_store_final_result_on_self_after_run(self):
        input_text = "foo! bar baz, and. quux?"
        features = ['sent_tokenize']
        sut = SimplePipeline(input_text, features)
        sut.run()
        assert sut.output is not None

    def test_if_word_tokenize_receives_none_input_is_forwarded(self):
        features = ['word_tokenize']
        sut = SimplePipeline(None, features)
        sut.run()
        assert sut.output is None

    def test_if_score_sentiment_receives_none_input_is_forwarded(self):
        features = ['score_sentiment']
        sut = SimplePipeline(None, features)
        sut.run()
        assert sut.output is None

    def test_if_sent_tokenize_receives_none_input_is_forwarded(self):
        features = ['sent_tokenize']
        sut = SimplePipeline(None, features)
        sut.run()
        assert sut.output is None

    @pytest.mark.parametrize("input_text, expected",
            [
                ("Foo! foo? foO!!", 1),
                ("bar, bar, bar??? bar and bar or bar?", 1),
                ("Really nice bicycle. Excellent horrible feature", 6),
                ("", 0),
                ("and", 0),
                ("and or. but for be.", 0),
            ])
    def test_pipeline_calculates_vocab_size(self, input_text, expected):
        features = ['sent_tokenize', 'word_tokenize', 'score_sentiment']
        sut = SimplePipeline(input_text, features)
        sut.run()
        assert sut.vocab_size == expected


