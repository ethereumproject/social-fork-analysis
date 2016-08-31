# Social Fork Analysis
A social network analysis is a recommended collection of tools being used to create data extraction scripts that can be used to create a saved state of the all public social media data relating to the Ethereum hard-fork. This project is a citizen journalism project, based upon public citizens "playing an active role in the process of collecting, reporting, analyzing, and disseminating news and information."

The goal is to create an easy to use data set for journalists and researchers interested in exploring the affects of social media on the decision making process of the Ethereum community.

By creating a saved state, we can guarantee access to the primary source material that has not yet been edited or deleted so that future research, journalistic articles and investigations do not have to rely on biased articles published by often biased cryptocurrency websites with low quality standards.

### Getting started with citizen journalism
Everyone participating is welcome to use whatever tools they like, but I recommend using easier, higher level programming languages so this project is widely accessible for anyone interested in collaboration. Making it accessible to anyone interested in participating is what makes citizen journalism possible. 

Start by cloning the git repository and installing a high level langague like Ruby or Python. I will be using Ruby in this guide.

#### Ruby install guide
````
# If you do not yet have git

sudo apt-get install git-core
git clone https://github.com/ethereumproject/social-fork-analysis.git
cd social-fork-analysis

# Install Ruby using RVM (manages multiple ruby installations) or using package manager
# since the Ruby versions in the package manager are now 2+

# RVM Method
gpg --keyserver hkp://keys.gnupg.net --recv-keys 409B6B1796C275462A1703113804BB82D39DC0E3
curl -sSL https://get.rvm.io | bash -s stable --ruby

# Package manager
sudo apt-get install ruby

# Check Ruby install
ruby -v

# Now you can install the database using the instructions below
````

#### Data extraction 
One of the easiest ways to approach data extraction, or data scraping from social media is to use either the library mechanize (which exists for Ruby, Python and Perl), or alternatively a read-only API client (use Github search, example `reddit read only api`). Once you decide on which library (referred to as a gem in Ruby) one just needs to install the library and start scripting. 

##### What data is important?
Deciding which data is important for archival purposes is up to the citizen journalist doing the extracting, combining these different perspectives together allows us to create a complete as possible data set for later use.

Citizen journalists can decide what content to filter out of the social media content created by the Ethereum community, for example filtering all content within a range of one week from the DAO exploit:

````
# The fork was prompted by
# an exploit used in a contract

# First use of DAO exploit was 6/17/2016 3:34:48 UTC
# In Unix time:
time_of_first_dao_exploit = 1466134488
# Seven days in unix time:
7_days = (60 * 60 * 24 * 7)

# If created before now OR created after
# the seven days prior to the first exploit
if social_data.created_at < Time.now ||
  Time.new((time_of_first_dao_exploit) - 7_days)) <= social_data.created_at
  # Extract and save data
end
````

##### Using Mechanize
````
# Mechanize is a general purpose tool that can be used to access web sites
# that function without javascript enabled.

# Documentation: http://www.rubydoc.info/gems/mechanize/Mechanize/Page
#                http://mechanize.rubyforge.org/EXAMPLES_rdoc.html

gem install mechanize

cd Reddit/reddit_scrape.rb
# Read the docs and start coding
````

##### Using social media API Wrappers
The easiest solution is to simply use the large library of existing APIs for social media.

````
# Twitter API 

# Libraries
# https://github.com/sferik/twitter
# https://github.com/dbrown/twitter-search
# https://github.com/hayesdavis/grackle

# Reddit API
# Please add suggestions and make a pull request

# Git API
# Please add suggestions and make a pull request

# Other relevant social media? 
# Please add other relevant social media, recommended libraries
# and make a pull request
````

#### Saving Extracted Data
Combining extracted data from participatins will be easiest if we use the same database, I recommend using LevelDB, but any simple database can be used.

LevelDB is a commonly used simple embedded database that requires no setup. It is initialized inline, and is just a collection of hashes/dictionaries which are automatically compressed. Only one process can access the LevelDB database at any one time, which is not a problem for simple extraction scripts.

**[LevelDB](https://github.com/DAddYE/leveldb)** is a Ruby implementation of LevelDB that is used in the guide. It is not as fast as the C++ implementation but for the purposes of this project it works well and is easy to use.

##### Installing Ruby LevelDB

````
# Dependencies 
# OSX
brew install snappy
# Debian & Ubuntu
sudo apt-get install libleveldb1v5 libleveldb-dev

# Install leveldb gem
gem install leveldb
````
##### Saving extracted data with Ruby LevelDB

````
# Ruby LevelDB Example 
# A simple script to show of how to save 
# extracted data. 
#
# If a database already exists, use unique keys
# to avoid overwriting existing data. If in doubt
# if your keys are unique, print all the values.

# Print all hashes/dictionaries in the database
def print_database(db)
  print "========\n"
  # Print database
  print "Database\n"
  print "========\n"
  db.each { |key, val| puts "Key: #{key}, Val: #{val}\n" }
end

# Presuming you already scraped the tweets
Tweets = scraped_tweets
# Init the DB
db = LevelDB::DB.new './../Data'
Tweets.each_with_index do |tweet, index|
  extracted_tweet = {"id" => tweet.id, "created_at" => tweet.date_data, "name" => tweet.name, "text" => tweet.post}
  # Store based on local iterative index
  db["tweet_#{index}_#{tweet.id}"] = tweet
  # Database changes are automatically compressed and saved
  print_database(db)
end
````  

##### After data has been collected

Once collected data is combined we can migrate them to a format and build simple scripts so that it that can be easily used with R for statistical analysis or migrated to an accessible full-text Lucene based search like Elastic to provide convenient access to journalists, citizen journalists and other researchers.


### Citizen journalism collaborative progress
Are you interested in volunteering to guarantee that important primary resources are kept intact by building data-sets for journalists and researchers? Use the table to determine: what needs to be done, and sign up to a task you are capable of contributing to. Once you decide add your name to the cell, more than two volunteers can work on the same social media as they are likely to prioritize different relevant content.

| Social Media        | Contributors     | % Completed|
| ------------------- |:----------------:|:----------:|
| reddit.com          | wig              | 5%         |
| twitter.com         | kimi, beholder0x2a             | 40%         |
| github.com          | n/a              | 0%         |
| forum.daohub.org    | n/a              | 0%         |









