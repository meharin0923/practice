list=[2,0,5,6,0,7]
for i in list:
    if i==0:
       list.remove(0)
       list.append(0)
print(list)
    #timecomplexity : O(n)