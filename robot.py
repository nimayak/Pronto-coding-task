# Woven graduate coding test
# Inputs: - a string of comma-separated commands eg `F1,R1,B2,L1,B3`
# Output: - the minimum amount of distance to get back to the starting point (`4` in this case)

import math

class Robot:
    x = 0
    y = 0
    direction = ""

robot = Robot()

def calculateDistance():
    p1 = [0, 0]
    p2 = [0, -4]
    distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    print(distance)

calculateDistance()