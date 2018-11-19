"""
Example script for running sentiment analysis on a string text sample
"""

from tokenizers import SimpleTokenizer
from sentiment_analyzer import SimpleSentimentAnalyzer

tokenizer = SimpleTokenizer()
sentiment = SimpleSentimentAnalyzer()

with open('./resources/sample_data/heart', 'r') as f:
    text = f.read()
    tokens = tokenizer.tokenize(text)
    score = sentiment.score(tokens)
    print("Score was: {}".format(score))
