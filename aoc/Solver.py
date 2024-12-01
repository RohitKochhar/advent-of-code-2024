import os

INPUT_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")
TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")

class Solver:
    def __init__(self, day: int, part_1: bool=True):
        """Class constructor"""
        self.day = day
        # Get the function that represents the solution
        try:
            self.solve_func = self.__getattribute__(f"day_{day}{'a' if part_1 else 'b'}_solution")
        except AttributeError:
            print(f"No solution has been implemented for day {day}{'a' if part_1 else 'b'}.")
            raise RuntimeError

        try:
            self.test(part_1)
            print("Test case success!")
        except AssertionError as e:
            print(f"Test case failed! {str(e)}")
            raise RuntimeError

        try:
            result = self.solve(part_1)
        except FileNotFoundError:
            print(f"Missing input file for {day}{'a' if part_1 else 'b'}")
            raise RuntimeError

        print(f"Expected solution for day {self.day}{'a' if part_1 else 'b'}: {result}")

    def test(self, part_1: bool):
        """Runs the solve function against the test case"""
        # Load input data
        with open(os.path.join(TEST_DATA_DIR, "in", f"{self.day}{'a' if part_1 else 'b'}.txt")) as f:
            test_in = f.read()
        
        # Load output data
        with open(os.path.join(TEST_DATA_DIR, "out", f"{self.day}{'a' if part_1 else 'b'}.txt")) as f:
            test_out = f.read()

        test_out = test_out.strip()

        result = self.solve_func(test_in)

        if str(result) != str(test_out):
            raise AssertionError(f"Expected {test_out}, instead got {result}!")
        
    def solve(self, part_1: bool):
        """Runs the solve function against the input file"""
        # Load input data
        with open(os.path.join(INPUT_DATA_DIR, f"{self.day}.txt")) as f:
            input = f.read()

        return self.solve_func(input)
    
    # DAY 1:
    # Common functions
    def __load_columns(self, table: str):
        """Loads a Nx2 table into two lists"""
        # Get a list representing each column
        col_a = []
        col_b = []

        for line in table.split("\n"):
            rows = line.split(" ", maxsplit=1)
            try:
                col_a.append(int(rows[0].strip()))
                col_b.append(int(rows[1].strip()))
            except ValueError:
                # Catch the newline exception
                pass

        return col_a, col_b
        
    def day_1a_solution(self, input: str):
        """
        We are given an input of two columns, 
        sort the columns in ascending order and find the difference in each row
        Return the sum
        """
        col_a, col_b = self.__load_columns(input)

        # Sort the lists in ascending order
        col_a = list(sorted(col_a))
        col_b = list(sorted(col_b))

        assert len(col_a) == len(col_b)

        # Get sum of the differences
        total = 0
        for i in range(0, len(col_a)):
            total += abs(col_a[i] - col_b[i])

        return total

    def day_1b_solution(self, input: str):
        """
        Given an input of two columns
        Find the number of times the Nth element of the first column appears in the right column
        Sum the total
        """
        col_a, col_b = self.__load_columns(input)

        # Create a hashmap to store the frequency of each number
        freq_map = {}

        total = 0

        for num in col_a:
            # Don't count numbers that have already been counted
            if num in freq_map:
                pass

            # Find the number of times the number appears in column b
            freq_map[num] = col_b.count(num)

            total += freq_map[num] * num

        return total


