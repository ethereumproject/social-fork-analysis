# Ethereum Classic Tweets Scraping / elasticsearch
![Image of Yaktocat](http://i.imgur.com/m2UaJhJ.png)

After downloading the latest elasticsearch release
```sh
$ bin/elasticsearch
```

Ethereum Classic Tweets Scraping install instructions

Install Babel
```sh
$ npm install --save-dev babel-cli -g
```

Install node.js dependencies
```sh
$ npm install
```

Run Babel Cli
```sh
$ babel twitter.js --watch --out-file compile_twitter.js
```
Modify `twitter.js`
```sh
$ nano twitter.js
```
Setting1
```
read({
        index : "etc",  // elasticsearch index
        q: "EthereumClassic",  // twitter tweets query
        since_id : 780158908763340800,  // twitter API since_id
        max_id : 876208908763340800,  // twitter API max_id
        step:50000000000000  // query tweets ID range
    });
```
Setting2
```
var client = new Twitter({
    consumer_key: TWITTER_CONSUMER_KEY,
    consumer_secret: TWITTER_CONSUMER_SECRET,
    access_token_key: TWITTER_ACCESS_TOKEN_KEY,
    access_token_secret: TWITTER_ACCESS_TOKEN_SECRET
});
```

Run `compile_twitter.js`
```sh
$ node compile_twitter.js
```

if you have meet some error messages, like
```
Error("Tweets at this interval over 100 counts, need to re-snapshot!");
```
it mean the captured Tweets are over 100, but the Twitter API only send 100 Tweets back.
You need to re-adjust the Setting1's step smaller to ensure captured tweets are below 100.
the console will also show the currently tweet id index, you can restart the script from last interrupt.


### Datasets
Please install **elasticsearch-dump**, more information please check below link
https://github.com/taskrabbit/elasticsearch-dump

After installed and **download the test datasets**, please Run
```sh
$ elasticdump --input=/home/{your User Name}/{your data foler}/etc20160926.json --output=http://127.0.0.1:9200/{your index} --type=data
```

#####  etc20160926.json
https://mega.nz/#!A1gigBTL
[Key]  
!DpD5kqiO9DefaBl1hBvjFWv26d5KH1RrH9E8susHtfk

