n=5
a=["New","Old","Existing","New","New"]
b=set(a)
for i in b:
    count=0
    if(i in a):
        count+=1
    else:
        continue
    print(i,end=' ')
    print(len(i),end=' ')
    print(count)
