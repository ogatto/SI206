# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
import tweepy
from textblob import TextBlob

access_token = "796041864759676932-YLHevEOltmwRAPn0zAt0gNfLVvoOx3w"
access_token_secret = "wSrinxiOZWbX19ggIqGhH9J0eVqRGPK2Qta18LcVP00sB"
consumer_key = "JVOPaboe8oOsXFi5FYdZOn8Jn"
consumer_secret = "W8MV2AuM64uKXsRDf5i0a6JJInOLXj4tz1GIEb8qZZcXx3jGfM"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

pol_sum = 0
pol_count = 0
subj_sum = 0
subj_count = 0

public_tweets = api.search('#Puppies')
for tweet in public_tweets:
	blob = TextBlob(tweet.text)
	print(blob)
	sent = blob.sentiment
	polarity = sent.polarity
	subjectivity = sent.subjectivity
	pol_sum += polarity
	pol_count += 1
	subj_sum += subjectivity
	subj_count += 1


print("Average subjectivity is", (subj_sum/subj_count))
print("Average polarity is", (pol_sum/pol_count))
