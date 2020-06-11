# 5. Write a python program to count the number of even and odd numbers from a series of numbers
# saample numbers: numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9] 
# Expected output: Number of even numbers: 4 Number of odd numbers: 5 
val_dict={}
numbers= [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in numbers:
    if(i%2==0):
        val_dict['even']=val_dict.get('even',0)+1
    else:
        val_dict['odd']=val_dict.get('odd',0)+1
print("Number of even numbers: "+str(val_dict['even']))
print("Number of odd numbers: "+str(val_dict['odd']))