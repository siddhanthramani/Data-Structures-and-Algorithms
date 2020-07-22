import turtle


def main():

    # creates a turtle graphic window to draw in
    t = turtle.Turtle()
    # the screen is used at the end of the program
    screen = t.getscreen()

    filename = input('Enter name of file to be opened : ')

    file = open(filename, 'r')

    for line in file:
        # print(line)  # tells us that \n is present in each line
        # thus we strip it off
        text = line.strip()
        # to separate the fields

        command_list = text.split(',')

        if command_list[0] == 'goto':
            x = float(command_list[1])
            y = float(command_list[2])
            width = float(command_list[3])

            color = command_list[4].strip()
            t.width = width
            t.pencolor = color
            t.goto(x, y)
        elif command_list[0] == 'circle':
            radius = float(command_list[1])
            width = float(command_list[2])
            color = command_list[3].strip()
            t.width = width
            t.pencolor = color
            t.circle(radius)

        elif command_list[0] == 'beginfill':
            color = command_list[1].strip()
            t.fillcolor(color)
            t.begin_fill()

        elif command_list[0] == 'endfill':
            t.end_fill()

        elif command_list[0] == 'penup':
            t.penup()

        elif command_list[0] == 'pendown':
            t.pendown()

        else:
            print('Command not found in file : ', command_list[0])

    # closes the file handler
    file.close()

    # hides the turtle that we used to draw the picture
    t.ht()

    # causes turtle screen to stay on till we mouse click
    screen.exitonclick()

    print('Program execution is complete. ')


if __name__ == "__main__":
    main()
