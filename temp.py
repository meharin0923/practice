list=[1,2,3,4,5,6]
k=0
for i in range(len(list)):
    if list[i]%2!=0:
       temp=list.pop(i)
       list.insert(k,temp)
       k+=1
print(list)
