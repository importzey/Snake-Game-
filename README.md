# SNAKE GAME
#### **Video Demo:** [()]
## A simple snake game using Pygame library in Python
### Project Overview
As in classic Snake game, when the game starts, snake goes right. User can change direction of snake with keyboard. Food spawns in random position. When snake eats food, its body grows. Score continuously appear in left corner of the screen. As score increasing, the speed of snake also increases. When snake touches any border of screen or its own body, game is over and, ultimately, in terminal window user can see their maximum score of all played games.
## Features:
* move snake 
* food spawning
* score counter
* increasing speed
* maximum score

### Controls:
<kbd>W</kbd> Up\
<kbd>S</kbd> Down\
<kbd>A</kbd> Left\
<kbd>D</kbd> Right

## Package and functioning
The main package consists of the following files:
* **project.py**
* **test_project.py**
* **requirements.txt**
* **scores.txt** file is created when the program is runned, which is for writing and reading all game scores to show the maximum score.

### 1.**project.py** implements all functions for the game 
* `main()`: contains variables like default values of direction,head position, blocks of body, score, speed, food spawn. It initializes pygame and show new window. In infinite loop, it quits when pressed x button and shows score on top left. With pygame, it draws the snake and food. Based on keyboard direction via keydirection() and previous direction it decides where to go (if previous direction is not opposite of keyboard direction, direction becomes keyboard direction). It add new head to body list. If food is eaten score value is increasing, and calls speed_update(). If food spawn is false, with random library , position of food is defined. Since body of snake can be growing or showing movement in case no food is eaten, it again draw snake. It calls is_game_running() to know whether break the loop or not. In the end of loop flip() update the screen and tick() control fps based on speed of snake. When loop is broken, it writes score to scores.txt and then reades all scores in that file to show max score with the help of cowsay library.
* `keydirection()` : when key is pressed, tells what direction to go
* `speed_update()` : in certain scores, increases the speed 
* `is_game_running()` : check if snake collide with screen borders or its body

### 2.**test_project.py** includes unit tests for 3 corresponding function of project.py
- `test_keydirection()` checks if direction is correct when key pressed 
- `test_speed_update()` checks if speed is correct in arbitrary score
- `test_is_game_running()` checks if collision detection works properly

### 3.**requirements.txt** includes all libraries used
- `pygame`
- `cowsay`


## Installation
All used libraries in **requirements.txt** can be installed via this pip command:\
`pip install -r requirements.txt`
### Usage
If installation part is complete, it remains to run the program with command line:\
`python project.py`\
Enjoy the game!


