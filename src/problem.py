import re

VALID_CHARS_RE = re.compile(r'[0-9]+(.[0-9]+)?')

def validate_operand(operand: str) -> bool:
    if operand is None or len(operand) == 0:
        return False

    return VALID_CHARS_RE.match(operand) != None

class Problem:
    def __init__(self, operand_1: str, operand_2: str, operation='+'):
        self.op1 = operand_1
        self.op2 = operand_2
        self.operation = operation

    def __str__(self):
        return f'{self.op1} {self.operation} {self.op2}'