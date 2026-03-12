#place holder
def Nand(a, b):
    if a not in (0, 1) or b not in (0, 1):
        raise ValueError(f"Expected 0 or 1, got {a}, {b}")
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
#a.nots + s.b
def Mux(a, b, sel):
    return Or(And(a, Not(sel)), And(sel,b))
def DMux(sel, Inp):
    return (And(sel,Inp ),And(Not(sel),Inp))
def Not16(a16): # a list of 16 bits
    if len(a16) != 16:
        raise ValueError(f"Expected 16 bits, got {len(a16)}")
    return [Not(a16[i]) for i in range(16)]
def And16(a16, b16): # 16-lists of bits
    if len(a16) != 16 or len(b16) != 16:
        raise ValueError(f"Expected 16 bits, got {len(a16)}, {len(b16)}")
    return [And(a16[i],b16[i]) for i in range(16)]
def Or16(a16, b16):
    if len(a16) != 16 or len(b16) != 16:
        raise ValueError(f"Expected 16 bits, got {len(a16)}, {len(b16)}")
    return [Or(a16[i],b16[i]) for i in range(16)]
def Mux16(a16, b16, sel):
    if len(a16) != 16 or len(b16) != 16:
        raise ValueError(f"Expected 16 bits, got {len(a16)}, {len(b16)}")
    return [Mux(a16[i], b16[i], sel) for i in range(16)]
def Or8Way(a8):
    pre_Or = 0
    for i in range(8):
        pre_Or = Or(a8[i],pre_Or)
    return pre_Or

def Mux4Way16(a16_4, sel): #4-list of 16-lists
    pass

def Mux8Way16(a16, sel):
    pass

def DMux4Way(inp, sel):
    pass

def DMux8Way(inp, sel):
    pass
a1 =[1,0,1,0,1,0,1,0]
a = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]
b = [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
print(Or8Way(a1))

print(Not16(a))      # expected: [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]
print(And16(a,b))    # expected: all zeros
print(Or16(a,b))     # expected: all ones
print(Mux16(a,b,0))  # expected: a
print(Mux16(a,b,1))  # expected: b