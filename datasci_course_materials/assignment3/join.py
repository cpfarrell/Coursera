import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # value: order id
    value = record[1]
    mr.emit_intermediate(value, record)

def reducer(key, records):
    # key: order id
    # value: record
    for v in records:
        for u in records:
            if u[0] ==  "line_item" and v[0] == "order":
                mr.emit(v + u)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
