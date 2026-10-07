my_list = [2,4,6,8,10,12,14]
print ("Original list is:",my_list)

sum = 0

for i in my_list:
    sum += i

mean = sum/len(my_list)

print ("The average of this list is:", mean)
print ("The sum of this list is:", sum)

my_list.sort

print ("The smallest number in this list is:",my_list[0])
print ("The largest number in this list is:", my_list[-1])