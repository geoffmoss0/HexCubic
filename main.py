import turtle
from hex import Hex


def main():

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

    size = (4 * count) - 1
    print(size)

    grid = [[Hex(x, y) for x in range(size)] for y in range(size)]
    steps = []

    current = (count - 1, count - 1)
    print(grid)

    succ, grid, steps = calculate(data, current, grid, steps)

    draw(grid)


def calculate(letters: str, current: (), grid: [], steps: []) -> (bool, []):
    """

    :param letters: the letters left to calculate
    :param current: the current position on the grid
    :param grid: the arrays representing the hex grid
    :param steps: the current path that the drawing will take
    :return: the success of the calculation, [] grid and [] steps
    """

    if letters == "":
        steps.add("*")
        return True, steps

    letter = letters[0]

    ur = grid[current[0]][current[1]].up_right()
    if ur is not None:
        up_right = grid[ur[0]][ur[1]]
    r = grid[current[0]][current[1]].right()
    if r is not None:
        right = grid[r[0]][r[1]]
    dr = grid[current[0]][current[1]].down_right()
    if dr is not None:
        down_right = grid[dr[0]][dr[1]]
    down_left = grid[grid[current[0]][current[1]].down_left()[0]][grid[current[0]][current[1]].down_left()[1]]
    left = grid[grid[current[0]][current[1]].left()[0]][grid[current[0]][current[1]].left()[1]]
    up_left = grid[grid[current[0]][current[1]].up_left()[0]][grid[current[0]][current[1]].up_left()[1]]

    surroundings = (up_right, right, down_right, down_left, left, up_left)

    if letter == "a" or letter == "b" or letter == "m" or letter == "n" or letter == "y" or letter == "z":

        succ = False
        exists = False

        # Check to make sure there is a space around it
        # Also, because these will all go up and to the right, the space down and to the left won't work in any case

        for i in range(6):
            if surroundings[i] is not None and i is not 4:
                exists = True

        if exists:
            for surr in surroundings:
                if surr is not None and surr.data == 0 and grid[surr.up_right().col][surr.up_right().row].data == 0: # Check that both the region we want and the one up and to the right are free
                    # TODO change the grid region

                    # TODO lots of if's here
                    # grid[surr.col][surr.row] =
                    if letter == "a":
                        surr.data = 1
                        grid[surr.up_right().col][surr.up_right().row].data = 1
                    if letter == "b":
                        surr.data = 1
                        grid[surr.up_right().col][surr.up_right().row].data = 2
                    if letter == "m":
                        surr.data = 2
                        grid[surr.up_right().col][surr.up_right().row].data = 1
                    if letter == "n":
                        surr.data = 2
                        grid[surr.up_right().col][surr.up_right().row].data = 2
                    if letter == "y":
                        surr.data = 3
                        grid[surr.up_right().col][surr.up_right().row].data = 1
                    if letter == "z":
                        surr.data = 3
                        grid[surr.up_right().col][surr.up_right().row].data = 2

                    succ, new_steps = calculate(letters[1:], (surr.col, surr.row), grid, steps)

                    # handle the output of calculate
                    if succ:
                        # TODO add to new_steps

                        return True, new_steps
                    else:
                        # reset the parts of the grid we changed
                        surr.data = 0
                        grid[surr.up_right().col][surr.up_right().row].data = 0
            # If succ is still false, then none of the surroundings were valid
            if not succ:
                return False, steps
        else:
            return False, steps

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


def draw(grid: []):
    pass


if __name__ == "__main__":
    main()
