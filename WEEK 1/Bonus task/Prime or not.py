n=int(input())
for i in range(2,n//2):
    if(n%i==0):
        print("Not prime number")
        break
        exit()
else:
    print("Prime number")