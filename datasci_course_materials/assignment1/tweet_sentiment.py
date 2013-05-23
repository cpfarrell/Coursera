import sys
import json
#import nltk
import csv

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    j=0
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
        j = j +1

    i = 0
    for line in tweet_file:
         allTweets = json.loads(line)
         sentiment = 0
         if "text" in allTweets:
             text = allTweets["text"]
#            words = nltk.word_tokenize(text) 
             words = text.split()
             i = i+1
             for idx, val in enumerate(words):
#             for word in words:
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
         print float(sentiment)
if __name__ == '__main__':
    main()