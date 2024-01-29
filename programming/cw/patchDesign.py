from graphics import *

# helper function to draw each arrow for patchwork P
def arrow(win, topLeft, colour, borderColour):
    bottomLeft = Point(topLeft.x, topLeft.y+10)
    topMiddle = Point(bottomLeft.x+10, bottomLeft.y)
    bottomMiddle = Point(topMiddle.x, topMiddle.y+10)
    topRight = Point(topLeft.x+20, topLeft.y)
    bottomRight = Point(topRight.x, bottomLeft.y)

    arrow = Polygon(topLeft, topMiddle, topRight, bottomRight, bottomMiddle, bottomLeft)
    arrow.setFill(colour)
    arrow.setOutline(borderColour)
    arrow.draw(win)

# function that draws patchwork P
def patchworkP(win, topLeft, colour):
    for y in range(0, 100, 20):
        for x in range(0, 100, 20):
            if y in (20, 60) and x in (20, 60):
                arrow(win, Point(topLeft.x + x, topLeft.y + y), 'white', colour)
            else:
                arrow(win, Point(topLeft.x+x, topLeft.y+y), colour, colour)


# function that draws patchwork F
def patchworkF(win, topLeft, colour):
    center = Point(topLeft.x+50, topLeft.y+95)
    rad = 5
    for i in range(10):
        ring = Circle(center, rad)
        ring.setOutline(colour)
        ring.draw(win)
        center.move(0, -5)
        rad += 5


# function that draws a plain square
def plainPatchwork(win, topLeft, colour):
    bottomRight = Point(topLeft.x+100, topLeft.y+100)
    plainSquare = Rectangle(topLeft, bottomRight)
    plainSquare.setFill(colour)
    plainSquare.setOutline(colour)
    plainSquare.draw(win)


# function to decide what colour each patch should be
def colourDecider(point, dimension, colours):
    pointX, pointY = point.x, point.y
    middle = int(dimension/2)
    if pointX < 100 or pointX >= dimension-100 or middle+50 > pointY >= middle-50:
        return colours[0]
    elif pointY < middle:
        return colours[2]
    else:
        return colours[1]


# core function that uses all patchwork drawing functions to create the main design
def drawDesign(win, dimension, colours):
    isPatchF = True
    for y in range(0, dimension, 100):
        for x in range(0, dimension, 100):
            topLeft = Point(x, y)
            colour = colourDecider(topLeft, dimension, colours)
            if isPatchF:
                patchworkF(win,topLeft, colour)
            else:
                if colour == colours[0]:
                    plainPatchwork(win, topLeft, colour)
                else:
                    patchworkP(win,topLeft, colour)
            isPatchF = not isPatchF


# function that allows the user to choose a window size
def dimensions():
    while True:
        selection = input('''
Please select a dimension
5) 5x5
7) 7x7
9) 9x9
''')
        if selection in ['5', '7', '9']:
            return int(selection)
        else:
            print('ERROR - INVALID OPTION')


# function that allows the user to choose 3 valid colours
def colourPick(validColours):
    colours = []
    while len(colours) < 3:
        print('The valid colours are as followed;')
        for i in validColours:
            if i != validColours[-1]:
                print(i, end=', ')
            else:
                print(i)

        colourSelection = input(f'\nPlease select colour {len(colours) + 1}: ').lower()

        if colourSelection in validColours and colourSelection not in colours:
            colours.append(colourSelection)
            print()

        elif colourSelection in colours:
            print('\nCOLOUR ALREADY PICKED\n')

        else:
            print('\nINVALID COLOUR\n')

    return colours


# start of the program
def main():
    size = dimensions()*100
    validColours = ['red', 'green', 'blue', 'magenta', 'orange', 'yellow', 'cyan']
    colours = colourPick(validColours)
    win = GraphWin('Patchwork Design', size, size)
    drawDesign(win, size, colours)
    win.mainloop()


# testing function for easy program testing
def testing():
    dimension = 500
    colours = ['blue', 'red', 'orange']
    win = GraphWin('Patchwork Design', dimension, dimension)
    drawDesign(win, dimension, colours)
    win.mainloop()
