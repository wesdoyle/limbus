# simple-sentiment

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/32a76893bb5b407aad5c8e24816874f3)](https://app.codacy.com/app/wesdoyle/simple-sentiment?utm_source=github.com&utm_medium=referral&utm_content=wesdoyle/simple-sentiment&utm_campaign=Badge_Grade_Dashboard)
[![Build Status](https://travis-ci.org/wesdoyle/simple-sentiment.svg?branch=master)](https://travis-ci.org/wesdoyle/simple-sentiment)
[![codecov](https://codecov.io/gh/wesdoyle/simple-sentiment/branch/master/graph/badge.svg)](https://codecov.io/gh/wesdoyle/simple-sentiment)

A tool for running natural language processing pipelines in Python.

Currenly supports pattern-matching methods for:
* Sentence extraction from raw text
* Word tokenization (builtin stopword removal)
* Sentence-based sentiment polarity analysis on lists of tokens

The `pipelines` module exposes the SimplePipeline object, which can be used to pipe raw text data through assembled features.  Features are provided to a new instance of SimplePipeline along with initial raw text. The output of each feature in a pipeline is returned to the input param of the subsequent feature in the list.

To set up a basic sentiment analysis pipeline from a text file on disk:

```python
# specify the features you'd like to run
features = ['sent_tokenize', 'word_tokenize', 'score_sentiment']

with open('alice.txt', 'r') as f:
  pipeline = SimplePipeline(f, features)

# run the pipeline
pipeline.run()

# various features are now available as class attributes on `pipeline`:
pipeline.vocab_size  # 2452

# extacted data can be used for downstream ops, like EDA:
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Prepare data from pipeline
df = pd.DataFrame(list(zip(sents, scores)))
df['time_series'] = df[1].cumsum()
data = {'sents': df.index.values, 'polarity': df['time_series'].values}

# Plot
plt.figure(figsize=(16, 6), dpi=80)
sns.set_style("whitegrid")
sns.set_context("notebook", font_scale=1.24, rc={"lines.linewidth": 1.3})
graph = sns.lineplot(x="sents", y="polarity", data=data, legend='full')
graph.set(xlabel='Sentence', ylabel='Cumulative Sentiment Polarity')

```

Positive and Negative word lists adapted from:
> [https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html](https://www.cs.uic.edu/~liub/FBS/sentiment-analysis.html)

References:
> _Minqing Hu and Bing Liu. "Mining and Summarizing Customer Reviews."_
>     Proceedings of the ACM SIGKDD International Conference on Knowledge
>     Discovery and Data Mining (KDD-2004), Aug 22-25, 2004, Seattle,
>     Washington, USA
>
> _Bing Liu, Minqing Hu and Junsheng Cheng. "Opinion Observer: Analyzing_
>     and Comparing Opinions on the Web." Proceedings of the 14th
>     International World Wide Web conference (WWW-2005), May 10-14,
>     2005, Chiba, Japan.
