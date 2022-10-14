# Author: Khalid Almotaery
# Date: 10/2/2022
# Projct: A* Puzzle Solver Agent

import random
import math
class Game:
    
    def __init__(self, n,array,h):
        self.board = [[0 for x in range(n)]  for y in range(n)]
        self.x = -1
        self.y = -1
        self.next = None
        self.steps = 0
        self.h = h
        self.initializeBoard(n,array)
       
    #expands a node
    def generateSubGames(self,n):
        arrayRep = self.arrayRep()
        self.leftState = Game(n, arrayRep,self.h)
        self.rightState = Game(n, arrayRep,self.h)
        self.upState = Game(n, arrayRep,self.h)
        self.downState = Game(n, arrayRep,self.h)

        self.leftState.moveSpace("l")
        self.rightState.moveSpace("r")
        self.upState.moveSpace("d")
        self.downState.moveSpace("u")

    #returns expnaded nodes
    def getSubs(self):
        return [self.leftState,self.rightState,self.upState,self.downState]

    #initialize the board
    def initializeBoard(self,n, array):
        digits = random.sample(range(0,n*n),(n*n))
        if array != []:
            digits = array
        counter = 0
        for row in range(0,n):
            for col in range(0,n):
                value = digits[counter]
                self.board[row][col] = value
                if value == 0:
                    self.x = col
                    self.y = row
                counter = counter + 1
    #prints the board
    def printBoard(self):
        n = len(self.board)
        s = ""
        for row in range(0,n):
            print("")
            s = s +"\n"
            for col in range(0,n):
                print(self.board[row][col],end="|")
                s = s + str(self.board[row][col])+"|"
        print("")
        s = s +"\n"
        return s
    #checks if current state is goal state
    def IS_GOAL(self):
        n = len(self.board)
        goal = list(range(0,n*n))
        state = self.arrayRep()
        if state == goal:
            return True
        else:
            return False
    #return f value of state based on the selceted h value 
    def f(self):
        if self.h == "h4":
            return self.g() + self.h4()
        elif self.h == "h3":
            return self.g() + self.h3()
        elif self.h == "h2":
            return self.g() + self.h2()
        else:
            return self.g() + self.h1()

    
    #returns the cost of getting at this state
    def g(self):
        return self.steps

    #increases the cost (g) of the current state
    def increaseCost(self):
        self.steps = self.steps + 1
    #implements H1
    def h1(self):
        n = len(self.board)
        goal = list(range(0,n*n))
        state = self.arrayRep()
        objectiveValue = (n*n)-1
        x = 0
        for digit in goal:
            if digit == state[x] and digit != 0:
                objectiveValue = objectiveValue - 1
            x = x + 1
        return objectiveValue
    #implements H2
    def h2(self):
        n = len(self.board)
        goal = list(range(0,n*n))
        goalState = Game(n,goal,self.h)
        sumDistance = 0
        for digit in goal:
            gameXY = self.getXYOf(digit,self.board)
            x1 = gameXY[0]
            y1 = gameXY[1]
            goalXY = self.getXYOf(digit,goalState.board)
            x2 = goalXY[0]
            y2 = goalXY[1]
            manhattanDistance = abs(x1-x2) + abs(y1-y2)
            sumDistance = sumDistance + manhattanDistance
        return sumDistance
    #implements H3
    def h3(self):
        array = self.arrayRep()
        swapCount = 0
        for i in reversed(range(1,len(array))):
            maxPos = i
            for j in range(0,i):
                if array[j] > array[maxPos]:
                    maxPos = j
            temp = array[maxPos]
            if array[i] != temp:
                swapCount = swapCount + 1
            array[maxPos] = array[i]
            array[i] = temp
        return swapCount

    #implements H4
    def h4(self):
        n = len(self.board)
        goal = list(range(0,n*n))
        goalState = Game(n,goal,self.h)
        sumDistance = 0
        for digit in goal:
            gameXY = self.getXYOf(digit,self.board)
            x1 = gameXY[0]
            y1 = gameXY[1]
            goalXY = self.getXYOf(digit,goalState.board)
            x2 = goalXY[0]
            y2 = goalXY[1]
            xs = (math.pow(x1-x2,2))
            ys = (math.pow(y1-y2,2))
            inside = xs + ys
            Distance = math.sqrt(inside)
            sumDistance = sumDistance + Distance
        return sumDistance
    #returns the % of misplaced tiles
    def percent(self):
        n = len(self.board)
        goal = list(range(0,n*n))
        state = self.arrayRep()
        objectiveValue = (n*n)
        x = 0
        for digit in goal:
            if digit == state[x]:
                objectiveValue = objectiveValue - 1
            x = x + 1
        return objectiveValue/((n*n))*100
    # helper function to get the x,y coordinates of a digit
    def getXYOf(self,digit,board):
        n = len(board)
        for row in range(0,n):
            for col in range(0,n):
                if digit == board[row][col]:
                    return [row,col]


    #returns an array representation of the board
    def arrayRep(self):
        n = len(self.board)
        state = []
        for row in range(0,n):
            for col in range(0,n):
                value = self.board[row][col]
                state.append(value)
        return state
    #hashes the array representation of the board
    def hashing(self):
        return hash(tuple(self.arrayRep()))

    #moves the blank space
    def moveSpace(self,command):
        n = len(self.board)
        if command == "l":
            if self.x > 0:
                self.board[self.y][self.x] = self.board[self.y][self.x-1] 
                self.x = self.x - 1
                self.board[self.y][self.x] = 0
                return True
            else: 
                return False

        if command == "r":
            if self.x < n-1:
                self.board[self.y][self.x] = self.board[self.y][self.x+1] 
                self.x = self.x + 1
                self.board[self.y][self.x] = 0
                return True
            else: 
                return False    

        if command == "u":
            if self.y > 0:
                self.board[self.y][self.x] = self.board[self.y-1][self.x] 
                self.y = self.y - 1
                self.board[self.y][self.x] = 0
                return True
            else: 
                return False  

        if command == "d":
            if self.y < n-1:
                self.board[self.y][self.x] = self.board[self.y+1][self.x] 
                self.y = self.y + 1
                self.board[self.y][self.x] = 0
                return True
            else: 
                return False     




    
        
