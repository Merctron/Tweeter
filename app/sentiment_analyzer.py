# We use VaderSentiment, a bag-of-words + rules based sentiment analysis engine
# for our simple classifier:
# https://github.com/cjhutto/vaderSentiment#about-the-scoring
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

def getSentiment(phrase):
	# Use VaderSentiment to generate sentiment scores. Convert the sentiment
	# dictionary into a list so it is easy to report the sentiment with the
	# maximum score.
	analysis = analyzer.polarity_scores(phrase)
	scores   = []
	for key in analysis:
		scores.append(analysis[key])

	# The shape of the analysis dict is:
	# { neg:<score>, neu:<score>, pos:<score>, comp:<score> }
	#
	# We get rid of the compound score and use a simple maximum
	# likelihood strategy
	scores = scores[:len(scores) - 1]

	# Get the index associate with the maximum score and key into the result
	# dictionary.
	idx         = scores.index(max(scores))
	result_dict = {
		0: "Negative",
		1: "Neutral",
		2: "Positive"
	}

	return result_dict[idx]

# We run a simple sentiment analyzer as a standalone script if invoked as main
if __name__ == "__main__":
	phrase = input("Enter a phrase for sentiment analysis:\n")
	print("The sentiment for the phrase '{}' is:\n{}".format(
														phrase,
														getSentiment(phrase)))
