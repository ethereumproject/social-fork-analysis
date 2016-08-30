import json
import time
import plyvel
import tweepy

db = plyvel.DB('../../Data/Twitter', create_if_missing=True)

def import_keys_from_config():
    config_file = open('config.json', 'r')
    config_string = config_file.read()
    key_json = json.loads(config_string)
    return(key_json)

def limit_handled(cursor):
    while True:
        try:
            yield cursor.next()
        except tweepy.RateLimitError:
            print('RateLimitError')
            time.sleep(60)
        except tweepy.TweepError:
            print('tweepy.TweepError')
            time.sleep(60)


if __name__ == '__main__':
    keys = import_keys_from_config()
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])

    api = tweepy.API(auth)

# Notes

for status in limit_handled(tweepy.Cursor(api.user_timeline, 
    id='avsa').items()):
        # process status here
        # if status.created_at > catastrophe_period_start:
        #     write_to_db


