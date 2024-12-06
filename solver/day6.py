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

def part_a(input_data: str) -> int:
    """
    Given a matrix with obstacles represented by #
    Navigate out of the matrix from a starting position
    by only making 90-degree right turns
    """
    maze: List[List[str]] = load_maze(input_data)

    # Get the starting position
    for row in range(0, len(maze)):
        for col in range(0, len(maze[row])):
            if maze[row][col] == "^":
                curr_idx: Tuple[int, int] = (row, col)
                break

    # Start by moving N
    direction: str = "N"

    escaped: bool = False

    # Starting at a cell counts as visiting a unique cell
    unique_visited: int = 1

    while not escaped:
        # Get the next index and see if anything needs to be done
        next_index: Tuple[int, int] = get_next_index(curr_idx, direction)
        # Check if we've escaped the matrix :cool:
        if (next_index[0] < 0) or (len(maze[0]) <= next_index[0]) or \
            (next_index[1] < 0) or (len(maze) <= next_index[1]):
            escaped = True
            unique_visited += 1
            break
        # Check if we're about to hit an obstacle
        curr_cell: str = maze[curr_idx[0]][curr_idx[1]]
        next_cell: str = maze[next_index[0]][next_index[1]]
        if next_cell == "#":
            # Rotate and get the new next cell
            direction = get_next_direction(direction)
            next_index = get_next_index(curr_idx, direction)

        unique_visited += 1 if curr_cell == "." else 0

        # Visit the current cell
        maze[curr_idx[0]][curr_idx[1]] = "X"

        curr_idx = next_index

    return unique_visited



