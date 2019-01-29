import turtle
from hex import Hex


def main():

    while True:
        data = input()
        graph(data.lower())


def graph(data: str):

    count = 0
    for letter in data:
        if not letter == " ":
            count += 1

    size = (4 * count) - 1

    grid = [[Hex(y, x) for x in range(size)] for y in range(size)]
    steps = []

    current = (size // 2, size // 2)

    succ, steps = calculate(data, current, grid, steps)
    print(steps)
    if succ:
        draw(grid, steps, size)
    else:
        print("Could not find solution")


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

    if letter == "a" or letter == "b" or letter == "m" or letter == "n" or letter == "y" or letter == "z":

        if len(steps) == 0:
            if letter == "a":

                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].up_right()[0]][grid[current[0]][current[1]].up_right()[1]]
                second.data = 1
                steps.append("d")
                steps.append(0)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "b":
                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].up_right()[0]][grid[current[0]][current[1]].up_right()[1]]
                second.data = 2
                steps.append("d")
                steps.append(0)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "m":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].up_right()[0]][grid[current[0]][current[1]].up_right()[1]]
                second.data = 1
                steps.append("u")
                steps.append(0)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "n":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].up_right()[0]][grid[current[0]][current[1]].up_right()[1]]
                second.data = 2
                steps.append("u")
                steps.append(0)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "y":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].up_right()[0]][grid[current[0]][current[1]].up_right()[1]]
                second.data = 1
                steps.append("n")
                steps.append(0)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "z":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].up_right()[0]][grid[current[0]][current[1]].up_right()[1]]
                second.data = 2
                steps.append("n")
                steps.append(0)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps

        else:
            succ = False
            exists = False

            # Check to make sure there is a space around it
            # Also, because these will all go up and to the right, the space down and to the left won't work in any case

            for i in range(6):
                if surroundings[i] is not None and i is not 3:
                    exists = True

            if exists:
                for k in range(len(surroundings)):
                    surr = surroundings[k]
                    if surr is not None and surr.data == 0 and grid[surr.up_right()[0]][surr.up_right()[1]].data == 0: # Check that both the region we want and the one up and to the right are free

                        # TODO lots of if's here
                        # grid[surr.col][surr.row] =
                        if letter == "a":
                            surr.data = 1
                            grid[surr.up_right()[0]][surr.up_right()[1]].data = 1
                            steps.append(k)
                            steps.append("d")
                            steps.append(0)
                            steps.append("d")
                            steps.append("#")
                        if letter == "b":
                            surr.data = 1
                            grid[surr.up_right()[0]][surr.up_right()[1]].data = 2
                            steps.append(k)
                            steps.append("d")
                            steps.append(0)
                            steps.append("u")
                            steps.append("#")
                        if letter == "m":
                            surr.data = 2
                            grid[surr.up_right()[0]][surr.up_right()[1]].data = 1
                            steps.append(k)
                            steps.append("u")
                            steps.append(0)
                            steps.append("d")
                            steps.append("#")
                        if letter == "n":
                            surr.data = 2
                            grid[surr.up_right()[0]][surr.up_right()[1]].data = 2
                            steps.append(k)
                            steps.append("u")
                            steps.append(0)
                            steps.append("u")
                            steps.append("#")
                        if letter == "y":
                            surr.data = 3
                            grid[surr.up_right()[0]][surr.up_right()[1]].data = 1
                            steps.append(k)
                            steps.append("n")
                            steps.append(0)
                            steps.append("d")
                            steps.append("#")
                        if letter == "z":
                            surr.data = 3
                            grid[surr.up_right()[0]][surr.up_right()[1]].data = 2
                            steps.append(k)
                            steps.append("n")
                            steps.append(0)
                            steps.append("u")
                            steps.append("#")

                        succ, new_steps = calculate(letters[1:], (surr.up_right()[0], surr.up_right()[1]), grid, steps)

                        # handle the output of calculate
                        if succ:
                            return True, new_steps
                        else:
                            # reset the parts of the grid we changed
                            surr.data = 0
                            grid[surr.up_right()[0]][surr.up_right()[1]].data = 0
                            for b in range(5):
                                steps.pop()
                # If succ is still false, then none of the surroundings were valid
                if not succ:
                    return False, steps
            else:
                return False, steps

    if letter == "c" or letter == "d" or letter == "o" or letter == "p" or letter == "0" or letter == "1":
        if len(steps) == 0:
            if letter == "c":

                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].right()[0]][grid[current[0]][current[1]].right()[1]]
                second.data = 1
                steps.append("d")
                steps.append(1)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "d":
                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].right()[0]][grid[current[0]][current[1]].right()[1]]
                second.data = 2
                steps.append("d")
                steps.append(1)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "o":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].right()[0]][grid[current[0]][current[1]].right()[1]]
                second.data = 1
                steps.append("u")
                steps.append(1)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "p":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].right()[0]][grid[current[0]][current[1]].right()[1]]
                second.data = 2
                steps.append("u")
                steps.append(1)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "0":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].right()[0]][grid[current[0]][current[1]].right()[1]]
                second.data = 1
                steps.append("n")
                steps.append(1)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "1":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].right()[0]][grid[current[0]][current[1]].right()[1]]
                second.data = 2
                steps.append("n")
                steps.append(1)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps

        else:
            succ = False
            exists = False

            # Check to make sure there is a space around it
            # Also, because these will all go up and to the right, the space down and to the left won't work in any case

            for i in range(6):
                if surroundings[i] is not None and i is not 4:
                    exists = True

            if exists:
                for k in range(len(surroundings)):
                    surr = surroundings[k]
                    if surr is not None and surr.data == 0 and grid[surr.right()[0]][surr.right()[1]].data == 0: # Check that both the region we want and the one up and to the right are free

                        # TODO lots of if's here
                        # grid[surr.col][surr.row] =
                        if letter == "c":
                            surr.data = 1
                            grid[surr.right()[0]][surr.right()[1]].data = 1
                            steps.append(k)
                            steps.append("d")
                            steps.append(1)
                            steps.append("d")
                            steps.append("#")
                        if letter == "d":
                            surr.data = 1
                            grid[surr.right()[0]][surr.right()[1]].data = 2
                            steps.append(k)
                            steps.append("d")
                            steps.append(1)
                            steps.append("u")
                            steps.append("#")
                        if letter == "o":
                            surr.data = 2
                            grid[surr.right()[0]][surr.right()[1]].data = 1
                            steps.append(k)
                            steps.append("u")
                            steps.append(1)
                            steps.append("d")
                            steps.append("#")
                        if letter == "p":
                            surr.data = 2
                            grid[surr.right()[0]][surr.right()[1]].data = 2
                            steps.append(k)
                            steps.append("u")
                            steps.append(1)
                            steps.append("u")
                            steps.append("#")
                        if letter == "0":
                            surr.data = 3
                            grid[surr.right()[0]][surr.right()[1]].data = 1
                            steps.append(k)
                            steps.append("n")
                            steps.append(1)
                            steps.append("d")
                            steps.append("#")
                        if letter == "1":
                            surr.data = 3
                            grid[surr.right()[0]][surr.right()[1]].data = 2
                            steps.append(k)
                            steps.append("n")
                            steps.append(1)
                            steps.append("u")
                            steps.append("#")

                        succ, new_steps = calculate(letters[1:], (surr.right()[0], surr.right()[1]), grid, steps)

                        # handle the output of calculate
                        if succ:
                            return True, new_steps
                        else:
                            # reset the parts of the grid we changed
                            surr.data = 0
                            grid[surr.right()[0]][surr.right()[1]].data = 0
                            for b in range(5):
                                steps.pop()
                # If succ is still false, then none of the surroundings were valid
                if not succ:
                    return False, steps
            else:
                return False, steps

    if letter == "e" or letter == "f" or letter == "q" or letter == "r" or letter == "2" or letter == "3":
        if len(steps) == 0:
            if letter == "e":

                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].down_right()[0]][grid[current[0]][current[1]].down_right()[1]]
                second.data = 1
                steps.append("d")
                steps.append(2)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "f":
                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].down_right()[0]][grid[current[0]][current[1]].down_right()[1]]
                second.data = 2
                steps.append("d")
                steps.append(2)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "q":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].down_right()[0]][grid[current[0]][current[1]].down_right()[1]]
                second.data = 1
                steps.append("u")
                steps.append(2)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "r":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].down_right()[0]][grid[current[0]][current[1]].down_right()[1]]
                second.data = 2
                steps.append("u")
                steps.append(2)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "2":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].down_right()[0]][grid[current[0]][current[1]].down_right()[1]]
                second.data = 1
                steps.append("n")
                steps.append(2)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "3":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].down_right()[0]][grid[current[0]][current[1]].down_right()[1]]
                second.data = 2
                steps.append("n")
                steps.append(2)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps

        else:
            succ = False
            exists = False

            # Check to make sure there is a space around it
            # Also, because these will all go up and to the right, the space down and to the left won't work in any case

            for i in range(6):
                if surroundings[i] is not None and i is not 5:
                    exists = True

            if exists:
                for k in range(len(surroundings)):
                    surr = surroundings[k]
                    if surr is not None and surr.data == 0 and grid[surr.down_right()[0]][surr.down_right()[1]].data == 0: # Check that both the region we want and the one up and to the right are free

                        # TODO lots of if's here
                        # grid[surr.col][surr.row] =
                        if letter == "e":
                            surr.data = 1
                            grid[surr.down_right()[0]][surr.down_right()[1]].data = 1
                            steps.append(k)
                            steps.append("d")
                            steps.append(2)
                            steps.append("d")
                            steps.append("#")
                        if letter == "f":
                            surr.data = 1
                            grid[surr.down_right()[0]][surr.down_right()[1]].data = 2
                            steps.append(k)
                            steps.append("d")
                            steps.append(2)
                            steps.append("u")
                            steps.append("#")
                        if letter == "q":
                            surr.data = 2
                            grid[surr.down_right()[0]][surr.down_right()[1]].data = 1
                            steps.append(k)
                            steps.append("u")
                            steps.append(2)
                            steps.append("d")
                            steps.append("#")
                        if letter == "r":
                            surr.data = 2
                            grid[surr.down_right()[0]][surr.down_right()[1]].data = 2
                            steps.append(k)
                            steps.append("u")
                            steps.append(2)
                            steps.append("u")
                            steps.append("#")
                        if letter == "2":
                            surr.data = 3
                            grid[surr.down_right()[0]][surr.down_right()[1]].data = 1
                            steps.append(k)
                            steps.append("n")
                            steps.append(2)
                            steps.append("d")
                            steps.append("#")
                        if letter == "3":
                            surr.data = 3
                            grid[surr.down_right()[0]][surr.down_right()[1]].data = 2
                            steps.append(k)
                            steps.append("n")
                            steps.append(2)
                            steps.append("u")
                            steps.append("#")

                        succ, new_steps = calculate(letters[1:], (surr.down_right()[0], surr.down_right()[1]), grid, steps)

                        # handle the output of calculate
                        if succ:
                            return True, new_steps
                        else:
                            # reset the parts of the grid we changed
                            surr.data = 0
                            grid[surr.down_right()[0]][surr.down_right()[1]].data = 0
                            for b in range(5):
                                steps.pop()
                # If succ is still false, then none of the surroundings were valid
                if not succ:
                    return False, steps
            else:
                return False, steps

    if letter == "g" or letter == "h" or letter == "s" or letter == "t" or letter == "4" or letter == "5":
        if len(steps) == 0:
            if letter == "g":

                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].down_left()[0]][grid[current[0]][current[1]].down_left()[1]]
                second.data = 1
                steps.append("d")
                steps.append(3)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "h":
                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].down_left()[0]][grid[current[0]][current[1]].down_left()[1]]
                second.data = 2
                steps.append("d")
                steps.append(3)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "s":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].down_left()[0]][grid[current[0]][current[1]].down_left()[1]]
                second.data = 1
                steps.append("u")
                steps.append(3)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "t":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].down_left()[0]][grid[current[0]][current[1]].down_left()[1]]
                second.data = 2
                steps.append("u")
                steps.append(3)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "4":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].down_left()[0]][grid[current[0]][current[1]].down_left()[1]]
                second.data = 1
                steps.append("n")
                steps.append(3)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "5":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].down_left()[0]][grid[current[0]][current[1]].down_left()[1]]
                second.data = 2
                steps.append("n")
                steps.append(3)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps

        else:
            succ = False
            exists = False

            # Check to make sure there is a space around it
            # Also, because these will all go up and to the right, the space down and to the left won't work in any case

            for i in range(6):
                if surroundings[i] is not None and i is not 6:
                    exists = True

            if exists:
                for k in range(len(surroundings)):
                    surr = surroundings[k]
                    if surr is not None and surr.data == 0 and grid[surr.down_left()[0]][surr.down_left()[1]].data == 0: # Check that both the region we want and the one up and to the right are free

                        # TODO lots of if's here
                        # grid[surr.col][surr.row] =
                        if letter == "g":
                            surr.data = 1
                            grid[surr.down_left()[0]][surr.down_left()[1]].data = 1
                            steps.append(k)
                            steps.append("d")
                            steps.append(3)
                            steps.append("d")
                            steps.append("#")
                        if letter == "h":
                            surr.data = 1
                            grid[surr.down_left()[0]][surr.down_left()[1]].data = 2
                            steps.append(k)
                            steps.append("d")
                            steps.append(3)
                            steps.append("u")
                            steps.append("#")
                        if letter == "s":
                            surr.data = 2
                            grid[surr.down_left()[0]][surr.down_left()[1]].data = 1
                            steps.append(k)
                            steps.append("u")
                            steps.append(3)
                            steps.append("d")
                            steps.append("#")
                        if letter == "t":
                            surr.data = 2
                            grid[surr.down_left()[0]][surr.down_left()[1]].data = 2
                            steps.append(k)
                            steps.append("u")
                            steps.append(3)
                            steps.append("u")
                            steps.append("#")
                        if letter == "4":
                            surr.data = 3
                            grid[surr.down_left()[0]][surr.down_left()[1]].data = 1
                            steps.append(k)
                            steps.append("n")
                            steps.append(3)
                            steps.append("d")
                            steps.append("#")
                        if letter == "5":
                            surr.data = 3
                            grid[surr.down_left()[0]][surr.down_left()[1]].data = 2
                            steps.append(k)
                            steps.append("n")
                            steps.append(3)
                            steps.append("u")
                            steps.append("#")

                        succ, new_steps = calculate(letters[1:], (surr.down_left()[0], surr.down_left()[1]), grid, steps)

                        # handle the output of calculate
                        if succ:
                            return True, new_steps
                        else:
                            # reset the parts of the grid we changed
                            surr.data = 0
                            grid[surr.down_left()[0]][surr.down_left()[1]].data = 0
                            for b in range(5):
                                steps.pop()
                # If succ is still false, then none of the surroundings were valid
                if not succ:
                    return False, steps
            else:
                return False, steps

    if letter == "i" or letter == "j" or letter == "u" or letter == "v" or letter == "6" or letter == "7":
        if len(steps) == 0:
            if letter == "i":

                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].left()[0]][grid[current[0]][current[1]].left()[1]]
                second.data = 1
                steps.append("d")
                steps.append(4)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "j":
                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].left()[0]][grid[current[0]][current[1]].left()[1]]
                second.data = 2
                steps.append("d")
                steps.append(4)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "u":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].left()[0]][grid[current[0]][current[1]].left()[1]]
                second.data = 1
                steps.append("u")
                steps.append(4)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "v":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].left()[0]][grid[current[0]][current[1]].left()[1]]
                second.data = 2
                steps.append("u")
                steps.append(4)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "6":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].left()[0]][grid[current[0]][current[1]].left()[1]]
                second.data = 1
                steps.append("n")
                steps.append(4)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "7":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].left()[0]][grid[current[0]][current[1]].left()[1]]
                second.data = 2
                steps.append("n")
                steps.append(4)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps

        else:
            succ = False
            exists = False

            # Check to make sure there is a space around it
            # Also, because these will all go up and to the right, the space down and to the left won't work in any case

            for i in range(6):
                if surroundings[i] is not None and i is not 1:
                    exists = True

            if exists:
                for k in range(len(surroundings)):
                    surr = surroundings[k]
                    if surr is not None and surr.data == 0 and grid[surr.left()[0]][surr.left()[1]].data == 0: # Check that both the region we want and the one up and to the right are free

                        # TODO lots of if's here
                        # grid[surr.col][surr.row] =
                        if letter == "i":
                            surr.data = 1
                            grid[surr.left()[0]][surr.left()[1]].data = 1
                            steps.append(k)
                            steps.append("d")
                            steps.append(4)
                            steps.append("d")
                            steps.append("#")
                        if letter == "j":
                            surr.data = 1
                            grid[surr.left()[0]][surr.left()[1]].data = 2
                            steps.append(k)
                            steps.append("d")
                            steps.append(4)
                            steps.append("u")
                            steps.append("#")
                        if letter == "u":
                            surr.data = 2
                            grid[surr.left()[0]][surr.left()[1]].data = 1
                            steps.append(k)
                            steps.append("u")
                            steps.append(4)
                            steps.append("d")
                            steps.append("#")
                        if letter == "v":
                            surr.data = 2
                            grid[surr.left()[0]][surr.left()[1]].data = 2
                            steps.append(k)
                            steps.append("u")
                            steps.append(4)
                            steps.append("u")
                            steps.append("#")
                        if letter == "6":
                            surr.data = 3
                            grid[surr.left()[0]][surr.left()[1]].data = 1
                            steps.append(k)
                            steps.append("n")
                            steps.append(4)
                            steps.append("d")
                            steps.append("#")
                        if letter == "7":
                            surr.data = 3
                            grid[surr.left()[0]][surr.left()[1]].data = 2
                            steps.append(k)
                            steps.append("n")
                            steps.append(4)
                            steps.append("u")
                            steps.append("#")

                        succ, new_steps = calculate(letters[1:], (surr.left()[0], surr.left()[1]), grid, steps)

                        # handle the output of calculate
                        if succ:
                            return True, new_steps
                        else:
                            # reset the parts of the grid we changed
                            surr.data = 0
                            grid[surr.left()[0]][surr.left()[1]].data = 0
                            for b in range(5):
                                steps.pop()
                # If succ is still false, then none of the surroundings were valid
                if not succ:
                    return False, steps
            else:
                return False, steps

    if letter == "k" or letter == "l" or letter == "w" or letter == "x" or letter == "8" or letter == "9":
        if len(steps) == 0:
            if letter == "k":

                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].up_left()[0]][grid[current[0]][current[1]].up_left()[1]]
                second.data = 1
                steps.append("d")
                steps.append(5)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "l":
                grid[current[0]][current[1]].data = 1
                second = grid[grid[current[0]][current[1]].up_left()[0]][grid[current[0]][current[1]].up_left()[1]]
                second.data = 2
                steps.append("d")
                steps.append(5)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "w":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].up_left()[0]][grid[current[0]][current[1]].up_left()[1]]
                second.data = 1
                steps.append("u")
                steps.append(5)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "x":
                grid[current[0]][current[1]].data = 2
                second = grid[grid[current[0]][current[1]].up_left()[0]][grid[current[0]][current[1]].up_left()[1]]
                second.data = 2
                steps.append("u")
                steps.append(5)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "8":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].up_left()[0]][grid[current[0]][current[1]].up_left()[1]]
                second.data = 1
                steps.append("n")
                steps.append(5)
                steps.append("d")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps
            if letter == "9":
                grid[current[0]][current[1]].data = 3
                second = grid[grid[current[0]][current[1]].up_left()[0]][grid[current[0]][current[1]].up_left()[1]]
                second.data = 2
                steps.append("n")
                steps.append(5)
                steps.append("u")
                steps.append("#")
                succ, new_steps = calculate(letters[1:], (second.row, second.col), grid, steps)
                if succ:
                    return True, new_steps
                else:
                    return False, steps

        else:
            succ = False
            exists = False

            # Check to make sure there is a space around it
            # Also, because these will all go up and to the right, the space down and to the left won't work in any case

            for i in range(6):
                if surroundings[i] is not None and i is not 2:
                    exists = True

            if exists:
                for k in range(len(surroundings)):
                    surr = surroundings[k]
                    if surr is not None and surr.data == 0 and grid[surr.up_left()[0]][surr.up_left()[1]].data == 0: # Check that both the region we want and the one up and to the right are free

                        # TODO lots of if's here
                        # grid[surr.col][surr.row] =
                        if letter == "k":
                            surr.data = 1
                            grid[surr.up_left()[0]][surr.up_left()[1]].data = 1
                            steps.append(k)
                            steps.append("d")
                            steps.append(5)
                            steps.append("d")
                            steps.append("#")
                        if letter == "l":
                            surr.data = 1
                            grid[surr.up_left()[0]][surr.up_left()[1]].data = 2
                            steps.append(k)
                            steps.append("d")
                            steps.append(5)
                            steps.append("u")
                            steps.append("#")
                        if letter == "w":
                            surr.data = 2
                            grid[surr.up_left()[0]][surr.up_left()[1]].data = 1
                            steps.append(k)
                            steps.append("u")
                            steps.append(5)
                            steps.append("d")
                            steps.append("#")
                        if letter == "x":
                            surr.data = 2
                            grid[surr.up_left()[0]][surr.up_left()[1]].data = 2
                            steps.append(k)
                            steps.append("u")
                            steps.append(5)
                            steps.append("u")
                            steps.append("#")
                        if letter == "8":
                            surr.data = 3
                            grid[surr.up_left()[0]][surr.up_left()[1]].data = 1
                            steps.append(k)
                            steps.append("n")
                            steps.append(5)
                            steps.append("d")
                            steps.append("#")
                        if letter == "9":
                            surr.data = 3
                            grid[surr.up_left()[0]][surr.up_left()[1]].data = 2
                            steps.append(k)
                            steps.append("n")
                            steps.append(5)
                            steps.append("u")
                            steps.append("#")

                        succ, new_steps = calculate(letters[1:], (surr.up_left()[0], surr.up_left()[1]), grid, steps)

                        # handle the output of calculate
                        if succ:
                            return True, new_steps
                        else:
                            # reset the parts of the grid we changed
                            surr.data = 0
                            grid[surr.up_left()[0]][surr.up_left()[1]].data = 0
                            for b in range(5):
                                steps.pop()
                # If succ is still false, then none of the surroundings were valid
                if not succ:
                    return False, steps
            else:
                return False, steps

    if letter == " ":
        steps.append(".")
        succ, new_steps = calculate(letters[1:], (current[0], current[1]), grid, steps)
        if succ:
            return True, new_steps
        else:
            steps.pop()
            return False, steps


