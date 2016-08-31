require 'leveldb'
require 'json'

def load_config(file_path = 'config.json')
  return JSON.parse(File.read(file_path))
end

def print_database(db)
  print "========\n"
  # Print database
  print "Database\n"
  print "========\n"
  db.each { |key, val| puts "Key: #{key}, Val: #{val}\n" }
end

# Init Database
db = LevelDB::DB.new './../../Data/Twitter'

print_database(db)

# Init Database Snapshot

test_tweet = {"id" => "0", "name" => "test", "text" => "tweet text"}

10.times do |index|
  db["tweet_#{index}"] = test_tweet
end

