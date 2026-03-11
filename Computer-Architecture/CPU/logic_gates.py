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
def Not16(bits16_list): # a list of 16 bits
    if len(bits16_list) != 16:
        raise ValueError(f"Expected 16 bits, got {len(bits16_list)}")
    Not_bus = []
    for bit in bits16_list:
        Not_bus.append(Not(bit))
    return Not_bus
def And16(bits16_bus1, bits16_bus2): # 16-lists of bits
    if len(bits16_bus1) != 16 or len(bits16_bus2) != 16:
        raise ValueError(t"Expected 16 bits, got {len(bits16_bus1)}, {len(bits16_bus2)}")
    And_bus = []
    for i in range(15):
        And_bus.append(And(bits16_bus1[i],bits16_bus2[i]))
    return And_bus
def Or16(a, b):
    pass

def Mux16(a, b, sel):
    pass

def Or8Way(a):
    pass

def Mux4Way16(a, b, c, d, sel):
    pass

def Mux8Way16(a, b, c, d, e, f, g, h, sel):
    pass

def DMux4Way(inp, sel):
    pass

def DMux8Way(inp, sel):
    pass
print(f" {Xor(0,0)}, {Xor(1,0)}, {Xor(0,1)}, {Xor(1,1)}")