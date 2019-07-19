# Woven graduate coding test
# Inputs: - a string of comma-separated commands eg `F1,R1,B2,L1,B3`
# Output: - the minimum amount of distance to get back to the starting point (`4` in this case)

import math

class Robot:
    x = 0
    y = 0
    direction = ""

robot = Robot()

def main():
    print("Woven graduate coding test - Robot CLI App \n")
    print("Available commands: \n * `F` - move forward 1 unit \n * `B` - move backward 1 unit \n * `R` - turn right 90 degrees \n * `L` - turn left 90 degrees \n example: `F1,R1,B2,L1,B3` \n")
    command = input("Please enter command: ")
    commandArray = command.split(",")
    print(commandArray)
    calculateDistance()

def calculateDistance():
    p1 = [0, 0]
    p2 = [0, -4]
    distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    print(distance)

if __name__ == "__main__":
    main()



