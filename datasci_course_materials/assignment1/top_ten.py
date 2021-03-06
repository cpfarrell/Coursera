import sys
import itertools
import json
#import nltk
#import re
import operator
from collections import defaultdict

def main():
    tweet_file = open(sys.argv[1])

    hashtotal = defaultdict(int)

    for json_tweet in tweet_file:
         tweet = json.loads(json_tweet)
         if "entities" in tweet:
             entities = tweet["entities"]
             if "hashtags" in entities:
                 hashtags = entities["hashtags"]
                 for hashtag in hashtags:
                     text = hashtag["text"]
                     hashtotal[text] += 1
#                     print hashtag["text"]

    sorted_total = sorted(hashtotal.iteritems(), key=operator.itemgetter(1))
    for word in reversed(sorted_total[-10:]):
         print("%s %.1f"%(word[0], word[1]))

if __name__ == '__main__':
    main()
