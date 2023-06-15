import unittest

import problem_factory


class ProblemFactoryTest(unittest.TestCase):
    def test_create_addition(self):
        # Since the factory creates random operands create a large amount and verify none violate the bounds
        min_value = 1
        max_value = 5

        sample_problems = [
            problem_factory.create_addition(min_value, max_value) for _ in range(500)
        ]

        self.assertTrue(
            all([min_value <= int(prob.op1) <= max_value for prob in sample_problems])
        )
        self.assertTrue(
            all([min_value <= int(prob.op2) <= max_value for prob in sample_problems])
        )
        self.assertTrue(all([prob.operation == "+" for prob in sample_problems]))
