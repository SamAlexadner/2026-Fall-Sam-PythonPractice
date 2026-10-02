import turtle

SQUARE = "1"
CIRCLE = "2"
TRIANGLE = "3"
QUIT = "4"

def main():
    #TODO: reference lecture5 slide#65 to call the function to draw the requested shape until user chooses to quit
    display_menu()
    choice = 0
    choice = input("Enter your choice: ")
    while choice != QUIT:
        if choice == SQUARE:
            square_x_coordinate = float(input("Enter the starting X coordinate: "))
            square_y_coordinate = float(input("Enter the starting Y coordinate: "))
            square_length = float(input("Enter the length of a side: "))
            square_color = input("Enter the fill color: ")
            square(square_x_coordinate, square_y_coordinate, square_length, square_color)
            display_menu()
            choice = input("Enter your choice: ")

        elif choice == CIRCLE:
            circle_x_coordinate = float(input("Enter the X coordinate of the center: "))
            circle_y_coordinate = float(input("Enter the Y coordinate of the center: "))
            circle_radius = float(input("Enter the radius: "))
            circle_color = input("Enter the fill color: ")
            circle(circle_x_coordinate, circle_y_coordinate, circle_radius, circle_color)
            display_menu()
            choice = input("Enter your choice: ")

        elif choice == TRIANGLE:
            triangle_x_coordinate = float(input("Enter the  staring X coordinate: "))
            triangle_y_coordinate = float(input("Enter the Y coordinate of the center: "))
            triangle_length = float(input("Enter the length of a side: "))
            triangle_color = input("Enter the fill color: ")
            equilateral_triangle(triangle_x_coordinate, triangle_y_coordinate, triangle_length, triangle_color)
            display_menu()
            choice = input("Enter your choice: ")

        else:            
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
            display_menu()
            choice = input("Enter your choice: ")
    print("Exiting the program.")
    turtle.done()

def display_menu():
    print()
    print("Shape Menu")
    print("1) Draw a Square")
    print("2) Draw a Circle")
    print("3) Draw an Equilateral Triangle")
    print("4) Quit")

#TODO: copy the code from lecture5 slide# 69
def square(x, y, side, color):
    turtle.penup()            # Raise the pen​
    turtle.goto(x, y)         # Move to (X,Y)​
    turtle.fillcolor(color)   # Set the fill color​
    turtle.pendown()          # Lower the pen​
    turtle.begin_fill()       # Start filling​
    for count in range(4):    # Draw a square​
        turtle.forward(side)
        turtle.left(90)
    turtle.end_fill()         # End filling​
    pass
   
#TODO: copy lecture slide 71 code
def circle(x, y, radius, color):
    turtle.penup()             # Raise the pen​
    turtle.goto(x, y - radius) # Position the turtle​
    turtle.fillcolor(color)    # Set the fill color​
    turtle.pendown()           # Lower the pen​
    turtle.begin_fill()        # Start filling​
    turtle.circle(radius)      # Draw a circle​
    turtle.end_fill()          # End filling​
pass

def equilateral_triangle(x, y, side, color):
    # draw a triangle starting coordinate at x,y
    turtle.penup()     
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown()
    turtle.begin_fill()
    for count in range(3):
        turtle.forward(side)
        turtle.left(120)
    turtle.end_fill()

if __name__ == "__main__":
    main()

