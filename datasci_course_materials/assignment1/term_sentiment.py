import sys
import itertools
import json
#import nltk
import re
from collections import defaultdict

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    wordsent = defaultdict(int)
    wordtotal = defaultdict(int)

    doc_hash = {}
    maxlen=0
    for line in sent_file:
        data = line.split()
        #print line                                                                                                                                                                  
        length = len(data)
        if(length > maxlen): maxlen = length
        word = data[0]
        for k in range(1, length-1):
            word = word + " " + data[k]
        doc_hash[word] = int(data[length-1])


    for json_tweet in tweet_file:
        tweet = json.loads(json_tweet)
        if "text" in tweet:
             text = tweet["text"]
             words = text.split()
#             words = nltk.word_tokenize(text)
             sentiment = 0
             for idx, val in enumerate(words):
                 if val in doc_hash:
                     sentiment += doc_hash[val]
                 if(len(words) - idx > 1):
                     twowords = val + " " + words[idx+1]
                     if twowords in doc_hash:
                         sentiment += doc_hash[twowords]
                 if(len(words) - idx > 2):
                     threewords = val + " " + words[idx+1] + " " + words[idx+2]
                     if threewords in doc_hash:
                         sentiment += doc_hash[threewords]

             for word in words:
                 valid=True
#                 valid = re.match('^[\w-]+$', word) is not None
                 if(valid):
                     wordsent[word] += int(sentiment)
                     wordtotal[word] += 1

    for key in wordtotal:
         average = float(wordsent[key])/float(wordtotal[key])
         print("%s %.2f"%(key, average))

if __name__ == '__main__':
    main()
