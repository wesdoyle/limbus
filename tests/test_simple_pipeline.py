from mock import patch

class TestSimplePipeline:

    @patch('pipelines.SimplePipeline.__new__')
    def test_simple_pipeline_should_invoke_provided_features_for_text(self, mock_pipeline):
        raw_text = "foo! bar baz, and. quux?"
        features = ['bang']
        sut = SimplePipeline(raw_text, features)
        nlp_pipeline.run()
        sut.bang.assert_called_once_with(raw_text)



