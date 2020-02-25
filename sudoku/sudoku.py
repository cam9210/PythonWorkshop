import copy

class cell:
    cell_num = None

    def __init__(self):
        self.cell_num = -1

    def set_num(self, input):
        self.cell_num = input
        
    def rem_num(self):
        self.cell_num = -1

    def get_num(self):
        return self.cell_num

class grid:
    cell_array = None
    def __init__(self):
        self.cell_array = list()
        for i in range(3):
            self.cell_array.append(list())
            for j in range(3):
                self.cell_array[i].append(cell())

    def get_grid(self):
        

class board:
    grid_array = None
    def __init__(self):
        self.grid_array = list()
        for i in range(3):
            self.grid_array.append(list())
            for j in range(3):
                self.grid_array[i].append(grid())

    def set_num(self, row, col, num):
        row_div = row // 3
        col_div = col // 3
        cell_row = row - (row_div * 3)
        cell_col = col - (col_div * 3)
        self.grid_array[row_div][col_div].cell_array[cell_row][cell_col].set_num(num)

    def rem_num(self, row, col, num):
        row_div = row // 3
        col_div = col // 3
        cell_row = row - (row_div * 3)
        cell_col = col - (col_div * 3)
        self.grid_array[row_div][col_div].cell_array[cell_row][cell_col].rem_num()

    def get_num(self, row, col, num):
        row_div = row // 3
        col_div = col // 3
        cell_row = row - (row_div * 3)
        cell_col = col - (col_div * 3)
        return self.grid_array[row_div][col_div].cell_array[cell_row][cell_col].get_num()


myboard = board()

myboard.set_num(0, 2, 7)
print(myboard.get_num(0, 2, 7))

print("test")