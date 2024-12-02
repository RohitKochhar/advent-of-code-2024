import json
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
            raise RuntimeError(f"No solution has been implemented for day {day}{'a' if part_1 else 'b'}.")

        try:
            self.test(part_1)
            print("Test case success!")
        except AssertionError as e:
            raise RuntimeError(f"Test case failed! {str(e)}")

        try:
            result = self.solve()
        except FileNotFoundError:
            raise RuntimeError(f"Missing input file for {day}{'a' if part_1 else 'b'}")

        print(f"Expected solution for day {self.day}{'a' if part_1 else 'b'}: {result}")

    def test(self, part_1: bool):
        """Runs the solve function against the test case"""
        # Load input data
        with open(os.path.join(TEST_DATA_DIR, "in", f"{self.day}.txt")) as f:
            test_in = f.read()
        
        # Load output data
        with open(os.path.join(TEST_DATA_DIR, "out.json")) as f:
            test_out = json.load(f)[self.day]['a' if part_1 else 'b']

        result = self.solve_func(test_in)

        if str(result) != str(test_out):
            raise AssertionError(f"Expected {test_out}, instead got {result}!")
        
    def solve(self):
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

    # DAY 2
    def __load_rows(self, table: str):
        """Returns an MxN table into M lists"""
        return filter(None, table.splitlines())
    
    def day_2a_solution(self, input: str):
        """
        Given an input of MxN table, find the number
        of rows in which each number is:
        - Uniformly increasing/decreasing
        - Only changing from the last by [1, 3]
        """
        rows = self.__load_rows(input)

        valid_rows = []

        for row in rows:
            row = row.split(" ")
            row = list(map(int, row))
            # Ignore the rows that aren't either uniformly increasing/decreasing
            valid = (list(sorted(row)) == row or list(sorted(row, reverse=True)) == row)
            # Ensure each item is within the acceptable delta
            for i in range(0, len(row) - 1):
                valid = valid & (abs(int(row[i]) - int(row[i+1])) in [1,2,3])
            
            if valid:
                valid_rows.append(row)

        return len(valid_rows)