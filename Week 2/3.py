# 3. [PERMUTATIONS ] A permutation of a list is another list with the same elements, but in a possibly different order.     
# Example: [1, 2, 1] is a permutation of [2, 1, 1], but not of [1, 2, 2]. 
# Write a function is permutation(list1, list2): bool that returns True if its  Arguments are permutations of each other. 
from itertools import permutations
def permutation(lis1,lis2):
    lis1=''.join(lis1)
    lis2=''.join(lis2)
    lis1=list(permutations(lis1))
    perms=[]
    for i in lis1:
        perms.append(''.join(i)) 
    if(lis2 in perms):
        return True
    else:
        return False

lis1=list(map(str,[1,1,2]))
lis2=list(map(str,[2,1,1]))
print(permutation(lis1,lis2))