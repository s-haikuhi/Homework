# 4. LESSON: ARITHMETIC OPERATIONS
"""
9.Line Segment:
You are given four real numbers - the coordinates of two points on a
plane. The first two numbers are the x and y coordinates of the first point,
and the last two numbers are the x and y coordinates of the second point.
Output the length of the line segment bounded by the two points.
Sample Input        Sample Output
1    2.2               3.9924
2.5 -1.5

0.0 0.0                 5
3.0 4.0
"""

# 9. SOLUTION
"""
In XOY coordinate system with 0 start point:
X is abscissa:  x-axis coordinate of a point , 
Y is Ordinate:  y-axis coordinate of a point 
"""

x1, y1 = 1, 2.2         # coordinates of P1 point
x2, y2 = 2.5, -1.5      # coordinates of P2 point

"""
H is the point of P2H and P1H perpendicular lines intersection.

P1HP2 is a right angled triangle, as P2H and P1H are perpendicular lines.
Based on Pythagoras theorem: P1P2**2 = P1H**2 + P2H**2
"""
P2H = x2 - x1
P1H = y1 - y2
P1P2 = (P2H ** 2 + P1H ** 2) ** 0.5
print(str(P1P2)[:6])

# Output: 3.9924


# Case 2.
"""
In XOY coordinate system with 0 start point:
X is abscissa:  x-axis coordinate of a point , 
Y is Ordinate:  y-axis coordinate of a point 
"""

x1, y1 = 0, 0  # coordinates of P1 point
x2, y2 = 3.0, 4.0  # coordinates of P2 point


"""
H is the point of P2H and P1H perpendicular lines intersection.
P2H = x2 - x1
P1H = y1 - y2

P1HP2 is a right angled triangle, as P2H and P1H are perpendicular lines.
Based on Pythagoras theorem: P1P2**2 = P1H**2 + P2H**2
"""
P1P2 = ((x2 - x1) ** 2 + (y1 - y2) ** 2) ** 0.5

print(str(P1P2)[0])

# Output: 5
