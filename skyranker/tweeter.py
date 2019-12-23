import os
import urllib

import sqlalchemy
from dotenv import load_dotenv
import twitter

load_dotenv()

api = twitter.Api(
    consumer_key=os.getenv("CONSUMER_KEY"),
    consumer_secret=os.getenv("CONSUMER_SECRET"),
    access_token_key=os.getenv("ACCESS_TOKEN"),
    access_token_secret=os.getenv("ACCESS_SECRET"),
)

engine = sqlalchemy.crea

def get_tweets(query):
    results = api.GetSearch(raw_query=query)
    return results


if __name__ == "__main__":
    params = {
        "q": "hope skywalker strikes phantom",
        "since": "2019-12-20",
        "result_type": "recent",
        "count": 100,
    }
    query = urllib.parse.urlencode(params)
    print(query)
    results = get_tweets(query)
    print(results)
