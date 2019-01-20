class Hex:

    def __init__(self, col, row):
        self.data = 0
        self.col = col
        self.row = row

    def set_data(self, data):
        self.data = data

    def up_left(self) -> (int, int):
        if self.row == 0:
            return None

        if self.col == 0 and (self.row & 2 == 0):
            return None

        if self.row % 2 == 0:
            return self.col - 1, self.row - 1
        else:
            return self.col, self.row - 1

    def up_right(self) -> (int, int):
        if self.row == 0:
            return None

        if self.row % 2 == 0:
            return self.col, self.row - 1
        else:
            return self.col + 1, self.row - 1

    def left(self) -> (int, int):
        if self.col == 0:
            return None

        return self.col - 1, self.row

    def right(self) -> (int, int):
        return self.col + 1, self.row

    def down_left(self) -> (int, int):
        if self.col == 0 and self.row % 2 == 0:
            return None

        if self.row % 2 == 0:
            return self.col - 1, self.row + 1
        else:
            return self.col, self.row + 1

    def down_right(self) -> (int, int):
        if self.row % 2 == 0:
            return self.col, self.row + 1
        else:
            return self.col + 1, self.row + 1
