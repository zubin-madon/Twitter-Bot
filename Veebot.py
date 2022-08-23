# Importing Modules/Libraries
import tweepy
import time
from datetime import datetime


def pull_next_quote():
    with open("trivia.txt", "r") as file:
        quotes = file.read().splitlines()
    quote = quotes.pop(0)
    quotes.append(quote)

    with open("trivia.txt", "w") as file:
        quotes = file.write("\n".join(quotes))
        print(quotes)

    return quote


# Credentials (Insert your keys and tokens below)
api_key = "********"
api_secret = "********"
bearer_token = r"********"
access_token = "********"
access_token_secret = "********"
client_id = "********"
client_secret = "********"
twitter_id = 1872****
app_id = 15550869********
# Connecting to Twitter API
client = tweepy.Client(bearer_token, api_key, api_secret, access_token, access_token_secret)

auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Bot's unique ID
bot_id = int(client.get_me().data.id)
print(bot_id)
exclusion = 'Vee'
# This is so the bot only looks for the most recent tweets.
start_id = 1
initialisation_resp = client.get_users_mentions(twitter_id)
if initialisation_resp.data != None:
    start_id = initialisation_resp.data[0].id

# Looking for mentions tweets in an endless loop
while True:
    response = client.get_users_mentions(twitter_id, since_id=start_id)
    print(response)

    # # Reply Code
    if response.data is not None:

        for tweet in response.data:
            if exclusion not in tweet.text:

                try:
                    message = pull_next_quote()
                    print(tweet.text)
                    client.create_tweet(in_reply_to_tweet_id=tweet.id, text=message)
                    start_id = tweet.id
                    print(start_id)
                    break
                except Exception as error:
                    print(error)

    # Delay (so the bot doesn't search for new tweets a bunch of time each second)
    time.sleep(10)
