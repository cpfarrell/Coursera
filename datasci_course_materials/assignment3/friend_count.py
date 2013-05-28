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
    mr.emit_intermediate(friendA, friendB)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    friends = list()
    for v in list_of_values:
        if v not in friends:
            total += 1
            friends.append(v)
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
