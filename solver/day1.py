def _load_columns(table: str):
    """Helper function to load columns from input."""
    col_a, col_b = [], []
    for line in table.strip().split("\n"):
        if not line.strip():
            continue
        a, b = map(int, line.split())
        col_a.append(a)
        col_b.append(b)
    return col_a, col_b

def part_a(input_data: str) -> int:
    col_a, col_b = _load_columns(input_data)
    col_a_sorted = sorted(col_a)
    col_b_sorted = sorted(col_b)
    return sum(abs(a - b) for a, b in zip(col_a_sorted, col_b_sorted))

def part_b(input_data: str) -> int:
    col_a, col_b = _load_columns(input_data)
    freq_map = {}
    total = 0
    for num in col_a:
        if num not in freq_map:
            freq_map[num] = col_b.count(num)
        total += freq_map[num] * num
    return total
