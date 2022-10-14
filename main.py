# Author: Khalid Almotaery
# Date: 10/2/2022
# Projct: A* Puzzle Solver Agent

from cmath import log
import configparser
from distutils.command.config import config
from Game import Game
from Search import Search
import time
import ast
import random
from configparser import ConfigParser

import logging   

#seting up the log
file = 'config.ini'
config = ConfigParser()
config.read(file)
logging.basicConfig(filename='output.log',encoding='utf-8', level=logging.DEBUG)
    
def main():
    #choosing the mode
    if config["Mode"]["ExperMode"] == "True":
        experiment()
    if config["Mode"]["SolveOneMode"] == "True":
        solveOne()
    if config["Mode"]["Generator"] == "True":
        makeSolvableGames(int(config["Generator"]["EdgeSize"]))

#running experiments
def experiment():
    alledges = config["Experiment"]["AllEdges"]
    edge2 = config["Experiment"]["Edge2"]
    edge3 = config["Experiment"]["Edge3"]
    edge4 = config["Experiment"]["Edge4"]
    Puzzles2 = config["Experiment"]["Puzzles2"]
    Puzzles2 = ast.literal_eval(Puzzles2)
    Puzzles3 = config["Experiment"]["Puzzles3"]
    Puzzles3 = ast.literal_eval(Puzzles3)
    Puzzles4 = config["Experiment"]["Puzzles4"]
    Puzzles4 = ast.literal_eval(Puzzles4)
    
    if alledges == "True" or edge2 == "True":
        e2(Puzzles2)
    if alledges == "True" or edge3 == "True":
        e3(Puzzles3)
    if alledges == "True" or edge4 == "True":
        e4(Puzzles4)

#solving one puzzle
def solveOne():
    n = int(config["SolveOne"]["EdgeSize"])
    h = config["SolveOne"]["Heuristic"]
    Puzzle = config["SolveOne"]["Puzzle"]
    Puzzle = ast.literal_eval(Puzzle)
    initialState = Game(n,Puzzle,h)
    start = time.time()
    search = Search(n,initialState)
    end = time.time()
    execTime = end - start
    print("#Soution Steps#")
    logging.info("#Soution Steps#")
    sols = search.solution
    for sol in sols:
        s = str(sol.printBoard())
        logging.info(s)
    print("#Performance#")
    logging.info("#Performance#")
    print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
    logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    
#running tests for edge size 4
def e4(initials):
    n = 4
    #h1
    for initial in initials:
        h = "h1"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h2
    for initial in initials:
        h = "h2"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h3
    for initial in initials:
        h = "h3"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h4
    for initial in initials:
        h = "h4"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))

#running tests for edge size 3
def e3(initials):
    n = 3
    #h1
    for initial in initials:
        h = "h1"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h2
    for initial in initials:
        h = "h2"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h3
    for initial in initials:
        h = "h3"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h4
    for initial in initials:
        h = "h4"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))

#running tests for edge size 4
def e2(initials):
    n = 2

    #h1
    for initial in initials:
        h = "h1"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h2
    for initial in initials:
        h = "h2"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h3
    for initial in initials:
        h = "h3"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))
    #h4
    for initial in initials:
        h = "h4"
        initialState = Game(n,initial,h)
        start = time.time()
        search = Search(n,initialState)
        end = time.time()
        execTime = end - start
        print("#Soution Steps#")
        logging.info("#Soution Steps#")
        sols = search.solution
        for sol in sols:
            s = str(sol.printBoard())
            logging.info(s)
        print("#Performance#")
        logging.info("#Performance#")
        print("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount)) 
        logging.info("Edge Size: "+str(n)+", Heuristic: "+h+", "+str(initialState.percent())+"% Misplaced, Time: "+str(execTime)+" seconds, Number of Nodes Expanded: "+str(search.nodeCount))

#generates random solvable puzzles
def makeSolvableGames(n):
    goal = list(range(0,n*n))
    games = []
    solveable = []
    for i in range(0,10):
        sample = random.sample(goal,len(goal))
        if games.count(sample) == 0:
            games.append(sample)
    b = 0
    for game in games:
        initialState = Game(n,game,"h1")
        search = Search(n,initialState)
        if search.solved == True:
            solveable.append(game)
            logging.info(str(game))
            print(game)
            b = b+1
    return solveable




if __name__ == "__main__":
    main()