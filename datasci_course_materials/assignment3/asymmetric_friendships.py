import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    friendA = record[0]
    friendB = record[1]
    lowerA=False
    friends = friendB, friendA
    if(friendA<friendB):
        lowerA=True
        friends = friendA, friendB
#    if friendA == "Valjean" and friendB == "Myriel":
#        print friendA + " " + friendB + "\n"
#        print friends
#    if friendB == "Valjean" and friendA == "Myriel":
#        print friendA + " " + friendB + "\n"
#        print friends
    mr.emit_intermediate(friends, lowerA)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    friend1 = key[0]
    friend2 = key[1]
    trueFound=False
    falseFound=False
    for v in list_of_values:
#        if friend2 == "Valjean" and friend1 == "Myriel": print v
        if v == True: trueFound = True
        if v == False: falseFound= True
    #if(not trueFound): mr.emit((friend2, friend1))
    #if(not falseFound): mr.emit((friend1, friend2))
    if(not falseFound or not trueFound):
        mr.emit((friend2, friend1))
        mr.emit((friend1, friend2))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
