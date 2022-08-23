import tweepy
from keepalive import keep_alive
import time
from datetime import datetime, timedelta

API_KEY = '********'
API_SECRET = '********'
BEARER_TOKEN = '********'
CLIENT_ID = '********'
CLIENT_SECRET = '********'
ACCESS_TOKEN = '********'
ACCESS_TOKEN_SECRET = '********'
keep_alive()


def pull_next_quote():
    with open("quotes.txt", "r", encoding="utf8") as file:
        quotes = file.read().splitlines()
    quote = quotes.pop(0)
    quotes.append(quote)

    with open("quotes.txt", "w", encoding="utf8") as file:
        quotes = file.write("\n".join(quotes))
        print(quotes)

    return quote


client = tweepy.Client(BEARER_TOKEN, API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

auth = tweepy.OAuth1UserHandler(API_KEY, API_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
client_id = int(client.get_me().data.id)

while True:
    tweet = api.user_timeline(user_id=client_id, screen_name='Radical Feminist Quotes', count=1)[0]
    last_tweet_date = tweet.created_at.replace(tzinfo=None)
    print(last_tweet_date)
    next_tweet_time = last_tweet_date + timedelta(hours=2)
    print(next_tweet_time)
    if datetime.utcnow() > next_tweet_time:
        print("overdue")
        message = pull_next_quote()
        try:
            api.update_status(message)
        except:
            print(f"could not tweet {message}")
    else:
        print("not overdue")

    time.sleep(2350)

