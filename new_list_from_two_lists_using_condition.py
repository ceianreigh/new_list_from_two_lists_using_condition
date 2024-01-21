# Create a new list from two list using the following condition

# Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.

# pseudocode

# write the two given lists
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

# create a new list
new_list = []

# for each number in the first list
for number in list1:
    # if the number is odd
    if number % 2 != 0:
        # add the number to the new list
        new_list.append(number)

# for each number in the second list
for number in list2:
    # if the number is odd
    if number % 2 == 0:
        # add the number to the new list
        new_list.append(number)

# print the new list
print("The new list is: ", new_list)
