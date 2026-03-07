from typing import List, Tuple

def load_maze(input_data: str) -> List[List[str]]:
    """
    Convert string into table of strings
    """
    return [list(row) for row in input_data.split()]

def get_next_direction(direction: str) -> str:
    """
    Rotate the current direction by 90d right
    """
    match direction:
        case "N":
            return "E"
        case "E":
            return "S"
        case "S":
            return "W"
        case "W":
            return "N"
    
    # Default return needed for mypy checks
    return "_"
        
def get_next_index(curr: Tuple[int, int], dir: str) -> Tuple[int, int]:
    """
    Get the next index moving at the current direction
    """
    match dir:
        case "N":
            return (curr[0] - 1, curr[1])
        case "E":
            return (curr[0], curr[1] + 1)
        case "S":
            return (curr[0] + 1, curr[1])
        case "W":
            return (curr[0], curr[1] - 1)
        
    # Default return needed for mypy checks
    return (-1, -1)
        
def get_cell(maze: List[List[str]], idx: Tuple[int, int]) -> str:
    """Get the value of the maze at the given index"""
    return maze[idx[0]][idx[1]]

def get_starting_position(maze: List[List[str]]) -> Tuple[int, int]:
    """Gets the position of '^' in the maze"""
    # Get the starting position
    for row in range(0, len(maze)):
        for col in range(0, len(maze[row])):
            if maze[row][col] == "^":
                return (row, col)

def print_maze(maze: List[List[str]]) -> None:
    for row in maze:
        print("".join(row))

def get_visited_indices(maze: List[List[str]]):
    """Go through the maze and find the indices of all visited squares"""
    curr_idx = get_starting_position(maze)

    # Start by moving N
    direction: str = "N"

    escaped: bool = False

    # Starting at a cell counts as visiting a unique cell
    visited_indices = [curr_idx]

    while not escaped:
        # Get the next index and see if anything needs to be done
        next_index: Tuple[int, int] = get_next_index(curr_idx, direction)
        # Check if we've escaped the matrix :cool:
        if (next_index[0] < 0) or (len(maze[0]) <= next_index[0]) or \
            (next_index[1] < 0) or (len(maze) <= next_index[1]):
            escaped = True
            visited_indices.append(curr_idx)
            break
        # Check if we're about to hit an obstacle
        curr_cell: str = maze[curr_idx[0]][curr_idx[1]]
        next_cell: str = maze[next_index[0]][next_index[1]]
        while next_cell == "#":
            # Rotate and get the new next cell
            direction = get_next_direction(direction)
            next_index = get_next_index(curr_idx, direction)
            next_cell = get_cell(maze, next_index)

        if curr_cell == ".":
            visited_indices.append(curr_idx)

        # Visit the current cell
        maze[curr_idx[0]][curr_idx[1]] = "X"

        curr_idx = next_index

    return visited_indices

def check_for_loop(curr_idx: Tuple[int, int], maze: List[List[str]]) -> bool:
    """Checks if there is a loop in the given maze"""
    # Start by moving N
    direction: str = "N"

    escaped: bool = False
    visited = set()

    while True:
        # Get the next index and see if anything needs to be done
        next_index: Tuple[int, int] = get_next_index(curr_idx, direction)
        # Check if we've escaped the matrix :cool:
        if (next_index[0] < 0) or (len(maze[0]) <= next_index[0]) or \
            (next_index[1] < 0) or (len(maze) <= next_index[1]):
            return False

        # Check if we're about to hit an obstacle
        curr_cell: str = maze[curr_idx[0]][curr_idx[1]]
        next_cell: str = maze[next_index[0]][next_index[1]]
        while next_cell == "#":
            # Rotate and get the new next cell
            direction = get_next_direction(direction)
            next_index = get_next_index(curr_idx, direction)
            next_cell = get_cell(maze, next_index)

        if (curr_idx in visited) and (next_index in visited) and next_cell == direction:
            return True

        # Visit the current cell
        visited.add(curr_idx)
        maze[curr_idx[0]][curr_idx[1]] = direction

        curr_idx = next_index


def part_a(input_data: str) -> int:
    """
    Given a matrix with obstacles represented by #
    Navigate out of the matrix from a starting position
    by only making 90-degree right turns
    """
    maze: List[List[str]] = load_maze(input_data)

    return len(get_visited_indices(maze))

def part_b(input_data: str) -> int:
    """
    Find all the ways to edit the maze to create a loop
    """
    maze: List[List[str]] = load_maze(input_data)

    curr_idx = get_starting_position(maze)

    loops: int = 0
    
    # Change all visited blocks in the original map and check for loops
    # Get all visited block indices
    visited_indices = get_visited_indices(maze)

    for i, j in visited_indices:
        if i == 39 and j == 19:
            continue
        # Change the space to a blocker and check for loops
        edited_maze = load_maze(input_data)
        edited_maze[i][j] = "#"
        # print(i, j)
        if check_for_loop(curr_idx, edited_maze):
            loops += 1
            print_maze(edited_maze)

    return loops
                