def draw(grid: [], steps: [], size: int):
    center = size // 2
    left = center
    right = center
    up = center
    down = center
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            hex = grid[i][j]
            if hex.data > 0:
                if hex.row < up:
                    up = hex.row
                if hex.row > down:
                    down = hex.row
                if hex.col < left:
                    left = hex.col
                if hex.col > right:
                    right = hex.col
    horiz = down - up + 2
    vert = right - left + 2
    if horiz > vert:
        side_length = 700 // (horiz * 2)
    else:
        side_length = 700 // (vert * 2)

    turtle.up()
    turtle.speed(0)
    # turtle.tracer(False)
    turtle.hideturtle()

    # Adjust for being too high
    turtle.right(90)
    for i in range((center - up) - 1):
        turtle.forward(side_length)
    turtle.left(90)

    # Adjust for being too far right
    turtle.left(180)
    for i in range((right - center) - 1):
        turtle.forward(side_length)
    turtle.right(180)

    # low
    turtle.left(90)
    for i in range((down - center)):
        turtle.forward(side_length)
    turtle.right(90)

    # left
    for i in range((center - left)):
        turtle.forward(side_length)

    turtle.down()
    turtle.setheading(30)
    for place in range(len(steps)):

        if place == 0 or steps[place] == ".":
            # place += 1
            if steps[place] == "d":
                draw_down(side_length)
            elif steps[place] == "u":
                draw_up(side_length)
            elif steps[place] == "n":
                draw_empty(side_length)
            if steps[place + 1] == 0:
                draw_dot(0, side_length)
            if steps[place + 1] == 1:
                draw_dot(1, side_length)
            if steps[place + 1] == 2:
                draw_dot(2, side_length)
            if steps[place + 1] == 3:
                draw_dot(3, side_length)
            if steps[place + 1] == 4:
                draw_dot(4, side_length)
            if steps[place + 1] == 5:
                draw_dot(5, side_length)

        else:
            if steps[place] == "d":
                draw_down(side_length)
            elif steps[place] == "u":
                draw_up(side_length)
            elif steps[place] == "n":
                draw_empty(side_length)
            elif steps[place] == 0:
                move_to(0, side_length)
            elif steps[place] == 1:
                move_to(1, side_length)
            elif steps[place] == 2:
                move_to(2, side_length)
            elif steps[place] == 3:
                move_to(3, side_length)
            elif steps[place] == 4:
                move_to(4, side_length)
            elif steps[place] == 5:
                move_to(5, side_length)
            elif steps[place] == "#":
                if steps[place - 1] == "d" and steps[place + 1] == 0:
                    shade(1, side_length)
                if steps[place - 1] == "u" and steps[place + 1] == 0:
                    shade(4, side_length)
                if steps[place - 1] == "d" and steps[place + 1] == 1:
                    shade(2, side_length)
                if steps[place - 1] == "u" and steps[place + 1] == 1:
                    shade(4, side_length)
                if steps[place - 1] == "d" and steps[place + 1] == 2:
                    shade(2, side_length)
                if steps[place - 1] == "u" and steps[place + 1] == 2:
                    shade(5, side_length)
                if steps[place - 1] == "d" and steps[place + 1] == 3:
                    shade(3, side_length)
                if steps[place - 1] == "u" and steps[place + 1] == 3:
                    shade(5, side_length)
                if steps[place - 1] == "d" and steps[place + 1] == 4:
                    shade(3, side_length)
                if steps[place - 1] == "u" and steps[place + 1] == 4:
                    shade(6, side_length)
                if steps[place - 1] == "d" and steps[place + 1] == 5:
                    shade(1, side_length)
                if steps[place - 1] == "u" and steps[place + 1] == 5:
                    shade(6, side_length)

    turtle.mainloop()


