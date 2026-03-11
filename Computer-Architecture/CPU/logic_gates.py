#place holder
def nand(a, b):
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError(f"inputs must be 0 or 1, got {a}, {b}")
    return 0 if (a == 1 and b == 1) else 1
