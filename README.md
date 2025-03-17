# Twitter Bot for Python Tips

This is a Python script that tweets random Python programming tips and responds to mentions on Twitter. It uses the Tweepy library to interact with the Twitter API and the `schedule` library to schedule tasks.

## Features

- Tweets a random Python programming tip every minute.
- Responds to Twitter mentions every hour with a thank you message and a random Python tip.
- Avoids tweeting duplicate tips by checking for duplicate status errors.

## Setup

1. **Clone the repository:**

```bash
git clone https://github.com/vanillabush/twitter-python-tips-bot.git
cd twitter-python-tips-bot
```
2. Install the required packages:
```
pip install tweepy python-dotenv schedule

```
3. Create a .env file in the project root and add your Twitter API credentials:
```
CONSUMER_ID=your-consumer-id
CONSUMER_SECRET=your-consumer-secret
ACCESS_TOKEN=your-access-token
ACCESS_TOKEN_SECRET=your-access-token-secret

```

Dependencies
tweepy: For interacting with the Twitter API.

schedule: For scheduling tasks.

logging: For logging info, warnings, and errors.

os and dotenv: For loading environment variables from a .env file.



### License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Developed with 💻 and 🧠 by Ohia Ikenna MarkHenry (2024)

