import problem

import random


def create_addition(min_operand=0, max_operand=9) -> problem.Problem:
    op1 = random.randint(min_operand, max_operand)
    op2 = random.randint(min_operand, max_operand)
    return problem.Problem(f"{op1}", f"{op2}", "+")
