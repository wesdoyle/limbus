from tokenizers import SimpleTokenizer
from sentiment_analyzer import SimpleSentimentAnalyzer

tokenizer = SimpleTokenizer()
sentiment = SimpleSentimentAnalyzer()

with open('./resources/sample_data/christmas', 'r') as f:
    text = f.read()
    tokens = tokenizer.tokenize(text)
    score = sentiment.score(tokens)
    print("Score was: {}".format(score))
