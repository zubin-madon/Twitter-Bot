# Twitter-Bot
## Twitter Bot in Python Tweepy:
1. Get a Twitter Developer account with elevated access. 
2. Get all the keys and tokens, copy paste them in appropriate places.

### Workings:
**RadFembot.py** tweets out quotes every 2 hours. The timestamp of the last tweet is checked against `utcnow()` and if it has been over two hours since the last tweet, 
the bot will tweet the next one. As each quote is tweeted, `the pull_next_quote()` function transfers the quote to the bottom of the page in the txt file.
**Veebot.py** works similarly with trivia.txt, only difference being it replies to @mentions of whatever user id you choose. It can be your bot's own ID or someone else's. Flask app because I like to run it on replit with cron jobs scheduled to wake it up every now and then.
