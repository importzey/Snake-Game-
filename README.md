# SNAKE GAME
#### **Video Demo:** [()]
## A simple snake game using Pygame library in Python
## Features:
* move snake 
* food spawning
* score counter
* increasing speed
* maximum score\

As in classic Snake game, when game starts, snake goes right. User can change direction of snake with keyboard. Food spawns in random position. When snake eats food, its body grows. Score continuously appear in left corner of screen. As score increasing, speed of snake also increase. When snake touches any border of screen or its own body, game is over and, ultimately, in terminal window user can see their maximum score of all playing games.
### Controls:
<kbd>W</kbd> Up\
<kbd>S</kbd> Down\
<kbd>A</kbd> Left\
<kbd>D</kbd> Right\

## Package
The main package consists of the following files:
* **project.py** implements all functions for the game 
* **requirements.py** includes all libraries used
* **test_project.py** includes unit tests for 3 function of project.py\

And **scores.txt** file is created when the program is runned, which contains scores of all game to get the maximum score.


## Installation
All used libraries in **requirements.txt** can be installed via this pip command:\
`pip install -r requirements.txt`
### Usage
If installation part is complete, it remains to run the program with command line:\
`python project.py`


