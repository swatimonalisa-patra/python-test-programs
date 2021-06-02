import itertools
n=6
m=12
a=[1,5,7,12,16,23]
for i in itertools.combinations(a,2):
    if(i[0]!=i[1]):
        if(i[0]+i[1]==m):
            print((a.index(i[0])+1),end=' ')
            print((a.index(i[1])+1))
        else:
            continue
    else:
        continue
