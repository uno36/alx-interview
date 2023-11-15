#!/usr/bin/python3
""" module contains algorithm that rotates a 2d array 90 degrees
    clockwise
    APPROACH:
        -> normalize the 2d array to a 1d array by abstracting each
           row_index - column-index pair into a single index; from
           this single index row_index and col_index can be computed
           easily since the matrix width == height
            -> actual row_index = floor(normalized_index / width)
               eg: if n_i = 20 and width = 5 actual row n_i element
               belong to = 4 (ie 5th row 0 indexed)
            -> actual col_index = normalized_index % width
               eg: if n_i = 20 and width = 5 actual column n_i element
               belong to = 0 (ie 1st column 0 indexed)
        -> get all possible indeces == width * height of matrix
        -> build a map of all normalized indeces to:
            -> its next position
            -> its value
        -> loop over map and place each value in its new position
    FUNCTIONS:
    rotate_2d_matrix -> main function; gathers every function together
    build_map -> builds a map of all normalized indeces to:
        -> its next position
        -> its value
        map_structure = {
            index: {
                'new_index': computed_new_index,
                'value': value at current index
            }
        }
    get_new_index -> computes the new index of an index after rotation
        parameters:
        index -> index to compute new index for
        width -> width of the matrix
        LOGIC:
            -> get its current col_index
            -> get its current row_index
            -> next_col_index = width - 1 - current_row_index
               e.g:
               4 starts at col_index 0, row_index 1
               and its new col_index is 1
               which is == 3(width) - 1(constant) - 1(row_index)
                start [                 end [
                        [1, 2, 3],              [7, 4, 1],
                        [4, 5, 6],              [8, 5, 2],
                        [7, 8, 9]               [9, 6, 3],
                ]                       ]
            -> next_row_index = current_col_index
               e.g:
               6 starts at row_index 1, col_index 2
               and its new row_index is 2
               which is == next_row_index = current_col_index
                start [                 end [
                        [1, 2, 3],              [7, 4, 1],
                        [4, 5, 6],              [8, 5, 2],
                        [7, 8, 9]               [9, 6, 3],
                ]                       ]
            -> compute normalized new index and return it
    get_value -> denormalize normalized index and return the
                 value retrived from the actual matrix
    compute_row_and_index -> returns actual row and index from a
                             normalized index
"""


def rotate_2d_matrix(m):
    """main function: rotates a 2d array 90 deg"""
    width = len(m[0])
    height = len(m)
    total_items = width * height
    map_ = build_map(m, total_items, width)
    # print(map_)
    for index in map_:
        prev_index = index
        value = map_[prev_index]["value"]
        new_index = map_[prev_index]["new_index"]
        row, index = compute_row_and_index(new_index, width)
        m[row][index] = value


def build_map(m, length, width):
    """returns a map of prev_index and their
    next positions"""
    dct = {
        i: {
            "new_index": get_new_index(i, width),
            "value": get_value(m, i, width)
        }
        for i in range(length)
    }
    return dct


def get_new_index(i, width):
    """computes new position"""
    current_index = i % width
    current_row = int(i / width)
    next_index = width - 1 - current_row
    next_row = current_index
    next_position = next_row * width + next_index
    return next_position


def get_value(m, i, width):
    """gets the value of a 2d array by denormalizing
    its flattened index"""
    current_index = i % width
    current_row = int(i / width)
    return m[current_row][current_index]


def compute_row_and_index(flat_index, width):
    """returns denormalized row and index from a
    flattened 2d array index"""
    row = int(flat_index / width)
    index = flat_index % width
    return row, index


def printx(lst):
    """custom print function to print 2d array"""
    print("[")
    for itm in lst:
        print("  ", str(itm) + ",")
    print("]")


def build_matrix(n):
    """ builds n * n 2d matrix """
    parent = []
    y = 1
    for i in range(n):
        child = []
        for x in range(y, n * n + 1):
            child.append(x)
            if x % n == 0 and x != 1:
                y = x + 1
                break
        parent.append(child)
    return parent


if __name__ == "__main__":
    matrix = build_matrix(3)

    rotate_2d_matrix(matrix)
    printx(matrix)
    print()
    matrix = build_matrix(5)

    rotate_2d_matrix(matrix)
    printx(matrix)
