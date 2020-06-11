# Take a list of Numbers or Names with repetitive values
# i. Get a list as output 
# ii.Each sublist has the number and how many times it is there in the list
# iii.The output should be in sorted order based on count
# iv.If the count is equal different numbers .sort them based on numbers
# Example: [23, 45, 23, 77, 67, 45, 45, 2, 3, 3, 2, 3] 
# Output   : [ [3,3], [45,3], [2,2], [23,2], [67,1], [77,1] ] 

inp=[23, 45, 23, 77, 67, 45, 45, 2, 3, 3, 2, 3]
val_dict={}
for i in inp:
    val_dict[i]=val_dict.get(i,0)+1
ans=[]    
for key,value in val_dict.items():
    lis=[]
    lis.append(key)
    lis.append(value)
    ans.append(lis)
ans.sort(key = lambda x: x[1],reverse=True)

for i in range(0,len(ans)-1):
    if(ans[i][1]==ans[i+1][1] and ans[i][0]>ans[i+1][0]):
        temp=ans[i]
        ans[i]=ans[i+1]
        ans[i+1]=temp
print(ans)