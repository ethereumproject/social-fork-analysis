# Twitter Search

install instructions

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
Setting
```
read({
        index : "etc",  // elasticsearch index
        q: "EthereumClassic",  // twitter tweets query
        since_id : 780158908763340800,  // twitter API since_id
        max_id : 876208908763340800,  // twitter API max_id
        step:50000000000000  // query tweets ID range
    });
```

Run `compile_twitter.js`
```sh
$ node compile_twitter.js
```

