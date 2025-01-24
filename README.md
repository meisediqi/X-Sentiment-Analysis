# X-Sentiment-Analysis
This Python program performs basic sentiment analysis on recent tweets related to a user-defined topic. It uses the Tweepy library to interact with the Twitter API and fetch tweets, and the TextBlob library to analyze the sentiment of the tweet text. It was created with the guidance of Siraj Raval.

# Key Features:
## Twitter API Integration:
1. Fetches recent tweets based on a keyword provided by the user.
2. Uses the Twitter API v2 for fetching tweet data, leveraging the search_recent_tweets endpoint. 

## Sentiment Analysis:
1. Each fetched tweet is analyzed using the TextBlob library to determine its sentiment (polarity and subjectivity).
2. Polarity ranges from -1.0 (negative) to 1.0 (positive).
3. Subjectivity ranges from 0.0 (objective) to 1.0 (subjective).

## Interactive:
1. Prompts the user to input a keyword for the desired topic of interest.
2. Displays the tweet text along with its sentiment analysis results.

# Requirements:
## Libraries: 
The program requires tweepy and textblob to be installed. 

## Twitter API Credentials: 
The program requires valid Twitter API credentials (API Key, Secret, Access Tokens, and Bearer Token) to authenticate with Twitter. Replace the placeholder values in the code with your credentials.

## How It Works:
1. The user inputs a keyword or topic of interest.
2. The program fetches up to 10 recent tweets matching the keyword.

## For each tweet, the program:
1. Prints the tweet text.
2. Computes and displays the sentiment analysis result.

## Example Output:
If the keyword is "Python":

- Enter the specific topic you'd like to find the sentiment of: Python
- Tweet: Python is amazing for data science!
- Sentiment: Sentiment(polarity=0.8, subjectivity=0.75)

- Tweet: I don't like Python for web development.
- Sentiment: Sentiment(polarity=-0.3, subjectivity=0.6)
