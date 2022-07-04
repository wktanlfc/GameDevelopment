import math
import os
import random
import re
import sys
import matplotlib as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Complete the 'rotateLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER d
#  2. INTEGER_ARRAY arr
#blah.pop()
#blah = [1,2,3,4,5]
#blah[0:3]
#blah[3:]
def rotateLeft(d, arr):
    wkqueue = arr[:d] # create a queue for FIFO arr[:d]
    laterhalf = arr[d:]
    return laterhalf + wkqueue

# Complete the 'matchingStrings' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY strings
#  2. STRING_ARRAY queries
# Testing Code 
# type(queries)
blahblah = ['ab', 'ab' , 'abc']
queriessample = ['ab', ' abc', 'bc']

def matchingStrings(strings, queries):
    holder = {}
    for string in strings:
        pass
        for query in queries:
            if query == string:
                #print('Yes ' + query + ' is in ' + string)
                holder[query] = holder.get(query, 0) + 1 # Look up what does .get do tomorrow.
            else:
                holder[query] = holder.get(query, 0) 
    samplelist = []
    for k,v in holder.items():
        samplelist.append(v)
    return samplelist

matchingStrings(blahblah, queriessample)

strings = ['ab', 'ab' , 'abc']
queries = ['ab', 'abc', 'bc']
holder = {}
for string in strings:
    pass
    for query in queries:
        if query == string:
            # print('Yes ' + query + ' is in ' + string)
            holder[query] = holder.get(query, 0) + 1 # Look up what does .get do tomorrow.
        else:
            holder[query] = holder.get(query, 0) #print('No ' + query + ' is NOT in ' + string) 

samplelist = []
for k,v in holder.items():
    samplelist.append(v)

print(samplelist)


sns.histplot()