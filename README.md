This is a program that can graphically display the Hexcubic (TM) cypher made by Matthew Bonney (https://github.com/mjb4611).

See https://github.com/mjb4611/Hexcubic to learn more about the Hecubic cypher.


The program takes a string of any length (strings over 30 characters may take a long to backtrack or may not work) and attempts to display it in the Hexcubic cypher. 
It uses a hex grid with offset coordinates and an array of instructions for drawing to keep track of the current image. 
The hex grid is initialized large enough to contain any possible configuration, so that a drawing that extended in any one of the six directions will not throw an error


The steps array of instructions for drawing the picture uses the following key:

	"d" - downward hex
 
	"u" - upward hex

	"n" - empty hex

	1-6 - side of the hexagon to move to next, starting with the top right and moving around clockwise

	"#" - signifies that the region touching the next hex drawn should be shaded

	"." - signifies the end of a word and that a dot should be drawn on the side that the next hex will be drawn on

	"*" - end of instructions


The program uses a recursive backtracking algorithm to test all viable arrangements of the characters and returns false if no valid configurations exist.
The backtracking algorithm constructs a tuple of the surrounding hexes, and ensures that at least one is not null before continuing.
If the only existing hexagon is in the opposite direction of where the hex after that needs to be placed, it will return false.
If a false is received at any point, the hexagons that were changed will be reset and the appropriate amount of characters will be removed from the steps array. 

The hex grid is a 2D array of Hex objects that uses offset coordinates. Adjacent hexagons are calculated using the methods in the Hex class.
The Hex class is a wrapper class for the coordinates of a point and can calculate the coordinates of all six adjacent hexagaons, or returns null if it does not exist

The drawing is created using turtle based on the instructions in the steps array. It draws the hexagons in the order they appear in the word
Turtle is used because when hidden it creates the effect of actually being drawn, instead of simply being rendered. 
The size of the drawing is determined based on the distance from the center point of the graph and side length of the hexagons is based on the 700 x 700 window
The distance the drawing strays from the center in the four cardinal directions is calculated and accounted for by moving the turtle opposite of the direction the drawing strays from the center


What I learned:
I learned how to implement and use a hex grid using offset coordinates
I learned how to use backtracking with recursion, implemented all the functionality independently. 
My first year CS class mentioned the topic of backtracking but we were never tested on it and never implemented it, so in place of a lab I created this program to learn the topic
