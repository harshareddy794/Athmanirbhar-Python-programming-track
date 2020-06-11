# 4. Write a python function that checks whether a passed string is palindrome or not
inp=['hello','malayalam','Lunch','madam']
for i in inp:
    if(i==i[::-1]):
        print(True)
    else:
        print(False)