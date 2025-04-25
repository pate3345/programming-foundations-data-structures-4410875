''' 
Problem Statement: Compute the average number of pets each student 
has in a given class. 
'''

#Simple array
student_pet_count_list = [0,1,2,3,4,1,2,3,4,2,2,1,1]

#Find the total student size.

student_in_class = len(student_pet_count_list)

# print(student_in_class)

# sum = 24
# avg = (sum/student_in_class)
# print("avg is",avg)

sum = 0
for i in student_pet_count_list:
    sum = sum + i
print(sum)

