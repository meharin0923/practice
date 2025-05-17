def generate(ind,curr,ans,digit,combo):
    if(ind==len(digit)):
        ans.append(curr)
        return
    i=int(digit[ind])
    for j in combo[i]:
        generate(ind+1,curr+j,ans,digit,combo)
def letter(digit):
    if(len(digit)==0):
        return []
    ind=0
    curr=""
    ans=[]
    combo=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    generate(ind,curr,ans,digit,combo)
    return ans
digit=str(input())
print(letter(digit))

