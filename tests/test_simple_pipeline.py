from mock import patch
import pytest

from pipelines import SimplePipeline

class TestSimplePipeline:

    @patch('pipelines.SimplePipeline.sent_tokenize')
    def test_simple_pipeline_should_invoke_sentence_tokenizer(self, mock_st):
        raw_text = "foo! bar baz, and. quux?"
        features = ['sent_tokenize']
        sut = SimplePipeline(raw_text, features)
        sut.run()
        sut.sent_tokenize.assert_called_once_with(raw_text)

    @pytest.mark.parametrize("input",
            [
                (['foo']), (['foo', 'sent_tokenize'], ['foo', 'bar'])
            ]
        )
    def test_simple_pipeline_should_invoke_sentence_tokenizer(self, input):
        raw_text = "foo! bar baz, and. quux?"
        features = ['foo']
        sut = SimplePipeline(raw_text, features)

        with pytest.raises(AttributeError):
            sut.run()
            sut.sent_tokenize.assert_called_once_with(raw_text)

