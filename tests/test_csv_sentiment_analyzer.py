class TestCsvSentimentAnalyzer:
    """
    CsvSentimentAnalyzer unit tests
    """
    def test_scores_net_positive_csv_as_positive(self):
        filepath = './fixture_files/pos_test.csv'
        csv_sa = CsvSentimentAnalyzer(filepath)
        score = csv_sa.score()
        assert score > 0
