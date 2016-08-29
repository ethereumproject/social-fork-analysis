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



#### Toolkit: Scraping & Storage
If we all agree to use the same set of easy to use tools early on, later we will be able to easily combine our scraping efforts. 

**Open source database**

**[LevelDB](https://github.com/DAddYE/leveldb)** is the tool we will be using to store our data. Regardless of whatever scraping tool you decide to use, stroing the extracted social media data within simple data structures inside a LevelDB snapshot will allow us to easily create scripts to combine and organize all collected data. 

[DAddYE's full Ruby implementation of LevelDB](https://github.com/DAddYE/leveldb)

**Installing Ruby LevelDB**

````
~/> brew install snappy
~/> gem install leveldb
~/>
irb -r leveldb
````

Once combined we can migrate the to a format that can be easily used with R for statistical analysis or migrated to an accessible full-text Lucene based search like Elastic to provide convient access to journalists and other researchers.

The advantage of using LevelDB is that a version exist written completely in Ruby meaning that the install process is as simple as installing any gem. It does not require the same setup process as full featured

#### Overview: Extracting and saving data

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
