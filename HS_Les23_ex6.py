# Lesson 23
"""
6. Dictionary Merge:
○ Given two dictionaries, merge them into a new dictionary, excluding any keys
that start with an underscore.
"""


"""
HINT:
For excluding any keys that start with an underscore:
if k[0] != "_"
if not k.startswith("_")
import re /if re.match(r"^[^_]", k)
"""
# Case 1.
dic1 = {"_A": 10, "A": 10, "B": 100, "C": 1000}
dic2 = {"A": 10, "C": 500, "D": 1500, "E": 2000, "_F": 5000}

new_merged_dict = {k: v for i in [dic1, dic2] for k, v in i.items() if not k.startswith("_")}
print(new_merged_dict)


# Case 2. with update()

dic1 = {"_A": 10, "A": 10, "B": 100, "C": 1000}
dic2 = {"A": 10, "C": 500, "D": 1500, "E": 2000, "_F": 5000}
dic1_copy = dic1.copy()
dic1.update(dic2)

merged_dict = {k: v for k, v in dic1.items() if not k.startswith("_")}
print(merged_dict)

# Output: {'A': 10, 'B': 100, 'C': 500, 'D': 1500, 'E': 2000}


# Case 3.

dict1 = {"_A": 10, "A": 10, "B": 100, "C": 1000}
dict2 = {"A": 10, "C": 500, "D": 1500, "E": 2000, "_F": 5000}
new_dict = {}

for i in [dict1, dict2]:
    for k, v in i.items():
        if not k.startswith("_"):
            new_dict[k] = v
print(new_dict)

# Output: {'A': 10, 'B': 100, 'C': 500, 'D': 1500, 'E': 2000}
