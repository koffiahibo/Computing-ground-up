#place holder
def Nand(a, b):
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError(f"inputs must be 0 or 1, got {a}, {b}")
    return 0 if (a == 1 and b == 1) else 1

def Not(a):
    return Nand(a,a)
def And(a, b):
    return Not(Nand(a,b))
def Or(a, b):
    return Nand(Not(a),Not(b))
def Xor(a, b):
    return And(Or(a,b), Nand(a,b)) #"at least one is 1" AND "not both are 1"
def Xor(a, b): #main
    return Or(And(a, Not(b)), And(Not(a),b)) # always one and not the other, not both

print(f" {Xor(0,0)}, {Xor(1,0)}, {Xor(0,1)}, {Xor(1,1)}")
