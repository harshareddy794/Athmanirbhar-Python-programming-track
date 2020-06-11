# 6. Write a python program that prints all the numbers from  0 to 6 except 3 and 6
# Note: use ‘continue ‘statement. Expected output: 0 1 2 4 5
for i in range(0,6):
    if(i==3 or i==6):
        continue
    print(i)