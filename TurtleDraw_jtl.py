# Jaiden Leonard
# CPSC-20000
# jaidentleonard@lewisu.edu
# Remedie#5020

import turtle

print('Say hello to Franklin.')

filename = input("Enter the name of the file containing your wishes for Franklin: ")

turtleFile = open(filename, 'r')
turtleTextLine = turtleFile.readline()

turtleWindow = turtle.Screen()
turtleWindow.setup(450, 450)

Franklin = turtle.Turtle()
Franklin.speed(10)
Franklin.penup()

total_distance = 0  # Create a variable to store the total distance

print("Your wish is Franklin's command.")

while turtleTextLine:
    print(turtleTextLine, end='')
    line = turtleTextLine.split()
    
    if (len(line) == 3): # The 3 words are color, x, and y.
        color = line[0]
        x = int(line[1])
        y = int(line[2])

        Franklin.color(color)
        distance = Franklin.distance(x, y)  # Calculate the distance traveled
        total_distance += distance  # Add the distance to the total distance
        Franklin.goto(x,y)
        Franklin.pendown()

    if (len(line) == 1): # The 1 word is “stop”.
        Franklin.penup()

    turtleTextLine = turtleFile.readline()

# Display the total distance at the end
text = "Total distance: {:.2f}".format(total_distance)
Franklin.penup()
x_pos = turtleWindow.window_width() // 2 - 50  # Set the x-coordinate to the right of the screen
y_pos = -turtleWindow.window_height() // 2 + 20  # Set the y-coordinate to the bottom of the screen
Franklin.setpos(x_pos, y_pos)  # Move the turtle to the bottom right corner of the screen
Franklin.write(text, font=('Arial', 12, 'normal'), align='right')

print('\nPress enter to say goodbye to Franklin.')

def close_program(): # Sets "close_program" to exit
    turtle.bye()

turtle.listen() # Looks for key presses
turtle.onkeypress(close_program, "Return" ) # Close program when the enter key is pressed

turtle.done()
turtleFile.close()
