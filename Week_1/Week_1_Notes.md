# Week 1

## Overview

### Objectives

By the end of this week, you should be able to:

+ Understand and be able to design simple algorithms
+ Apply problem-solving techniques in algorithm design
+ Have installed PyCharm (A tool for Python programming) on your local computer

### Readings & Resources

+ All of the readings are in the module for the week

### Activities & Assignments

1. Introduce Yourself
2. Discussion - Design your own Algorithm
3. Maze Solving
4. Thought Problem: "How high can you count on five fingers?"
5. Install PyCharm

## Lesson

### Algorithms

+ __Algorithm__: A finite set of instructions that specify a sequence of operations to be carried out in order to solve a specific problem or class of problems
+ We judge an algorithm based on two criteria:
  + Correctness
  + Efficiency
+ An algorithm is *not* a program - a __program__ is the concrete expression of an algorithm in a particular programming language
+ Guessing game - guess number between 1 and 16, with each guess you will be told high or low, what is the most efficient way to find the right number?
  + __Linear Search__ - Start from number one and work your way up one number at a time. Will find the right answer, but it is inneficient and slow. In worst case it could take 16 guesses to find right answer.
  + __Binary Search__ - Guess the middle each time. Cuts the search space in half each time. At worst, it would take 5 guesses. This is the most efficient algorithm for this problem.

### Algorithm for a Maze

+ Let's try to design an algorithm for a maze, that you could always follow to solve any maze.

### Maze Solution #1 - The Random Approach

__Random Walk Algorithm__

1. Move forward until there is either a left or right turn or a dead end
2. If there is a left or right rurn, choose a random direction
3. If you are at a dead end turn around

__Problem__: Can take a very long time

### Maze Solution #2 - Follow the right wall

__Follow Right Wall Algorithm__

1. Go in a straight line until you encounter a junction or a dead-end
2. At a junction, always go to rightmost option from where you are currently facing
3. At a dead-end, turn around 180 degrees

__Problem__: May get stuck in some mazes, or Islands - correctness

### Maze Solution #3 - Tremauz's Algorithm

__Tremaux's Algorithm__

+ Charles Pierre Tremaux invented an algorithm for colving mazes:

1. As you walk down the maze, draw a line on the path
2. At a dead end, turn around and walk back the way you came
3. At a junction you've not seen before, take any new path
4. At junction you have been to before:
    1. If you are on a new path, turn back the way you came
    2. If you are on a path you've marked before, take a new path if you can
5. Never go down a path already marked with two lines
6. When your path reaches a junction, you choose an exit

## Homework

### Maze Solving Game

1. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=1&skin=0#3m64bp)

```javascript
moveForward();
moveForward();
```

2. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=2&skin=0#daume6)

```javascript
moveForward();
turnLeft();
moveForward();
turnRight();
moveForward();
```

3. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=3&skin=0#cmhyhx)

```javascript
while (notDone()) {
  moveForward();
}
```

4. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=4&skin=0#ci6g6f)

```javascript
while (notDone()) {
  moveForward();
  turnLeft();
  moveForward();
  turnRight();
}
```

5. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=5&skin=0#qaygga)

```javascript
moveForward();
moveForward();
turnLeft();
while (notDone()) {
  moveForward();
}
```

6. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=6&skin=0#86r6y7)

```javascript
while (notDone()) {
  if (isPathLeft()) {
    turnLeft();
  }
  moveForward();
}
```

7. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=7&skin=0#kmfef5)

```javascript
while (notDone()) {
  if (isPathForward()) {
    moveForward();
  }
  if (isPathRight()) {
    turnRight();
  }
}
```

8. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=8&skin=0#zvdz2d)

```javascript
while (notDone()) {
  if (isPathLeft()) {
    turnLeft();
  }
  if (isPathRight()) {
    turnRight();
  }
  moveForward();
}
```
9. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=9&skin=0#szydsf)

```javascript
while (notDone()) {
  if (isPathForward()) {
    moveForward();
  } else {
    if (isPathLeft()) {
      turnLeft();
    } else {
      turnRight();
    }
  }
}
```

10. Solved solution: [Link](https://blockly-games.appspot.com/maze?lang=en&level=10&skin=0#wba7pd)

```javascript
while (notDone()) {
  if (isPathForward()) {
    if (isPathRight()) {
      turnRight();
    } else {
      if (isPathLeft()) {
        turnLeft();
      }
    }
  } else {
    if (isPathLeft()) {
      turnLeft();
    } else {
      turnRight();
    }
  }
  moveForward();
}
```
