import gpt_api
import twitter_api

tweet = gpt_api.make_tweet()
twitter_api.post(tweet)