def draw_down(length: int):
    """
    :param length: side length
    """
    for i in range(6):
        turtle.forward(length)
        turtle.right(60)
    turtle.right(60)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(180)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.right(180)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.right(120)


def draw_up(length: int):
    for i in range(6):
        turtle.forward(length)
        turtle.right(60)
    turtle.right(120)
    turtle.forward(length)
    turtle.left(120)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.left(180)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.right(180)
    turtle.forward(length)
    turtle.left(60)
    turtle.forward(length)
    turtle.right(120)
    turtle.forward(length)
    turtle.right(60)


def draw_empty(length: int):
    for i in range(6):
        turtle.forward(length)
        turtle.right(60)


def move_to(side: int, length: int):
    turtle.up()
    if side == 0:
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(60)
    if side == 1:
        for i in range(2):
            turtle.forward(length)
            turtle.right(60)
        turtle.left(120)
    if side == 2:
        for i in range(4):
            turtle.forward(length)
            turtle.right(60)
        turtle.right(120)
    if side == 3:
        turtle.right(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.left(180)
    if side == 4:
        turtle.left(120)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(180)
    if side == 5:
        turtle.left(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
    turtle.down()


def shade(region: int, length: int):
    # 1 is top, 2 is right, 3 is left, 4 is up right, 5 is bottom, 6 is up left
    turtle.begin_fill()
    if region == 1:
        turtle.right(60)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(180)
    if region == 2:
        for i in range(2):
            turtle.forward(length)
            turtle.right(60)
        turtle.right(60)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(60)
        turtle.forward(length)
        for j in range(2):
            turtle.left(60)
            turtle.forward(length)
        turtle.left(180)
    if region == 3:
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
    if region == 4:
        for i in range(2):
            turtle.forward(length)
            turtle.right(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.left(180)

    if region == 5:
        turtle.right(120)
        turtle.forward(length)
        turtle.left(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(60)
    if region == 6:
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length)
        turtle.right(120)
        turtle.forward(length)
        turtle.right(60)
    turtle.end_fill()


def draw_dot(region: int, length: int):
    if region == 0:
        turtle.forward(length)
        turtle.right(60)
        turtle.forward(length / 2)
        turtle.right(100)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.dot(length / 8)
        turtle.right(180)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.left(100)
        turtle.forward(length / 2)
        turtle.left(60)
        turtle.forward(length)
        turtle.right(180)
    if region == 1:
        for i in range(2):
            turtle.forward(length)
            turtle.right(60)
        turtle.forward(length / 2)
        turtle.right(60)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.dot(length / 8)
        turtle.right(180)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.left(60)
        for i in range(2):
            turtle.forward(length)
            turtle.left(60)
        turtle.left(120)
    if region == 2:
        for i in range(3):
            turtle.forward(length)
            turtle.right(60)
        turtle.forward(length / 2)
        turtle.right(100)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.dot(length / 8)
        turtle.right(180)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.left(100)
        turtle.forward(length / 2)
        turtle.left(60)
        for i in range(3):
            turtle.forward(length)
            turtle.left(60)
        turtle.left(120)
    if region == 3:
        for i in range(4):
            turtle.forward(length)
            turtle.right(60)
        turtle.forward(length / 2)
        turtle.right(60)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.dot(length / 8)
        turtle.right(180)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.left(60)
        for i in range(4):
            turtle.forward(length)
            turtle.left(60)
        turtle.left(120)
    if region == 4:
        turtle.right(120)
        turtle.forward(length / 2)
        turtle.left(60)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.dot(length / 8)
        turtle.right(180)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.right(60)
        turtle.forward(length / 2)
        turtle.right(60)
    if region == 5:
        turtle.forward(length / 2)
        turtle.right(60)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.dot(length / 8)
        turtle.right(180)
        turtle.up()
        turtle.forward(length / 4)
        turtle.down()
        turtle.left(60)
        turtle.forward(length / 2)
        turtle.right(180)


if __name__ == "__main__":
    main()
