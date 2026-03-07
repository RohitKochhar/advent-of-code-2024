from typing import List

def load_ordering_rules(input_data: str) -> List[List[int]]:
    """Gets all the ordering rules from the input data"""
    return [list(map(int, i.split("|"))) for i in list(filter(None,input_data.split("\n\n")[0].split("\n")))]

def load_page_lists(input_data: str) -> List[List[int]]:
    """Gets all the page lists from the input data"""
    return [list(map(int, i.split(","))) for i in list(filter(None,input_data.split("\n\n")[1].split("\n")))]

def get_page_lists_by_validity(page_lists: List[List[int]], ordering_rules: List[List[int]], valid: bool=True) -> List[List[int]]:
    """Gets all valid or invalid lists"""
    # Get all valid lists
    valid_lists = []
    for page_list in page_lists:
        is_valid = True
        for ordering_rule in ordering_rules:
            # Get the indices of the low and high bound
            low = ordering_rule[0]
            high = ordering_rule[1]
            if low in page_list and high in page_list:
                if not (page_list.index(low) < page_list.index(high)):
                    is_valid = False
                    break
        if is_valid:
            valid_lists.append(page_list)

    if valid:
        return valid_lists

    return [list for list in page_lists if list not in valid_lists]

def part_a(input_data: str) -> int:
    """
    Given a list of ordering rules X|Y, and lists, 
    Find the lists in which X comes before Y
    From the valid lists, extract the middle element
    """
    valid_lists = get_page_lists_by_validity(load_page_lists(input_data), load_ordering_rules(input_data))
    return sum([page_list[int((len(page_list) - 1) / 2)] for page_list in valid_lists])

def part_b(input_data: str) -> int:
    """
    Sort the invalid lists in a way that meets the relevant ordering rules
    """
    ordering_rules = load_ordering_rules(input_data)
    # Get all invalid lists
    invalid_lists = get_page_lists_by_validity(load_page_lists(input_data), ordering_rules, valid=False)

    total = 0

    # Get all the ordering rules that are relevant for each list
    for li in invalid_lists:
        rules = [rule for rule in ordering_rules if (rule[0] in li) and (rule[1] in li)]

        ordering_nums = list(set([inner for outer in rules for inner in outer]))

        ordered_rules: List[int] = []

        for num in ordering_nums:
            # Get all the numbers this one must precede
            followers = set([i[1] for i in ordering_rules if i[0] == num])
            # Get all the numbers this one must follow
            preceders = set([i[0] for i in ordering_rules if i[1] == num])

            # Insert the number at a spot where all followers would be after and preceders before
            for i in range(0, len(ordered_rules)+1):
                if (set(ordered_rules[:i]) <= preceders) and (set(ordered_rules[i:]) <= followers):
                    ordered_rules.insert(i, num)
                    break

        ordered_page_list = sorted(
            li,
            key=lambda x: {item: index for index, item in enumerate(ordered_rules)}.get(x, float('inf'))
        )

        total += ordered_page_list[int((len(ordered_page_list) - 1) / 2)]

    return total
