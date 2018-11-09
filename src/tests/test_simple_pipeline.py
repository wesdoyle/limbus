from mock import patch
import pytest


# noinspection PyUnusedLocal
from src.pipelines import SimplePipeline


class TestSimplePipeline:

    @patch('pipelines.SimplePipeline.sent_tokenize')
    def test_simple_pipeline_should_invoke_sentence_tokenizer(self, mock_st):
        input_text = "foo! bar baz, and. quux?"
        features = ['sent_tokenize']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.sent_tokenize.assert_called_once_with(input_text)

    @patch('pipelines.SimplePipeline.word_tokenize')
    def test_simple_pipeline_should_invoke_word_tokenizer(self, mock_wt):
        input_text = "foo! bar baz, and. quux?"
        features = ['word_tokenize']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.word_tokenize.assert_called_once_with(input_text)

    @patch('pipelines.SimplePipeline.score_sentiment')
    def test_simple_pipeline_should_invoke_score_sentiment(self, mock_ss):
        input_text = "Good stuff"
        features = ['score_sentiment']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.score_sentiment.assert_called_once_with(input_text)

    @patch('pipelines.SimplePipeline.word_tokenize')
    @patch('pipelines.SimplePipeline.sent_tokenize')
    def test_simple_pipeline_should_invoke_two_features_in_order(self, mock_st, mock_wt):
        mock_st.return_value = "foo"
        input_text = "foo! bar baz, and. quux?"
        features = ['sent_tokenize', 'word_tokenize']
        sut = SimplePipeline(input_text, features)
        sut.run()
        sut.sent_tokenize.assert_called_once_with(input_text)
        sut.word_tokenize.assert_called_once_with("foo")

    @patch('pipelines.SimplePipeline.score_sentiment')
    @patch('pipelines.SimplePipeline.word_tokenize')
    @patch('pipelines.SimplePipeline.sent_tokenize')
    def test_simple_pipeline_should_invoke_three_features_in_order(self, mock_st, mock_wt, mock_ss):
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
    def test_simple_pipeline_should_invoke_sentence_tokenizer(self, input):
        input_text = "foo! bar baz, and. quux?"
        features = ['foo']
        sut = SimplePipeline(input_text, features)

        with pytest.raises(AttributeError):
            sut.run()
            sut.sent_tokenize.assert_called_once_with(input_text)
