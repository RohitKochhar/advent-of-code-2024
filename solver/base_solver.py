import json
import os
import importlib
from typing import Callable

INPUT_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")
TEST_DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tests")

class Solver:
    def __init__(self, day: int, part: str = 'a'):
        """Initialize Solver for a specific day and part."""
        self.day = day
        self.part = part.lower()
        if self.part not in ['a', 'b']:
            raise ValueError("Part must be 'a' or 'b'.")

        self.solution_func = self._load_solution()

        self._run_tests()
        self.result = self.solve()

        print(f"Solution for Day {self.day} Part {self.part.upper()}: {self.result}")

    def _load_solution(self) -> Callable[[str], any]:
        """Dynamically load the solution function for the specified day and part."""
        try:
            day_module = importlib.import_module(f"solver.day{self.day}")
            solution_func = getattr(day_module, f"part_{self.part}")
            return solution_func
        except (ModuleNotFoundError, AttributeError) as e:
            raise RuntimeError(f"Solution for Day {self.day} Part {self.part.upper()} not found.") from e

    def _run_tests(self):
        """Run test cases before solving the actual input."""
        test_input_path = os.path.join(TEST_DATA_DIR, "in", f"{self.day}.txt")
        test_output_path = os.path.join(TEST_DATA_DIR, "out.json")

        with open(test_input_path, 'r') as f:
            test_input = f.read()

        with open(test_output_path, 'r') as f:
            test_out = json.load(f)[f"{self.day}"][self.part]

        expected = self.solution_func(test_input)
        if str(expected) != str(test_out):
            raise AssertionError(f"Test failed for Day {self.day} Part {self.part.upper()}: Expected {test_out}, got {expected}")
        print("Test case passed!")

    def solve(self) -> any:
        """Solve the problem using the input file."""
        input_path = os.path.join(INPUT_DATA_DIR, f"{self.day}.txt")
        if not os.path.exists(input_path):
            raise FileNotFoundError(f"Input file for Day {self.day} Part {self.part.upper()} not found.")

        with open(input_path, 'r') as f:
            input_data = f.read()

        return self.solution_func(input_data)
