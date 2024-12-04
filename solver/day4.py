from typing import List, Tuple

def load_table(input_data: str) -> List[List[str]]:
    """Convert a string of characters into a table"""
    return list(filter(None, [list(line) for line in input_data.split("\n")]))

def get_xmas_count(table: str, coord: Tuple[int, int]):
    """Finds all the words starting at the given coordinate"""
    i, j = coord
    count = 0
    in_top_bound = i >= 3
    in_bottom_bound = i <= len(table) - 4
    in_left_bound = j >= 3
    in_right_bound = j <= len(table[i]) - 4
    # North word
    if in_top_bound:
        count += 1 if table[i][j] + table[i-1][j] + table[i-2][j] + table[i-3][j] == "XMAS" else 0
    # Northeast word
    if in_top_bound and in_right_bound:
        count += 1 if table[i][j] + table[i-1][j+1] + table[i-2][j+2] + table[i-3][j+3] == "XMAS" else 0
    # East word
    if in_right_bound:
        count += 1 if table[i][j] + table[i][j+1] + table[i][j+2] + table[i][j+3] == "XMAS" else 0
    # Southeast word
    if in_bottom_bound and in_right_bound:
        count += 1 if table[i][j] + table[i+1][j+1] + table[i+2][j+2] + table[i+3][j+3] == "XMAS" else 0
    # South word
    if in_bottom_bound:
        count += 1 if table[i][j] + table[i+1][j] + table[i+2][j] + table[i+3][j] == "XMAS" else 0
    # Southwest word
    if in_bottom_bound and in_left_bound:
        count += 1 if table[i][j] + table[i+1][j-1] + table[i+2][j-2] + table[i+3][j-3] == "XMAS" else 0
    # West word
    if in_left_bound:
        count += 1 if table[i][j] + table[i][j-1] + table[i][j-2] + table[i][j-3] == "XMAS" else 0
    # Northwest word
    if in_top_bound and in_left_bound:
        count += 1 if table[i][j] + table[i-1][j-1] + table[i-2][j-2] + table[i-3][j-3] == "XMAS" else 0
    return count
        

def part_a(input_data: str):
    """Find all occurances of XMAS in a table of characters (any direction)"""
    table = load_table(input_data)

    # First, find all the coordinates of Xs in the table
    x_coords = []

    for i in range(0, len(table)):
        for j in range(0, len(table[i])):
            if table[i][j] == "X":
                x_coords.append((i, j))

    # Build all the words starting at the "root" of the coordinates
    count = 0
    for coord in x_coords:
        count += get_xmas_count(table, coord)

    return count
