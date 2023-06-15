import problem

import random


def create_addition(min=0, max=9, display_vertical=False, **kwargs) -> problem.Problem:
    op1 = random.randint(min, max)
    op2 = random.randint(min, max)
    return problem.Problem(f"{op1}", f"{op2}", "+", is_vertical=display_vertical)


def create_subtraction(
    min=0, max=9, display_vertical=False, positive_only=False, **kwargs
) -> problem.Problem:
    op1 = random.randint(min, max)
    op2 = random.randint(min, max)

    if positive_only and op1 < op2:
        temp = op1
        op1 = op2
        op2 = temp

    return problem.Problem(f"{op1}", f"{op2}", "-", is_vertical=display_vertical)
