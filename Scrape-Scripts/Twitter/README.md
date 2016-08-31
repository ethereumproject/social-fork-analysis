#### Scraping with Python

Using Tweepy (https://tweepy.readthedocs.io/en/v3.5.0/index.html) and Plyvel (https://plyvel.readthedocs.io/en/latest/).
The script will save all posts from shortly before the Dao Catastrophe to present. 

##### Setup:
System install of LevelDB required:

    apt-get install libleveldb1 libleveldb-dev
    pip3 install tweepy plyvel

Create a file of users to scrape, one user name per line, in the same directory as the script.

##### To scrape:

    python3 py_twitter_scrape.py
