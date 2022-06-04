import json
from os import getenv
from datetime import datetime as dt, timedelta as td
from dotenv import load_dotenv
from requests import get

import fileutils

MAX_COUNT = 100
MAX_CALLS = 100


def call(startingtime: str, endtime: str) -> dict:
    load_dotenv()

    token = getenv('TWEETER_TOKEN')

    response = get(
        url="https://api.twitter.com/2/tweets/search/recent",
        params={
            'query': '"PROUNI" -is:retweet -is:reply lang:pt',
            'max_results': MAX_COUNT,
            'sort_order': 'relevancy',
            'start_time': startingtime,
            'end_time': endtime,
            'expansions': 'author_id',
            'tweet.fields': 'id,created_at,text,public_metrics',
            'user.fields': 'id,created_at,verified,public_metrics'
        },
        headers={'Authorization': f"Bearer {token}"})

    if response.ok:
        print("REQUEST OK!")
        return json.loads(response.content)
    else:
        print("SOMETHING WENT WRONG...")
        print(response.status_code)
        raise Exception(response.text)


def get_hours(interval: int):
    date = dt.now() - td(hours=interval)
    return date.isoformat()[:-3] + 'Z'


def main():
    calls = {
        'data': [],
        'users': []
    }
    hour_interval = 0

    try:
        for i in range(MAX_CALLS):
            if hour_interval == (7 * 24 - 3):  # limite de 7 dias da API (-3 pra corrigir timezone)
                break
            hour_interval += 3
            result = call(startingtime=get_hours(hour_interval), endtime=get_hours(hour_interval - 3))
            if result.get('data') is not None \
                    and result.get('includes') is not None \
                    and result['includes']['users'] is not None:
                calls['data'] += result.get('data')
                calls['users'] += result['includes']['users']
    except Exception as e:
        print(e)
    finally:
        if len(calls.get('data')) <= 0:
            return
        print(f"FETCHED {len(calls['data'])} TWEETS.")
        fileutils.tojson('tweets', calls)
        print("JSON CREATED!")


if __name__ == "__main__":
    main()
