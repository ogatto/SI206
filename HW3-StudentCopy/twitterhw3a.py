# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

# Unique code from Twitter
access_token = "796041864759676932-YLHevEOltmwRAPn0zAt0gNfLVvoOx3w"
access_token_secret = "wSrinxiOZWbX19ggIqGhH9J0eVqRGPK2Qta18LcVP00sB"
consumer_key = "JVOPaboe8oOsXFi5FYdZOn8Jn"
consumer_secret = "W8MV2AuM64uKXsRDf5i0a6JJInOLXj4tz1GIEb8qZZcXx3jGfM"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
img = "hello.jpg"
hashtag_txt = "#UMSI-206 #Proj3"
api.update_with_media(img, status=hashtag_txt)