import re

VALID_OPERANDS_RE = re.compile(r"[0-9]+(.[0-9]+)?")
VALID_OPERATIONS_RE = re.compile(r"[+]")


def validate_operand(operand: str) -> bool:
    if operand is None or len(operand) == 0:
        return False

    return VALID_OPERANDS_RE.match(operand) is not None


def validate_operation(operation: str) -> bool:
    if operation is None or len(operation) == 0:
        return False

    return VALID_OPERATIONS_RE.match(operation) is not None


class Problem:
    def __init__(self, operand_1: str, operand_2: str, operation="+"):
        if not (
            validate_operation(operation)
            and validate_operand(operand_1)
            and validate_operand(operand_2)
        ):
            raise ValueError(f"Invalid parameters: {operand_1} {operation} {operand_2}")

        self.op1 = operand_1
        self.op2 = operand_2
        self.operation = operation

    def __str__(self):
        return f"{self.op1} {self.operation} {self.op2}"
