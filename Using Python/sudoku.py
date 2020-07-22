

def reduce(matrix):
    changed = True
    groups = getGroups()

    while changed:
        changed = reduceGroups(groups)


def main():
    sudoku_filename = input("enter the name of the text file : ")

    fh = open(sudoku_filename, 'r')
    for line in sud:
        cell_list = line.split(' ')

        for cell in cell_list:
