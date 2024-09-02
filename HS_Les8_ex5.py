# Lesson 8. Sets
"""
Exercise 5:
You are given three lists, list1, list2, and list3. Your task is to implement a
program that takes these lists and prints the following:
Case 1. The set of elements that are common to all three lists.
Case 2. The set of elements that are present in at least two of the three lists, but not in all
three.
Case 3. The set of elements that are unique to each list (present in only one list).
"""
list1 = {100, 200, 300, 400, 500, 600, 900}
list2 = {300, 350, 400, 450, 500, 550, 600, 650, 700, 750, 800}
list3 = {500, 520, 540, 560, 580, 600, 620, 640, 660, 680, 700, 800, 900, 1000, 1500}

# Case 1. The set of elements that are common to all three lists.
target_list = list1 & list2 & list3
print(target_list)

# Output: Common to all three lists:
#  {600, 500}

# Case 2. The set of elements that are present in at least two of the three lists, but not in all three.
target_list = ((list1 & list2) - list3) ^ ((list1 & list3) - list2) ^ ((list2 & list3) - list1)
print(target_list)

# Output: Present in at least 2 lists, but not in all 3:
# {800, 900, 300, 400, 700}

# Case 3. The set of elements that are unique to each list (present in only one list).
target_list = (list1 - list2 - list3) | (list2 - list1 - list3) | (list3 - list1 - list2)
print(target_list)

# Output: Unique to each list:
# {640, 450, 580, 200, 520, 650, 660, 1500, 540, 350, 100, 550, 680, 1000, 620, 750, 560}


