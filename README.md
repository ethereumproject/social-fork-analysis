# Social Fork Analysis
A social network analysis is a recommended collection of tools being used to create a saved state of the all public social media data relating to the Ethereum hard-fork. The goal is to create an easy to use data set for journalists and researchers interested in exploring the affects of social media on the decision making process of the Ethereum community.

By creating a saved state, we can guarantee access to the primary source material that has not yet been edited or deleted so that future research, stories and investigations do not have to rely on what on biased articles published by cryptocurrency websites with low quality standards.

### Getting started
*Guide assumes you are using Debian/Ubuntu flavor of Linux but the package names used to install are typically the same. If they are not, use tab complete or search the internet for how to install the package on your operating system.*
To start you will want to first pull down the git repository and install ruby.

````
// If you do not yet have git or vim

~/>sudo apt-get install git-core vim
~/>git clone https://github.com/ethereumproject/social-fork-analysis.git
~/>cd social-fork-analysis

// Install Ruby using RVM (manages multiple ruby installations) or using package manager
// since the Ruby versions in the package manager are now 2+

// RVM Method
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby

// Package manager
sudo apt-get install ruby

// Check Ruby install
ruby -v

// Now you can install the database using the instructions below
````

#### Toolkit: Scraping & Storage
I'm going to be using Ruby for this project, but everyone is welcome to use whatever tools they like. I recommend using easier, higher level programming languages so this project is easy to contribute to. Long as everyone uses the same database, LevelD it will make combining our datasets together easier later. 

**Scraping tools**
It is recommended that you use either Ruby mechanize or a ready-only API client (use Github search, example `reddit read only api`). Once you decide on which to use, you can install the gem (the term used for libraries) and setup the database and start scripting. 


#### Using Mechanize
````
// Mechanize is a general purpose tool that can be used to access web sites
// that function without javascript enabled.

// Documentation: http://www.rubydoc.info/gems/mechanize/Mechanize/Page
//                http://mechanize.rubyforge.org/EXAMPLES_rdoc.html

gem install mechanize

cd Reddit/reddit_scrape.rb
// Read the docs and start coding
````

#### Using social media API Wrappers
The easiest solution is to simply use the large library of existing APIs for social media.
````
// Twitter API 

// Libraries
// https://github.com/sferik/twitter
// https://github.com/dbrown/twitter-search
// https://github.com/hayesdavis/grackle

// Reddit API
// Please add suggestions and make a pull request

// Git API
// Please add suggestions and make a pull request


// Other relevant social media? 
// Please add other relevant social media, recommended libraries
// and make a pull request


````

**Open source database**

**[LevelDB](https://github.com/DAddYE/leveldb)** is the tool we will be using to store our data. Regardless of whatever scraping tool you decide to use, stroing the extracted social media data within simple data structures inside a LevelDB snapshot will allow us to easily create scripts to combine and organize all collected data. 

[DAddYE's full Ruby implementation of LevelDB](https://github.com/DAddYE/leveldb)

**Installing Ruby LevelDB**

````

~/> gem install leveldb
~/> cd ScrapeScripts
~/> cd Reddit
~/> vim reddit_scrape.rb

db = LevelDB::DB.new './../Data'

# Writing
db.put('hello', 'world')
db['hello'] = 'world'

# Reading/Writing
db.fetch('hello', 'hello world') # => will write 'hello world' if there is no key 'hello'
db.fetch('hello'){ |key| 'hello world' } # => same as above

# Deleting
db.delete('hello')

# When you are done write data to file!
b.write!

// Create a fork or a new branch
// and push your changes to your new branch 
// then issue a pull request to add your data
// to the collection

````

Once combined we can migrate the to a format that can be easily used with R for statistical analysis or migrated to an accessible full-text Lucene based search like Elastic to provide convient access to journalists and other researchers.

The advantage of using LevelDB is that a version exist written completely in Ruby meaning that the install process is as simple as installing any gem. It does not require the same setup process as full featured

###


#### Overview: Extracting and saving data
The goal is to create an time line of available data public social data that help inform the public perception of the events. 



````

// DAO Hack Timeline
// 
time_of_hack     =  "6/17/2016 3:34:48 UTC"

ether_transfered = 3,641,694 
percent_of_all_ether_transferred = 31.6%

hacker’s main account +0x969837498944ae1dc0dcac2d0c65634c88729b2d

````


The scape tools included with this repository is designed to easily:

  (1) GET data from relevant social media servers,
  
  (2) extract data from the DOM, and
  
  (3) compile relevant data into simple data structures and store them within a LevelDB snapshot.
  

The scraping tools search defined social media networks, filtering relevant content created by the Ethereum community between:

    Time.new((DAO Catastrophe) - 7.days)) =< social_data < Time.now
  
Relevant content is extracted from the DOM and stored in a simple structure. 


## Save the state of public data
The primary purpose is to ensure a reliable saved state of all the relevant social media data exists and is freely available before social media content can be further modified or deleted. 

This software was initialized to create tools to faciliate research for an article I'm writing. Using hindsight clarity, the article looks back over the events, attempts to identify patterns and chronicle the events accurately as possible from the perspective of a unaffiliated but active developer.


### Development progress

| Social Media  | Contributors     | % Completed|
| ------------- |:----------------:|:----------:|
| reddit.com    | wig              | 5%         |
| twitter.com   | n/a              | 0%         |
| github.com    | n/a              | 0%         |

*Are you interested in volunteering to prevent historic resources are kept intact by building data-sets for journalists and researchers?*
*Use the table below to determine: what needs to be done, where you are capable of contributing and add your name to the cell. More than two volunteers can work on the same script, add your name using a comma separation.*

*If the scripts are built in a modular way, they can be improved and expanded to work for other events were social media data may be important.*
