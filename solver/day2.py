def load_rows(table: str):
    """Returns an MxN table into M lists"""
    return list(filter(None, table.splitlines()))

def check_level_validity(row):
    if isinstance(row, str):
        row = row.split(" ")

    # Assume all are true to start
    asc = True
    des = True
    delta = True

    for i in range(0, len(row) - 1):
        a = int(row[i])
        b = int(row[i+1])
        # Check if the ascending assumption is still true
        asc = asc & (a < b)
        des = des & (a > b)
        delta = delta & (abs(a - b) in [1,2,3])

    return delta and (asc or des)

def recurse_list(levels: list, idx: int):
    """
    Recurses the list to remove each element until a valid solution is found
    """
    if check_level_validity(levels):
        return True
    
    modified_level = levels[:idx] + levels[idx+1:]

    if check_level_validity(modified_level):
        return True
    elif idx == len(levels) - 1:
        return False
    else:
        return recurse_list(levels, idx + 1)

def part_a(input: str):
    """
    Given an input of MxN table, find the number
    of rows in which each number is:
    - Uniformly increasing/decreasing
    - Only changing from the last by [1, 3]
    """
    return sum(list(map(check_level_validity, load_rows(input))))

def part_b(input: str):
    """
    Same as step 1, but we can now remove a single element to make the list safe
    """
    valid = 0
    for row in load_rows(input):
        valid += 1 if recurse_list(row.split(" "), 0) else 0

    return valid
