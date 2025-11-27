"""Task 1: Calculating Shape Properties:"""


def get_option():
    """Get the option while not in "Square", "Circle", "Triangle", "Rectangle" and return this option. """
    option = ""
    while option not in ("Square", "Circle", "Triangle", "Rectangle"):
        option = str(input("The options available for calculation are:" \
        " 'Square', 'Circle', 'Triangle', 'Rectangle': ")).strip().title()

        if option not in ("Square", "Circle", "Triangle", "Rectangle"):
            print("Wrong option, try again!")
        
    return option


def shapes(option):
    """Calculate shape properties based on an option"""
    print(f"Chosen option: {option}")
    
    if option == "Square":
        while True:
            try:
                length = int(input("Please enter the length of the side of the square as an integer value: "))
                perimeter = length * 4
                area = length ** 2
                return f"Perimeter: {perimeter}\nArea: {area}"
            except ValueError:
                print("Invalid input. Please try again!")
    
    elif option == "Circle":
        while True:
            try:
                radius = float(input("Please enter the radius of the circle as a float value: "))
                circumference = radius * 2 * 3.14159
                area = 3.14159 * radius ** 2
                diameter = radius * 2
                return f"Circumference: {circumference}\nArea: {area}\nDiameter: {diameter}"
            except ValueError:
                print("Invalid input. Please try again!")
    
    elif option == "Triangle":
        while True:
            try:
                base = float(input("Please enter the base of the triangle as a numeric value: "))
                height = float(input("Please enter the height of the triangle as a numeric value: "))
                area = 0.5 * base * height
                return f"Area: {area}"
            except ValueError:
                print("Invalid input. Please try again!")
   
    elif option == "Rectangle":
        while True:
            try:
                length = float(input("Please enter the length of the rectangle as a numeric value: "))
                width = float(input("Please enter the width of the rectangle as a numeric value: "))
                perimeter = (2 * length) + (2 * width)
                area = length * width
                return f"Perimeter: {perimeter}\nArea: {area}"
            except ValueError:
                print("Invalid input. Please try again!")



art = r"""
   ______      __           __      __  _                _____ __                        ____                             __  _           __
  / ____/___ _/ /______  __/ /___ _/ /_(_)___  ____ _   / ___// /_  ____ _____  ___     / __ \_________  ____  ___  _____/ /_(_)__  _____/ /
 / /   / __ `/ / ___/ / / / / __ `/ __/ / __ \/ __ `/   \__ \/ __ \/ __ `/ __ \/ _ \   / /_/ / ___/ __ \/ __ \/ _ \/ ___/ __/ / _ \/ ___/ / 
/ /___/ /_/ / / /__/ /_/ / / /_/ / /_/ / / / / /_/ /   ___/ / / / / /_/ / /_/ /  __/  / ____/ /  / /_/ / /_/ /  __/ /  / /_/ /  __(__  )_/  
\____/\__,_/_/\___/\__,_/_/\__,_/\__/_/_/ /_/\__, /   /____/_/ /_/\__,_/ .___/\___/  /_/   /_/   \____/ .___/\___/_/   \__/_/\___/____(_)   
                                            /____/                    /_/                            /_/                                    
"""
print(art)

continue_calculating = ""
while continue_calculating != "n":
    option = get_option()   
    result = shapes(option)
    print(result)
    continue_calculating = str(input("Do you want to continue calculating? Type 'y' to continue and 'n' yo stp: "))