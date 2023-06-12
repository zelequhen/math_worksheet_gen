import problem

import unittest


class TestProblem(unittest.TestCase):
    def test_should_validate_operands(self):
        VALID_OPERANDS = ["1", "10", "4.2", "93.123"]

        for good_operand in VALID_OPERANDS:
            self.assertTrue(problem.validate_operand(good_operand))

    def test_should_detect_invalid_operands(self):
        INVALID_OPERANDS = [None, "", "abc", ".1"]
        for invalid_operand in INVALID_OPERANDS:
            self.assertFalse(problem.validate_operand(invalid_operand))

    def test_should_detect_valid_operations(self):
        VALID_OPERATIONS = ["+"]
        for operation in VALID_OPERATIONS:
            self.assertTrue(problem.validate_operation(operation))

    def test_should_detect_invalid_operations(self):
        INVALID_OPERATIONS = [None, "", "a"]
        for operation in INVALID_OPERATIONS:
            self.assertFalse(problem.validate_operation(operation))

    def test_should_create_a_problem(self):
        sample_problem = problem.Problem("1", "2", "+")

        self.assertIsNotNone(sample_problem)

    def test_should_not_create_a_problem(self):
        self.assertRaises(ValueError, lambda: problem.Problem("1", "five", "add"))
