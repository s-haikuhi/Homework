# 4. LESSON: ARITHMETIC OPERATIONS
"""
12.Line Segment Intersection
You are given four real numbers- a1, b1, a2, b2 - The endpoints of two
line segments on a line. Find the length of their intersection. Note that the
order of the endpoints of a segment is irrelevant, i.e. the segments [1;2]
and [2;1] are considered the same.
Sample Input                Sample Output
1 4                         0
9 7

1 2.5                       0.5
3 2

10 0                        0.1
0.1 0.2
"""
# 11. SOLUTION

a1, a2 = 1, 2.5
b1, b2 = 3, 2
intersection_len = 0

if a1 - a2 > 0 < b1 - b2 and a2 < b2 < a1 <= b1:
    intersection_len += a1 - b2
elif a1 - a2 > 0 < b1 - b2 and a2 < b2 < a1 > b1:
    intersection_len += b1 - b2
elif a1 - a2 < 0 < b1 - b2 and a1 < b2 < a2 <= b1:
    intersection_len += a2 - b2
elif a1 - a2 < 0 < b1 - b2 and a1 < b2 < a2 > b1:
    intersection_len += b1 - b2
elif a1 - a2 > 0 > b1 - b2 and a2 < b1 < a1 <= b2:
    intersection_len += a1 - b1
elif a1 - a2 > 0 > b1 - b2 and a2 < b1 < a1 > b2:
    intersection_len += b2 - b1
elif a1 - a2 < 0 > b1 - b2 and a1 < b1 < a2 <= b2:
    intersection_len += a2 - b1
elif a1 - a2 < 0 > b1 - b2 and a1 < b1 < a2 > b2:
    intersection_len += b2 - b1
elif a1 - a2 > 0 < b1 - b2 and b2 <= a2 < b1 >= a1:
    intersection_len += a1 - a2
elif a1 - a2 > 0 < b1 - b2 and b2 <= a2 < b1 < a1:
    intersection_len += b1 - a2
elif a1 - a2 > 0 > b1 - b2 and b1 <= a2 < b2 >= a1:
    intersection_len += a1 - a2
elif a1 - a2 > 0 > b1 - b2 and b1 <= a2 < b2 < a1:
    intersection_len += b2 - a2
elif a1 - a2 < 0 < b1 - b2 and b2 <= a1 < b1 >= a2:
    intersection_len += a2 - a1
elif a1 - a2 < 0 < b1 - b2 and b2 <= a1 < b1 < a2:
    intersection_len += b1 - a1
elif a1 - a2 < 0 > b1 - b2 and b1 <= a1 < b2 >= a2:
    intersection_len += a2 - a1
elif a1 - a2 < 0 > b1 - b2 and b1 <= a1 < b2 < a2:
    intersection_len += b2 - a1
else:
    intersection_len = 0
print(intersection_len)

# Outputs for the cases [1 4, 9 7], [1 2.5, 3 2], [10 0, 0.1 0.2] accordingly
"""
0
0.5
0.1
"""
