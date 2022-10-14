# Author: Khalid Almotaery
# Date: 10/2/2022
# Projct: A* Puzzle Solver Agent

from operator import ne
import queue
from Game import Game
class Search:
    
    def __init__(self,n,initialState):
        self.arrayToGame = {} #maps a configuration hash to a game object
        self.hashToArray = {} 
        self.nodeCount = 0
        self.solved = False # seach is succesfull?

        self.arrayToGame[initialState.hashing()] = initialState
        self.solution = [] # the soultion path

        current = initialState
        self.h = current.h
        self.solution.append(initialState)
        #loops through the substates
        while current.IS_GOAL() == False:
            if self.nodeCount > 100000:
                break 
            nextHash = self.solve(current,n) 
            self.solution.append(self.arrayToGame[nextHash])
            current = self.arrayToGame[nextHash] 
            self.nodeCount = self.nodeCount + 1

        if current.IS_GOAL() != True:
            # print("Unsolved")
            self.solved = False
            k = 2
        else:
            self.solved = True

        current = self.arrayToGame[initialState.hashing()] 
        nextHash = current.hashing()
        z = 0
        while current.next != None:
            current = self.arrayToGame[current.hashing()]
           
            nextHash = current.next
            current = self.arrayToGame[nextHash]
            z = z+1
  
    #finds the best new state
    def solve(self,initialState,n):

        #creates substates:
        arrayRep = initialState.arrayRep()

        leftState = Game(n, arrayRep,self.h)
        rightState = Game(n, arrayRep,self.h)
        upState = Game(n, arrayRep,self.h)
        downState = Game(n, arrayRep,self.h)

        valid = []
        
        valid.append(leftState.moveSpace("l"))
        valid.append(rightState.moveSpace("r"))
        valid.append(upState.moveSpace("u"))
        valid.append(downState.moveSpace("d"))

        #checks if states have been visted and increase cost if it has been.
        try: 
            leftState = self.arrayToGame[leftState.hashing()]
            leftState.increaseCost()
        except:
            self.arrayToGame[leftState.hashing()] = leftState
        try: 
            rightState = self.arrayToGame[rightState.hashing()]
            rightState.increaseCost()
        except:
            self.arrayToGame[rightState.hashing()] = rightState
        try: 
            upState = self.arrayToGame[upState.hashing()]
            upState.increaseCost()
        except:
            self.arrayToGame[upState.hashing()] = upState
        try: 
            downState = self.arrayToGame[downState.hashing()]
            downState.increaseCost()
        except:
            self.arrayToGame[downState.hashing()] = downState
        
        states = [self.arrayToGame[leftState.hashing()],self.arrayToGame[rightState.hashing()],self.arrayToGame[upState.hashing()],self.arrayToGame[downState.hashing()]]

        valid = [True,True,True,True]

        #makes a list of valid substates

        validStates = []

        x = 0
        for v in valid:
            if v == True:
                validStates.append(states[x])
            x = x + 1
        try:
            nextState = validStates[0]
        except:
            print("unsolvable")
            exit()
        #gets the states with the lowest f value
        for i in range(1,len(validStates)):
            canddidate = validStates[i]
            if canddidate.f() < nextState.f():
                nextState = canddidate

        self.arrayToGame[nextState.hashing()].increaseCost()
        return nextState.hashing()


    
    




