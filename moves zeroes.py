a=[2,0,5,6,0,7]
for i in a:
    if i==0:
       a.remove(0)
       a.append(0)
print(a)