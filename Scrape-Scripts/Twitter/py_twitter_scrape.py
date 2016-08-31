import json
import time
import plyvel
import tweepy

user_db = plyvel.DB('../../Data/Twitter/Users', create_if_missing=True)
tweet_db = plyvel.DB('../../Data/Twitter/Tweets', create_if_missing=True)

users = []
user_file = open('users', 'r')
for user in user_file:
    users.append(user.strip())

print(users)

# First use of DAO exploit 6/17/2016 3:34:48 UTC. Unix time: 
time_of_first_dao_exploit = 1466134488
catastrophe_period_start = time_of_first_dao_exploit - (60 * 60 * 24 * 7)

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

def write_to_tweet_db(status):
    tweet_dict = {'place': status._json['place'],
	'coordinates': status.coordinates,
	'source': status.source,
	'lang': status.lang,
	'is_quote_status': status.is_quote_status,
	'in_reply_to_status_id': status.in_reply_to_status_id,
	'created_at': status.created_at.timestamp(),
	'favorite_count': status.favorite_count,
	'contributors': status.contributors,
	'in_reply_to_screen_name': status.in_reply_to_screen_name,
	'in_reply_to_user_id_str': status.in_reply_to_user_id_str,
	'in_reply_to_status_id_str': status.in_reply_to_status_id_str,
	'entities': status.entities,
	'retweet_count': status.retweet_count,
	'geo': status.geo,
	'text': status.text,
	'author': status.author.id}
    tweet_db.put(bytes(status.id_str, 'utf-8'), bytes(json.dumps(tweet_dict), 'utf-8'))

def write_to_user_db(user):
    user_dict = {'contributors_enabled': user.contributors_enabled,
        'location': user.location,
        'created_at': user.created_at.timestamp(),
        'time_zone': user.time_zone,
        'default_profile': user.default_profile,
        'screen_name': user.screen_name,
        'statuses_count': user.statuses_count,
        'listed_count': user.listed_count,
        'favourites_count': user.favourites_count,
        'name': user.name,
        'followers_count': user.followers_count,
        'geo_enabled': user.geo_enabled}
    user_db.put(bytes(user.id_str, 'utf-8'), bytes(json.dumps(user_dict), 'utf-8'))


if __name__ == '__main__':
    keys = import_keys_from_config()
    auth = tweepy.OAuthHandler(keys['consumer_key'], keys['consumer_secret'])
    auth.set_access_token(keys['access_token'], keys['access_token_secret'])

    api = tweepy.API(auth)

    for user in users:
        print('Crawling %s' % user)
        for status in limit_handled(tweepy.Cursor(api.user_timeline, 
            id=user).items()):
                if status.created_at.timestamp() > catastrophe_period_start:
                    if not tweet_db.get(bytes(status.id_str, 'utf-8')):
                        print('Saving tweet: %s' % status.id_str)
                        write_to_tweet_db(status)
                    if not user_db.get(bytes(status.author.id_str, 'utf-8')): 
                        print('Saving user: %s' % status.author.id_str)
                        write_to_user_db(status.author)


