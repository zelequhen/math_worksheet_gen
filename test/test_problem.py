import problem

import unittest

class TestProblem(unittest.TestCase):

    def test_should_validate_operands(self):
        VALID_OPERANDS = [
            '1',
            '10',
            '4.2',
            '93.123'
        ]

        for good_operand in VALID_OPERANDS:
            self.assertTrue(problem.validate_operand(good_operand))

    def test_should_detect_invalid_operands(self):
        INVALID_OPERANDS = [
            None,
            '',
            'abc',
            '.1'
        ]
        for invalid_operand in INVALID_OPERANDS:
            self.assertFalse(problem.validate_operand(invalid_operand))