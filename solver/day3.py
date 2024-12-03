import re

def part_a(input: str):
    """
    Given a set of "corrupted instructions", i.e:
        xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
    Extract all mul(x,y) instructions, perform a multiplication operation, and sum
    """ 
    # Pull all the multiplication operations
    matches = re.findall(r'mul\([0-9]+,[0-9]+\)', input.strip())
    # Perform the multiplication for all matches
    total = 0
    for match in matches:
        # Extract first and second number
        nums = re.findall(r'\d+', match)
        total += int(nums[0]) * int(nums[1])
        
    return total
