# ProgrammingTechnologies
Tetris game
Blender engine game consists of three python controllers for the game logic provided:
*tetris.py - is responsible for creating new tetris shape during the game is attached to the creator plain axis;
*line.py - checks wherever row is full, deletes line, moves controlled shapes, increases the game score; 
*shapes.py - is attached to the all tetris shapes provided (ShapeI, ShapeL, ShapeJ, ShapeO, ShapeT, ShapeZ, ShapeS - blender groups),
controlls movements (left, right, descend), responsible for speed-up, rotation, saves fixed shapes.
