from itertools import groupby, zip_longest
from operator import itemgetter

SENTINEL = object()

keyfunc = itemgetter(0)
compact = lambda *x: [(yield values) for values,_ in groupby(zip_longest(*x, fillvalue=SENTINEL), keyfunc)]
#def compact(*x):
#    for values,_ in groupby(zip_longest(*x, fillvalue=SENTINEL), keyfunc):
#        yield values

