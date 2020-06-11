# 1. Read two lists from the user. Two lists contain the names of students
#     i.Get the Names which are there in both lists
#     ii.Get the Names which are there in atleast one list 
#     iii.Get the Names which are there in List1 not there in List2
#     iv.Get  the names  which  are there in List2 not there in List1
list1=['student1','student2','student4','student6','student9']
list2=['student1','student3','student5','student4','student10']
print(set(list1) & set(list2))
print(set(list1) | set(list2))
print(set(list1) - set(list2))
print(set(list2) - set(list1))