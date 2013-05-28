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
    matrixA = record[0]=="a"
    row = record[1]
    column = record[2]
    value = record[3]
    if matrixA: 
        for a in range(0,100):
            element = row, a
            mr.emit_intermediate(element, record)
    else:
        for b in range(0,100):
            element = b, column
            mr.emit_intermediate(element, record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    row = -1
    sum = 0
    for v in list_of_values:
        k = -1
        if v[0]=="a":
            k = v[2]
            for w in list_of_values:
                if w[0]=="b" and w[1]==k:
                    sum = sum + v[3] * w[3]
#                    if(key[0]==0 and key[1]==0): 
#                        print k
#                        print v[3]
#                        print w[3]
#x                        print "\n"
    if(sum != 0): mr.emit((key[0], key[1], sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
