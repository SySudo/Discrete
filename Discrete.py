import os
os.system('clear')

def partition(collection):
    if len(collection) == 1:
        yield [ collection ]
        return

    first = collection[0]
    for smaller in partition(collection[1:]):
        
        # insert `first` in each of the subpartition's subsets
        for n, subset in enumerate(smaller):
            yield smaller[:n] + [[ first ] + subset] + smaller[n+1:]
        
        # put `first` in its own subset
        yield [ [ first ] ] + smaller

x = int(input("|-----> "))
if x == 0:
    something = list(range(0,x+1))
else:
    something = list(range(1,x+1))

for n, p in enumerate(partition(something), 1):
    print(n, sorted(p))

partition(True)
