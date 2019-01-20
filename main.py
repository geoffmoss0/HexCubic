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
    print("size: " + str(size))

    grid = [[Hex(x, y) for x in range(size)] for y in range(size)]
    steps = []

    current = (size // 2, size // 2)
    print("current: " + str(current))
    for col in range(len(grid)):
        if col % 2 == 0:
            out = ""
            for row in range(len(grid)):
                out = out + str(grid[col][row]) + " "
            print(out)
        else:
            out = " "
            for row in range(len(grid)):
                out = out + str(grid[col][row]) + " "
            print(out)

    succ, steps = calculate(data, current, grid, steps)

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
        steps.append("*")
        return True, steps

    letter = letters[0]

    ur = grid[current[0]][current[1]].up_right()
    if ur is not None:
        ur = grid[ur[0]][ur[1]]
    r = grid[current[0]][current[1]].right()
    if r is not None:
        r = grid[r[0]][r[1]]
    dr = grid[current[0]][current[1]].down_right()
    if dr is not None:
        dr = grid[dr[0]][dr[1]]
    dl = grid[current[0]][current[1]].down_left()
    if dl is not None:
        dl = grid[dl[0]][dl[1]]
    l = grid[current[0]][current[1]].left()
    if l is not None:
        l = grid[l[0]][l[1]]
    ul = grid[current[0]][current[1]].up_left()
    if ul is not None:
        ul = grid[ul[0]][ul[1]]

    surroundings = (ur, r, dr, dl, l, ul)
    for sur in range(len(surroundings)):
        print(surroundings[sur])

    if letter == "a" or letter == "b" or letter == "m" or letter == "n" or letter == "y" or letter == "z":

        if len(steps) == 0:
            grid[current[0]][current[1]]

        succ = False
        exists = False

        # Check to make sure there is a space around it
        # Also, because these will all go up and to the right, the space down and to the left won't work in any case

        for i in range(6):
            if surroundings[i] is not None and i is not 4:
                exists = True

        print("exists: " + str(exists))
        if exists:
            for surr in surroundings:
                print("surr: " + str(surr))
                if surr is not None and surr.data == 0 and grid[surr.up_right()[0]][surr.up_right()[1]].data == 0: # Check that both the region we want and the one up and to the right are free
                    # TODO change the grid region

                    # TODO lots of if's here
                    # grid[surr.col][surr.row] =
                    if letter == "a":
                        surr.data = 1
                        grid[surr.up_right()[0]][surr.up_right()[1]].data = 1
                    if letter == "b":
                        surr.data = 1
                        grid[surr.up_right()[0]][surr.up_right()[1]].data = 2
                    if letter == "m":
                        surr.data = 2
                        grid[surr.up_right()[0]][surr.up_right()[1]].data = 1
                    if letter == "n":
                        surr.data = 2
                        grid[surr.up_right()[0]][surr.up_right()[1]].data = 2
                    if letter == "y":
                        surr.data = 3
                        grid[surr.up_right()[0]][surr.up_right()[1]].data = 1
                    if letter == "z":
                        surr.data = 3
                        grid[surr.up_right()[0]][surr.up_right()[1]].data = 2

                    for col in range(len(grid)):
                        if col % 2 == 0:
                            out = ""
                            for row in range(len(grid)):
                                out = out + str(grid[col][row]) + " "
                            print(out)
                        else:
                            out = " "
                            for row in range(len(grid)):
                                out = out + str(grid[col][row]) + " "
                            print(out)

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
