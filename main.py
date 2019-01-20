import turtle
from hex import Hex


def main():
    turtle.forward(375)
    turtle.mainloop()

    while True:
        data = input()
        result = graph(data)
        if result is not None:
            draw()


def graph(data: str) -> ([], []):  # Hey look, the return type is my reaction to the return type

    count = 0
    for letter in data:
        if not letter == " ":
            count += 1

    size = (2 * count) - 1

    grid = [[Hex(x, y) for x in range(size)] for y in range(size)]
    steps = []

    current = (count - 1, count - 1)

    succ, grid, steps = calculate(data, current, grid, steps)

    draw(grid)



def calculate(letters :str, current :(), grid: [], steps :[]) -> (bool, [], []):
    """

    :param letters: the letters left to calculate
    :param current: the current position on the grid
    :param grid: the arrays representing the hex grid
    :param steps: the current path that the drawing will take
    :return: the success of the calculation, [] grid and [] steps
    """

    if letters == "":
        steps.add("*")
        return True, grid, steps

    letter = letters[0]


    if letter == "a" or letter == "b" or letter == "m" or letter == "n" or letter == "y" or letter == "z":
        surroundings = (grid[current[0]][current[1]].up_right(), grid[current[0]][current[1]].right(),
                        grid[current[0]][current[1]].down_right(), grid[current[0]][current[1]].down_left(),
                        grid[current[0]][current[1]].left(), grid[current[0]][current[1]].up_left())

        exists = False

        # Check to make sure there is a space around 
        for surr in surroundings:
            if surr is not None:
                exists = True

        if exists:
            for surr in surroundings:
                if surr.data == 0:
                    # TODO change the grid region

                    # TODO lots of if's here
                    # grid[surr.col][surr.row] =
                    succ, grid, steps = calculate(letters[1:], (surr.col, surr.row), grid, steps) # TODO actually add the step to the array once I figure out the format. It'll stay blank for now
        else:
            # TODO reset the grid region I changed
            return False, grid, steps

    if letter == "c" or letter == "d" or letter == "o" or letter == "p" or letter == "0" or letter == "1":
        surroundings = (grid[current[0]][current[1]].up_right(), grid[current[0]][current[1]].right(),
                        grid[current[0]][current[1]].down_right(), grid[current[0]][current[1]].down_left(),
                        grid[current[0]][current[1]].left(), grid[current[0]][current[1]].up_left())

    if letter == "e" or letter == "f" or letter == "q" or letter == "r" or letter == "2" or letter == "3":
        surroundings = (grid[current[0]][current[1]].up_right(), grid[current[0]][current[1]].right(),
                        grid[current[0]][current[1]].down_right(), grid[current[0]][current[1]].down_left(),
                        grid[current[0]][current[1]].left(), grid[current[0]][current[1]].up_left())

    if letter == "g" or letter == "h" or letter == "s" or letter == "t" or letter == "4" or letter == "5":
        surroundings = (grid[current[0]][current[1]].up_right(), grid[current[0]][current[1]].right(),
                        grid[current[0]][current[1]].down_right(), grid[current[0]][current[1]].down_left(),
                        grid[current[0]][current[1]].left(), grid[current[0]][current[1]].up_left())

    if letter == "i" or letter == "j" or letter == "u" or letter == "v" or letter == "6" or letter == "7":
        surroundings = (grid[current[0]][current[1]].up_right(), grid[current[0]][current[1]].right(),
                        grid[current[0]][current[1]].down_right(), grid[current[0]][current[1]].down_left(),
                        grid[current[0]][current[1]].left(), grid[current[0]][current[1]].up_left())

    if letter == "k" or letter == "l" or letter == "w" or letter == "x" or letter == "8" or letter == "9":
        surroundings = (grid[current[0]][current[1]].up_right(), grid[current[0]][current[1]].right(),
                        grid[current[0]][current[1]].down_right(), grid[current[0]][current[1]].down_left(),
                        grid[current[0]][current[1]].left(), grid[current[0]][current[1]].up_left())


def draw(grid :[]):
    pass


if __name__ == "__main__":
    main()
