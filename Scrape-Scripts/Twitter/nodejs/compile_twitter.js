

//09-15  :  776208908763340800

let search_twitter = (() => {
    var _ref = _asyncToGenerator(function* (obj1) {
        return new Promise(function (resolve, reject) {

            client.get('search/tweets', {
                q: obj1.q,
                count: 100,
                since_id: obj1.since_id,
                max_id: obj1.since_id + obj1.step

            }, function (error, tweets, response) {
                console.log(error);
                //console.log(tweets.statuses[0].text);
                console.log("This time's search Quantity : " + tweets.statuses.length);
                if (tweets.statuses.length > 99) {
                    throw new Error("Tweets at this interval over 100 counts, need to re-snapshot!");
                }
                resolve(tweets.statuses);
            });
        });
    });

    return function search_twitter(_x) {
        return _ref.apply(this, arguments);
    };
})();

let es_create = (() => {
    var _ref2 = _asyncToGenerator(function* (obj1) {
        return new Promise(function (resolve, reject) {

            client_es.create({
                index: obj1.index,
                type: 'json',
                id: obj1.id,
                body: {
                    timestamp: obj1.timestamp,
                    doc: obj1.doc
                }
            }, function (error, response) {
                //console.log(error);
                resolve();
            });
        });
    });

    return function es_create(_x2) {
        return _ref2.apply(this, arguments);
    };
})();

let sleep = (() => {
    var _ref3 = _asyncToGenerator(function* (timeout) {
        return new Promise(function (resolve, reject) {
            setTimeout(function () {
                resolve();
            }, timeout);
        });
    });

    return function sleep(_x3) {
        return _ref3.apply(this, arguments);
    };
})();

let read = (() => {
    var _ref4 = _asyncToGenerator(function* (obj1) {

        for (var j = obj1.since_id; j < obj1.max_id; j = j + obj1.step) {
            console.log("tweet ID counter : " + j);
            yield sleep(5000);

            var tweets = yield search_twitter({
                q: obj1.q,
                since_id: j,
                step: obj1.step
            });

            //console.log(tweets);

            for (var i = 0; i < tweets.length; i++) {

                //console.log(tweets[i].text);
                var date_parse = new Date(Date.parse(tweets[i].created_at));
                var date = moment(date_parse);

                var x1 = yield es_create({
                    index: obj1.index,
                    id: tweets[i].id,
                    timestamp: date,
                    doc: tweets[i]
                });
            }
        }
    });

    return function read(_x4) {
        return _ref4.apply(this, arguments);
    };
})();

//EthereumClassic
//$ETC

//Latest count :  780158908763340800

function _asyncToGenerator(fn) { return function () { var gen = fn.apply(this, arguments); return new Promise(function (resolve, reject) { function step(key, arg) { try { var info = gen[key](arg); var value = info.value; } catch (error) { reject(error); return; } if (info.done) { resolve(value); } else { return Promise.resolve(value).then(function (value) { return step("next", value); }, function (err) { return step("throw", err); }); } } return step("next"); }); }; }

/**
 * Created by kimi on 2016/9/16.
 */
var Twitter = require('twitter');
var moment = require('moment');
var _ = require('lodash');

var elasticsearch = require('elasticsearch');

var client_es = new elasticsearch.Client({
    host: 'localhost:9200'
    //log: 'trace'
});

var client = new Twitter({
    consumer_key: process.env.TWITTER_CONSUMER_KEY,
    consumer_secret: process.env.TWITTER_CONSUMER_SECRET,
    access_token_key: process.env.TWITTER_ACCESS_TOKEN_KEY,
    access_token_secret: process.env.TWITTER_ACCESS_TOKEN_SECRET
});_asyncToGenerator(function* () {

    read({
        index: "etc",
        q: "EthereumClassic",
        since_id: 780158908763340800,
        max_id: 876208908763340800,
        step: 50000000000000
    });
})();
