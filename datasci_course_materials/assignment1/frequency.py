import sys
import itertools
import json
#import nltk
#import re
import operator
from collections import defaultdict

def main():
    tweet_file = open(sys.argv[1])

    wordtotal = defaultdict(int)
    totalwords=0

    for json_tweet in tweet_file:
         tweet = json.loads(json_tweet)
         if "text" in tweet:
             text = tweet["text"]
             words = text.split()
#             words = nltk.word_tokenize(text)
             for word in words:
                 valid=True
#                 valid = re.match('^[\w-]+$', word) is not None
                 if(valid):
                     wordtotal[word] += 1
                     totalwords += 1

#    f = open('solution3.txt', 'w')             
    sorted_total = sorted(wordtotal.iteritems(), key=operator.itemgetter(1))
    for word in sorted_total:
         average = float(word[1])/totalwords
         print("%s %f"%(word[0], average))

if __name__ == '__main__':
    main()
