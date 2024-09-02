# 5. LESSON
"""
4.Second smaller
Write a Python program to find the second smaller number in a list.
Sample Input                Sample Output
[1, 2, 3, 4]                2
[5, 7, 3, 9, 11]            5
[25, 1, 1, 13]              1
[1, 2, 1, 1]                1
"""
# 4. SOLUTION

# Case 1.

given_list = [1, 2, 3, 4]
smallest_num = given_list[0]
second_smaller = given_list[0]
helper = 0
double_sm = 0

for n in given_list:
    if second_smaller < n <= smallest_num:
        smallest_num = second_smaller
        second_smaller = n
    elif smallest_num <= n < second_smaller:
        second_smaller = n
    elif smallest_num > n <= second_smaller < smallest_num:
        smallest_num = n
    elif smallest_num >= n < second_smaller > smallest_num:
        second_smaller = smallest_num
        smallest_num = n
    elif smallest_num <= n > second_smaller < smallest_num:
        helper = second_smaller
        second_smaller = smallest_num
        smallest_num = helper
    elif second_smaller == smallest_num:
        double_sm = 0
        for j in given_list:
            if j == second_smaller:
                double_sm += 1
        if double_sm > 1:
            second_smaller = smallest_num
            double_sm = 0
        else:
            second_smaller = n
print(second_smaller)

# Output for the inputs [1, 2, 3, 4] [5, 7, 3, 9, 11] [25, 1, 1, 13] [1, 2, 1, 1] accordingly:
"""
2
5
1
1
"""

# Case 2.

given_list = [5, 7, 3, 9, 11]
nth = 2

if nth <= len(given_list):
    given_list.sort()
    print(given_list[nth - 1])
else:
    print("Nth element is out of range in the given list")

# Output: 5

