import sys
import json
#import nltk
import csv
import operator
from collections import defaultdict

state_to_code = {"VERMONT": "VT", "GEORGIA": "GA", "IOWA": "IA", "Armed Forces Pacific": "AP", "GUAM": "GU", "KANSAS": "KS", "FLORIDA": "FL", "AMERICAN SAMOA": "AS", "NORTH CAROLINA": "NC", "HAWAII": "HI", "NEW YORK": "NY", "CALIFORNIA": "CA", "ALABAMA": "AL", "IDAHO": "ID", "FEDERATED STATES OF MICRONESIA": "FM", "Armed Forces Americas": "AA", "DELAWARE": "DE", "ALASKA": "AK", "ILLINOIS": "IL", "Armed Forces Africa": "AE", "SOUTH DAKOTA": "SD", "CONNECTICUT": "CT", "MONTANA": "MT", "MASSACHUSETTS": "MA", "PUERTO RICO": "PR", "Armed Forces Canada": "AE", "NEW HAMPSHIRE": "NH", "MARYLAND": "MD", "NEW MEXICO": "NM", "MISSISSIPPI": "MS", "TENNESSEE": "TN", "PALAU": "PW", "COLORADO": "CO", "Armed Forces Middle East": "AE", "NEW JERSEY": "NJ", "UTAH": "UT", "MICHIGAN": "MI", "WEST VIRGINIA": "WV", "WASHINGTON": "WA", "MINNESOTA": "MN", "OREGON": "OR", "VIRGINIA": "VA", "VIRGIN ISLANDS": "VI", "MARSHALL ISLANDS": "MH", "WYOMING": "WY", "OHIO": "OH", "SOUTH CAROLINA": "SC", "INDIANA": "IN", "NEVADA": "NV", "LOUISIANA": "LA", "NORTHERN MARIANA ISLANDS": "MP", "NEBRASKA": "NE", "ARIZONA": "AZ", "WISCONSIN": "WI", "NORTH DAKOTA": "ND", "Armed Forces Europe": "AE", "PENNSYLVANIA": "PA", "OKLAHOMA": "OK", "KENTUCKY": "KY", "RHODE ISLAND": "RI", "DISTRICT OF COLUMBIA": "DC", "ARKANSAS": "AR", "MISSOURI": "MO", "TEXAS": "TX", "MAINE": "ME"}


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    state_total = defaultdict(int)
    state_sentiment = defaultdict(int)

    j=0
    doc_hash = {}
    maxlen=0
    for line in sent_file:
        data = line.split()
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
             words = text.split()
#             words = nltk.word_tokenize(text)
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
         if "place" in allTweets:
             place = allTweets["place"]
             if place is not None:
                 if(place["country"]=="United States"):
                     full_name = place["full_name"]
                     length = len(full_name)
                     ID = full_name[length-2:length]
                     if(ID == "US"):
                         state = full_name[:length-4]
                         ID = state_to_code[state.upper()]
                     if(ID.isupper()):
                         state_total[ID] += 1
                         state_sentiment[ID] += sentiment

    for key in state_total:
#        print key
#        print float(state_sentiment[key])/float(state_total[key])
        state_sentiment[key] = state_sentiment[key]/state_total[key]

    sorted_sentiment = sorted(state_sentiment.iteritems(), key=operator.itemgetter(1))
    print sorted_sentiment[-1][0]
#    for word in sorted_sentiment:
#        print word
#        print sorted_sentiment[1]
#         print("%s %f"%(word[0], word[1]))
#         print sentiment
if __name__ == '__main__':
    main()
