n=5
a=[45,78,33,97,13]
b=[66,89,23,97,54]
p=0
q=0
for i in range(n):
    if(a[i]>b[i]):
        p+=1
    elif(b[i]>a[i]):
        q+=1
    else:
        continue
print("Alice",p)
print("Bob",q)
if(p>q):
  print("Alice won the competition")
else:
  print("Bob won the competition")
