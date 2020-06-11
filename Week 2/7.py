# Write a python function to check whether the given number is prime or not
n=int(input())
def prime(n):
    for i in range(2,n):
        if(n%i==0):
            print('Not prime')
            break
    else:
        print("Prime")
prime(n)