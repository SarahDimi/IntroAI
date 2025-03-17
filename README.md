# 2048 Game - using Minimax Algorithm
<b>Source code by: ColumbiaEDX - Artificial Intelligence Course - Micro Master</b><br />
<b>By: Guillermo Andres De Mendoza Corrales </b>, memoodm@gmail.com, Colombia, Bogota D.C.<br />
Language: Python 3.6<br />
Description: Minimax Algorithm that finds the best move for the 2048 game

## 1. 2048 Game

![game2048](https://github.com/memoodm/game2048/blob/master/images/game2048.png)

An instance of 2048 is played in a 4x4 grid, with numbered tiles that slide in all four directions. In every turn, a new tile will randomly appear in an empty slot on the board, with a value of either 2 or 4. The player can slide the tiles in all the four directions (Up, Down, Left and Right). As per the input direction given by the player, all tiles on the grid slide as far as possible in that direction, until (1) they either collide with another tile or (2) collide with the edge of the grid. If two tiles with the same number collide, then they merge into a single tile with value twice as that of the individual tiles. It has to be noted that the resulting tile will not collide with another tile in the same move. In this project, the game of 2048 is solved using the Minimax algorithm. Here, 2048 is treated as an adversarial game where the player is the computer which is attempting to maximize the value of the highest tile in the grid and the opponent is the computer which randomly places tiles in the grid to minimize the maximum score. Minimax algorithm would be suitable in this case as the game is played between opponents with a known motive of maximizing/minimizing a total score


## 2. Minimimax Algorithm Overview

![minmax](https://github.com/memoodm/game2048/blob/master/images/minmax.png)

A strategy has to be employed in every game playing algorithm. With the minimax algorithm, the strategy assumes that the computer opponent is perfect in minimizing player's outcome. This is done irrespective of whether or not the opponent is perfect in doing so. 

This algorithm assumes that there are two players. One is named the Min and the other one is the Max. Both the players alternate in turms. The Max moves first. The aim of max is to maximize a heuristic score and that of min is to minimize the same. For every player, a minimax value is computed. This value is the best achievable payoff against his play. The move with the optimum minimax value is chosen by the player. 

Usually, the number of nodes to be explored by this algorithm is huge. In order to optimize it, pruning is used. 

Here, the 4x4 grid with a randomly placed 2/4 tile is the initial scenario. The computer player (MAX) makes the first move. This move is chosen by the minimax algorithm. After his play, the opponent randomly generates a 2/4 tile. The entire process continues until the game is over. 

While using the minimax algorithm, the MAX uses his move (UP, DOWN, RIGHT and LEFT) for finding the possible children nodes. Whereas the MIN will have the 2/4 tiles placed in all the empty cells for finding its children. Hence, for every max, there will be at most 4 children corresponding to each and every direction. And for MIN, the number of children will be 2*n where n is the number of empty cells in the grid. 


## 3. Heuristic Function Used

```sh
H=[[65536,32768,16384,8192],[512,1024,2048,4096],[256,128,64,32],[2,4,8,16]]
```


## 4. Code used
```sh
[1]BaseDisplayer_3.py and Displayer_3.py: Print the grid

[1]GameManager_3 :  Driver program that loads Computer AI and Player AI and begins the game where they compete with each other. Note that the time for making a move is kept as 2 seconds. 

[1]Grid_3 : Defines the Grid object. Incorporates useful operations for the grid like move, getAvailableCells, insertTile and clone

[1]BaseAI_3 : Base class for any AI component. All AI's inherit from this module and implement the getMove function which takes a Grid object as parameter and returns a move

[1]ComputerAI_3 : This inherits from BaseAI. The getMove() function returns a computer action, i.e. a tuple (x, y) indicating the place you want to place a tile

[2]PlayerAI_3 : Gets the next move for the player using Minimax Algorithm 

[1]Helper_3 : All utility functions created for this game are written here. This includes the eval function which evaluates the heuristic score for a given configuration
```
<b>[1]</b> = Source code by: ColumbiaEDX - Artificial Intelligence Course - Micro Master<br />
<b>[2]</b> = Guillermo Andres De Mendoza Corrales , memoodm@gmail.com, Colombia, Bogota D.C.<br />


## 5. Execute project

```sh
Run python GameManager_3.py
```