from typing import List

def load_ordering_rules(input_data: str) -> List[List[int]]:
    """Gets all the ordering rules from the input data"""
    return [list(map(int, i.split("|"))) for i in list(filter(None,input_data.split("\n\n")[0].split("\n")))]

def load_page_lists(input_data: str) -> List[List[int]]:
    """Gets all the page lists from the input data"""
    return [list(map(int, i.split(","))) for i in list(filter(None,input_data.split("\n\n")[1].split("\n")))]

def part_a(input_data: str) -> int:
    """
    Given a list of ordering rules X|Y, and lists, 
    Find the lists in which X comes before Y
    From the valid lists, extract the middle element
    """
    ordering_rules = load_ordering_rules(input_data)
    page_lists = load_page_lists(input_data)

    total = 0

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
            total += page_list[int((len(page_list) - 1) / 2)]

    return total
