from datetime import datetime
import json
#from analysis import analyze, find_verified


#def process_one(data: dict, users: list):
#    isverified = find_verified(data["author_id"], users)
#
#    return analyze(data['text'].replace('\n', ' '), isverified, data["created_at"])


#def process_all(data: dict):
#    users = data["users"]
#
#    return list(map(lambda d: process_one(d, users), data['data']))


def tojson(file_format: str, data):
    dt = str(datetime.utcnow()).replace(':', '-').replace(' ', '_')[:-7]

    with open(f'{file_format}-{dt}.json', 'w') as fp:
        json.dump(data, fp, indent=4)


def read(file_name: str):
    with open(file=file_name) as f:
        return json.load(f)


#def run(file_name: str):
#    data = read(file_name)
#    tojson('twitter-results', process_all(data))
