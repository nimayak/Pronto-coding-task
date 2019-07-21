# Woven graduate coding test
# Move a robot by telling it to go forwards or backwards or left or right.
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
    print("""Move a robot by telling it to go forwards or backwards or left or right.  
These commands must be  in the format <command><number>.  
For example 'L1' means 'turn left by 90 degrees once'.  
'B2' would mean go backwards 2 units. \n""")
    print("""Available commands: \n
    * `F` - move forward 1 unit 
    * `B` - move backward 1 unit  
    * `R` - turn right 90 degrees 
    * `L` - turn left 90 degrees \n 
    Example: `F1,R1,B2,L1,B3` \n""")
    command = input("Please enter command string: ")
    command_array = command.split(",")
    print("Your input string: " + str(command_array))
    valid_command_array = check_valid(command_array)
    x1, y1, x2, y2 = move_robot(valid_command_array)
    distance = calculate_distance(x1, y1, x2, y2)
    print("\n The distance between the origin and the new position is: " + distance)


def check_valid(command_array):
    for elem in command_array:
        if elem[0] in ('F', 'B', 'R', 'L') and isinstance(int(elem[1]), int):
            return command_array
        else:
            print("invalid input")


def move_robot(command_array):
    original_x = 0
    original_y = 0
    for elem in command_array:
        if elem[0] == 'F':
            robot.y = robot.y + int(elem[1])
        elif elem[0] == 'B':
            robot.y = robot.y - int(elem[1])
        elif elem[0] == 'R':
            robot.x = robot.x + int(elem[1])
        elif elem[0] == 'L':
            robot.x = robot.x - int(elem[1])
    return original_x, original_y, robot.x, robot.y


def calculate_distance(x1, y1, x2, y2):
    distance = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    return str(distance)


if __name__ == "__main__":
    main()
