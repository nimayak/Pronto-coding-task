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
    print("""Available commands: \n
    * `F` - move forward 1 unit 
    * `B` - move backward 1 unit  
    * `R` - turn right 90 degrees 
    * `L` - turn left 90 degrees \n 
    example: `F1,R1,B2,L1,B3` \n""")
    command = input("Please enter command string: ")
    commandArray = command.split(",")
    print("Your input string: " + str(commandArray))
    moveRobot(commandArray)

def moveRobot(commandarray):
    # validation
    originalx = 0
    originaly = 0
    for elem in commandarray:
        if elem[0] == 'F':
            robot.y = robot.y + int(elem[1])
        elif elem[0] == 'B':
            robot.y = robot.y - int(elem[1])
        elif elem[0] == 'R':
            robot.x = robot.x + int(elem[1])
        elif elem[0] == 'L':
            robot.x = robot.x - int(elem[1])
    return calculateDistance(originalx, originaly, robot.x, robot.y)


def calculateDistance(x1,y1,x2,y2):
    p1 = [x1, y1]
    p2 = [x2, y2]
    distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
    print("The distance between the origin and the new position is: " + str(distance))

if __name__ == "__main__":
    main()

