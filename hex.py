class Hex:

    def __init__(self, row, col):
        self.data = 0
        self.row = row
        self.col = col

    def set_data(self, data):
        self.data = data

    def up_left(self) -> (int, int):
        if self.row == 0:
            return None

        if self.col == 0 and (self.row & 2 == 0):
            return None

        if self.row % 2 == 0:
            return self.row - 1, self.col - 1
        else:
            return self.row - 1, self.col

    def up_right(self) -> (int, int):
        if self.row == 0:
            return None

        if self.row % 2 == 0:
            return self.row - 1, self.col
        else:
            return self.row - 1, self.col + 1

    def left(self) -> (int, int):
        if self.col == 0:
            return None

        return self.row, self.col - 1

    def right(self) -> (int, int):
        return self.row, self.col + 1

    def down_left(self) -> (int, int):
        if self.col == 0 and self.row % 2 == 0:
            return None

        if self.row % 2 == 0:
            return self.row + 1, self.col - 1
        else:
            return self.row + 1, self.col

    def down_right(self) -> (int, int):
        if self.row % 2 == 0:
            return self.row + 1, self.col
        else:
            return self.row + 1, self.col + 1

    def coords(self):
        return "(" + str(self.row) + ", " + str(self.col) + ")"

    def __str__(self):
        return str(self.data)
