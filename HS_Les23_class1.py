# Lesson 23
"""
Comprehension exercises
* Write a list comprehension to print this output
*
**
***
****
*****
******
*******
********
*********
"""
# Case 1
my_list = ["*" * i for i in range(1, 10)]
helper = "\n".join(my_list)
print(helper)
"""
Output:
*
**
***
****
*****
******
*******
********
*********
"""

# Case 2
g_list = [["*" for i in range(j)] for j in range(1, 10)]

for i in g_list:
    print("".join(i))
"""
Output:
*
**
***
****
*****
******
*******
********
*********
"""

# Ex 2. Create new dict from the existing one having v % 2 == 0

# Shortest case

my_dic = {"A": 9, "B": 15, "C": 26, "D": 18, "E": 32}
my_new_dic = {k: v for k, v in my_dic.items() if v % 2 == 0}
print(my_new_dic)

# Output: {'C': 26, 'D': 18, 'E': 32}


# Case with filter

my_dic = {"A": 9, "B": 15, "C": 26, "D": 18, "E": 32}

my_dict = {k: v for k, v in filter(lambda item: item[1] % 2 == 0, my_dic.items())}
print(my_dict)

# Output: {'C': 26, 'D': 18, 'E': 32}


# filter with __next__().
my_dict = {filter(lambda k: my_dic[k] == v, my_dic.keys()).__next__(): v for v in
           tuple(filter(lambda v: v % 2 == 0, my_dic.values()))}
print(my_dict)

# Output: {'C': 26, 'D': 18, 'E': 32}

# longer case
hlp = {}
for k, v in my_dic.items():
    if v % 2 == 0:
        hlp[k] = v
print(hlp)

# Output: {'C': 26, 'D': 18, 'E': 32}


# The Longest case: not optimal
helper1 = {}
for v in tuple(filter(lambda v: v % 2 == 0, my_dic.values())):
    for k in my_dic.keys():
        if my_dic[k] == v:
            helper1[k] = v
print(helper1)

# Output: {'C': 26, 'D': 18, 'E': 32}
