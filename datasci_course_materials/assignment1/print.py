import urllib
import json

for i in range(1,10):
   response = urllib.urlopen("http://search.twitter.com/search.json?q=microsoft&page=" + str(i))
   allTweets = json.load(response)
   for line in allTweets["results"]:
#      print line
      print line["text"]
