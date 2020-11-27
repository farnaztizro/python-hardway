def jam(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def tafriq(a, b):
    print(f"SUBTRACTING {a} - {b}")    
    return a - b

def zarb(a, b):
    print(f"MULTIPLYING {a} * {b}")    
    return a * b

def taqsim(a, b):
    print(f"DIVIDING {a} / {b}")    
    return a / b

print("let's do some math with functions!!")    

age = jam(30, 5)
height = tafriq(78, 4)
weight = zarb(90, 2)
iq = taqsim(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")
