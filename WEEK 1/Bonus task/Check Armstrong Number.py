num=int(input())
split_num=list(map(int,str(num)))
n=len(split_num)
ans=0
for i in split_num:
    ans+=i**n
if(ans==num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")