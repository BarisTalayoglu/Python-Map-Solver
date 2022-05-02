
#ReadMe
#hello Mr. Nowak,
#we used turtle library to visualize depth first search algorithm and 
#implemented by the fastest way possible, we hope you enjoy! Time Complexity= O(n^2) 
# Barış Talayoğlu, Burak Padır, Ozan Aydın Sahkulubey

# firstly, our code traversing all possibilities and than it shows the fastest solution

import turtle
import time
import os
from mapReader import MapReader



visual = turtle.Screen()
visual.bgpic('bg.gif')
visual.title("Team Alpha Male Fast Maze Solver")
visual.setup(1200,800)
time.sleep(3)
visual.bgpic('')
visual.bgcolor("black")


startX = 0
startY = 0
endX = 0
endY = 0

class dfsMaze(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)


class visitedNodes(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("yellow")
        self.penup()
        self.speed(0)

class frontierNodes(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("circle")
        self.color("green")
        self.penup()
        self.speed(0)


class startNode(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("orange")
        self.setheading(270)
        self.penup()
        self.speed(0)


class endNode(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)


maps = MapReader.getMapContent("map1.txt")



def createMaze(file):
    global startX, startY, endX, endY
    for y in range(len(file)):
        for x in range(len(file[y])):
            char = file[y][x]
            screenX = -588 + (x * 24)
            screenY = 288 - (y * 24)

            if char == "+":
                maze.goto(screenX, screenY)
                maze.stamp()
                walls.append((screenX, screenY))

            if char == " ":
                path.append((screenX, screenY))

            if char == "e":
                endN.goto(screenX, screenY)
                endN.stamp()
                endX, endY = screenX, screenY
                path.append((screenX, screenY))

            if char == "s":
                startX, startY = screenX, screenY
                startN.goto(screenX, screenY)

def dfsTraversal(x,y):
    frontier.append((x, y))
    solution[x, y] = x, y
    while len(frontier) > 0:
        time.sleep(0)
        current = (x,y)

        if(x - 24, y) in path and (x - 24, y) not in visited:
            leftNode = (x - 24, y)
            solution[leftNode] = x, y
            frontierN.goto(leftNode)
            frontierN.stamp()
            frontier.append(leftNode)

        if (x, y - 24) in path and (x, y - 24) not in visited:
            bottomNode = (x, y - 24)
            solution[bottomNode] = x, y
            frontierN.goto(bottomNode)
            frontierN.stamp()
            frontier.append(bottomNode)

        if(x + 24, y) in path and (x + 24, y) not in visited:
            rightNode = (x + 24, y)
            solution[rightNode] = x, y
            frontierN.goto(rightNode)
            frontierN.stamp()
            frontier.append(rightNode)

        if(x, y + 24) in path and (x, y + 24) not in visited:
            upperNode = (x, y + 24)
            solution[upperNode] = x, y
            frontierN.goto(upperNode)
            frontierN.stamp()
            frontier.append(upperNode)

        x, y = frontier.pop()
        visited.append(current)
        visitedN.goto(x,y)
        visitedN.stamp()
        if (x,y) == (endX, endY):
            endN.stamp()
        if (x,y) == (startX, startY): 
            startN.stamp()

def backRoute(x, y):
    endN.goto(x, y)                      
    endN.stamp()
    while (x, y) != (startX, startY):
        endN.goto(solution[x, y])
        endN.stamp()
        x, y = solution[x, y]


maze = dfsMaze()
startN = startNode()
frontierN = frontierNodes()
visitedN = visitedNodes()
endN = endNode()
walls = []
path = []
visited = []
frontier = []
solution = {}

createMaze(maps)
dfsTraversal(startX, startY)
backRoute(endX, endY)

visual.exitonclick()