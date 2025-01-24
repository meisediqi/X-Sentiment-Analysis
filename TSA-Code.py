import tweepy
from textblob import TextBlob

# Insert your credentials here 
APIKey = ''
APISecret = ''
accessToken = ''
accessTokenSecret = ''
bearerToken = ''

# Authenticate with Twitter using the v2 API client
client = tweepy.Client(bearer_token=bearerToken)

# Keyword input
keyword = input("Enter the specific topic you'd like to find the sentiment of: ")

# Fetch tweets using v2 search_recent_tweets endpoint
response = client.search_recent_tweets(query=keyword, max_results=10, tweet_fields=['text'])

# Check if the response contains tweets
if response.data:
    for tweet in response.data:
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
else:
    print("No tweets found for the specified keyword.")
