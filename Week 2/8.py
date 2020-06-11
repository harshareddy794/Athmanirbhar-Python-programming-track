# 8. Write a python function to check whether the given number is Adam number or not
# EXAMPLE: Input: 12  Output: Adam Number  
# Explanation: 12*12=144 Reverse of 12 is 21→ 21*21=441 Reverse of 144==441

def adam(n):
    rev_mul=n*n
    n=(str(n))[::-1]
    n=int(n)
    mul_rev=n*n    
    if(rev_mul==int(str(mul_rev)[::-1])):
        print(True)
        return
    else:
        print(False)


n=int(input()) 
adam(n)