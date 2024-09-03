# Lesson 21
"""
7. Tuple Exercise:
Write a function that swaps the values of two tuples.
"""


# Case 1.

def swap_tuples(tuple1, tuple2):
    tuple1, tuple2 = tuple2, tuple1
    return tuple1, tuple2


print(swap_tuples((1, 2, 3, 4), ("eins", "zwei", "drei", "vier")))

# Output: (('eins', 'zwei', 'drei', 'vier'), (1, 2, 3, 4))


# Case 2.    Longest way

def swap_tuples(tuple1, tuple2):
    n = 0
    tuple1 = list(tuple1)
    tuple2 = list(tuple2)

    for i in tuple1:
        tuple1[n] = tuple2[n]
        tuple2[n] = i
        n += 1
    return tuple(tuple1),tuple(tuple2)


print(swap_tuples((1, 2, 3, 4), ("eins", "zwei", "drei", "vier")))

# Output: (('eins', 'zwei', 'drei', 'vier'), (1, 2, 3, 4))
