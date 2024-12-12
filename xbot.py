
import tweepy
import random
import schedule
import time
import logging
import os
from dotenv import load_dotenv


# Setup logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Replace these with your own credentials
load_dotenv()
consumer_id = os.getenv('CONSUMER_ID')
consumer_secret = os.getenv('CONSUMER_SECRET')
access_token = os.getenv('ACCESS_TOKEN')
access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuth1UserHandler(consumer_id, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

# Verify authentication
try:
    api.verify_credentials()
    logger.info("Authentication OK")
except Exception as e:
    logger.error("Error during authentication", exc_info=True)
    raise e

# Define your tips
tips = [
    """Use f-strings for cleaner string formatting: 
    ```
    name = "John" 
    age = 30
    print(f"Name: {name}, Age: {age}")
    ```
    """,
    
    """
    List comprehension for concise filtering:
    ```
    numbers = [1, 2, 3, 4, 5]
    evens = [x for x in numbers if x % 2 == 0]
    ```
    """,
    
    """
    Dictionary comprehension:
    ```
    squares = {x: x*x for x in range(5)}

    ```
    """,
    
    """
    Multiple assignments in one line:
    ```
    x, y, z = 1, 2, 3

    ```
    """,
    """
    Ternary operator for concise conditional assignment:
    ```
    result = "Even" if num % 2 == 0 else "Odd"
    ```
    """,
    """
    Use enumerate() for counter in loops:
    ```
    fruits = ['apple', 'banana', 'cherry']
    for i, fruit in enumerate(fruits):
        print(f"{i}: {fruit}")

    ```
    """,
    """
    Use zip() for parallel iteration:
    ```
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    for name, age in zip(names, ages):
        print(f"{name} is {age} years old.")
    ```
    """,
    """
    Use set() for efficient membership testing:
    ```
    numbers = [1, 2, 3, 4, 5]
    if 3 in numbers:
        print("3 is in the list.")
    ```
    """,
    """
    Use defaultdict for handling missing keys:
    ```
    from collections import defaultdict
    d = defaultdict(int)
    d['apple'] += 1
    ```
    """,
    """
    Use *args and **kwargs for flexible function arguments:
    ```
    def my_function(*args, **kwargs):
        print(args)
        print(kwargs)
    ```
    """,
    """
    Use lambda functions for concise one-line functions:
    ```
    square = lambda x: x**2
    ```
    """,
    """
    Use generator expressions for lazy evaluation:
    ```
    squares = (x**2 for x in range(5))
    ```
    """,
    """
    Use @property for computed attributes:
    ```
    class Circle:
        def __init__(self, radius):
            self._radius = radius
            @property
            def area(self):
            return 3.14 * self._radius**2
    ```
    """,
]

# Tweet a tip
def tweet_tip():
    tip = random.choice(tips)
    try:
        api.update_status(tip)
        logger.info(f"Tweeted: {tip}")
    except tweepy.TweepyException as error:
        if error.api_codes and 187 in error.api_codes:
            logger.warning("Duplicate status detected, trying another tip")
            tweet_tip()  # Try another tip if duplicate status error occurs
        else:
            logger.error(f"Error: {error}", exc_info=True)

# Respond to mentions
def respond_to_mentions():
    mentions = api.mentions_timeline(count=10)
    for mention in mentions:
        if not mention.favorited:
            try:
                api.create_favorite(mention.id)
                logger.info(f"Favorited mention by @{mention.user.screen_name}")
                reply_text = f"Thanks for the mention, @{mention.user.screen_name}! Here's a Python tip for you: {random.choice(tips)}"
                api.update_status(status=reply_text, in_reply_to_status_id=mention.id)
                logger.info(f"Replied to @{mention.user.screen_name}")
            except tweepy.TweepyException as error:
                logger.error(f"Error: {error}", exc_info=True)

# Schedule the bot
schedule.every(1).day.do(tweet_tip)  # Tweet a tip every day 
schedule.every(1).hour.do(respond_to_mentions)   # Check mentions every hour

while True:
    schedule.run_pending()
    time.sleep(1)




