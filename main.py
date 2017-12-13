# This code shows how four different types of Hashing may work:
# Chained, Linear, Quadratic and Double Hashing
# and possible Problems with the latter two.

# The Array of input elements to be put into a Hash table needs to be defined below
# as needs to be defined the length of the Hash table

A = [44, 12, 23, 88, 71, 11, 94, 39, 20, 5, 16]
T_len = 16

A_len = len(A)

def hashfunction (v):
    h = (3*v + 7)%16
    return h
    
def hashfunction2 (v,i):
    h0 = (3*v + 7)%16
    h = h0 + i
    return h
    
def hashfunction3 (v,i):
    h0 = (3*v + 7)%16
    c1 = 0.5
    c2 = 0.5
    h = int((h0 + c1*i + c2*i*i)%16)
    return h

def hashfunction4 (v,i):
    h1 = (3*v + 7)%16
    h2 = 7 - 2*(v % 4)
    h = int(h1 + i*h2)
    return h

# We will add values of a given array to the right position in the value list now
# Depending on a hashing function

# a) Hashing tables

# 1. Chaining
print()
print("-----------Chaining-----------")
print()
failed_T = 0
T1 = [[] for i in range(T_len)]
for a in range (0, len(A)):
    h = hashfunction(A[a])
    print("Value A[",a,"] = ", A[a],": h = ",h)
    T1[h].append(A[a])
print(T1)

print()

# 2. Linear Probing
print("-----------Linear Probing-----------")
print()
failed_T2 = 0
T2 = [[] for i in range(T_len)]
A2_tries = [1 for i in range(A_len)]
for a in range (0, len(A)):
    i = 0
    h2 = hashfunction2(A[a],0)
    print("Attempt Value A[",a,"] = ", A[a],": h = ",h2)
    while(T2[h2 % T_len]!=[] and i<T_len):
        i += 1
        h2 = hashfunction2(A[a],i)
        print("linearly probed: Value A[",a,"] = ", A[a],": h2 = ",h2)
        A2_tries[a] += 1
        if(T2[h2 % T_len]!=[] and i==(T_len - 1)):
            failed_T2 += 1
    T2[h2 % T_len].append(A[a])
print(T2)
print("A2_tries = ", A2_tries)
print("failed_T2 = ", failed_T2)

print()

# 3. Quadratic Probing
print("-----------Quadratic Probing-----------")
print()
failed_T3 = 0
T3 = [[] for i in range(T_len)]
A3_tries = [1 for i in range(A_len)]
for a in range (0, len(A)):
    i = 0
    h3 = hashfunction3(A[a],0)
    print("Attempt Value A[",a,"] = ", A[a],": h = ",h3)
    while(T3[h3 % T_len]!=[] and i<T_len):
        i += 1
        h3 = hashfunction3(A[a],i)
        print("quadraticly probed: Value A[",a,"] = ", A[a],": h3 = ",h3)
        A3_tries[a] += 1
        if(T3[h3 % T_len]!=[] and i==(T_len - 1)):
            failed_T3 += 1
    T3[h3 % T_len].append(A[a])
print(T3)
print("A3_tries = ", A3_tries)
print("failed_T3 = ", failed_T3)

print()

# 4. Double Hashing
print("-----------Double Hashing-----------")
print()
failed_T4 = 0
T4 = [[] for i in range(T_len)]
A4_tries = [1 for i in range(A_len)]
for a in range (0, len(A)):
    i = 0
    h4 = hashfunction4(A[a],0)
    print("Attempt Value A[",a,"] = ", A[a],": h = ",h4)
    while(T4[h4 % T_len]!=[] and i<T_len):
        i += 1
        h4 = hashfunction4(A[a],i)
        print("doubly hashed: Value A[",a,"] = ", A[a],": h4 = ",h4)
        A4_tries[a] += 1
        if(T4[h4 % T_len]!=[] and i==(T_len - 1)):
            failed_T4 += 1
    T4[h4 % T_len].append(A[a])
print(T4)
print("A4_tries = ", A4_tries)
print("failed_T4 = ", failed_T4)

print()

# b) Problems with certain functions

# 1. Double Hashing

print("-----------Problematic Double Hashing-----------")
print()

def hashfunction5 (v,i):
    h1 = (3*v + 7)%16
    h2 = 8 - (v % 8)
    h = int(h1 + i*h2)
    return h
    
failed_T5 = 0
T5 = [[] for i in range(T_len)]
A5_tries = [1 for i in range(A_len)]
for a in range (0, len(A)):
    i = 0
    h5 = hashfunction5(A[a],0)
    print("Attempt Value A[",a,"] = ", A[a],": h = ",h5)
    while(T5[h5 % T_len]!=[] and i<T_len):
        i += 1
        h5 = hashfunction5(A[a],i)
        print("doubly hashed: Value A[",a,"] = ", A[a],": h5 = ",(h5%T_len))
        A5_tries[a] += 1
        if(T5[h5 % T_len]!=[] and i==(T_len - 1)):
            failed_T5 += 1
    if(T5[h5 % T_len] == []):
        T5[h5 % T_len].append(A[a])
print(T5)
print("A5_tries = ", A5_tries)
print("failed_T5 = ", failed_T5)

print()

# 2. Quadratic Hashing: if we choose c1 and c2 unwisely, the same problem occurs

print("-----------Problematic Quadratic Hashing-----------")
print()

def hashfunction6 (v,i):
    h0 = (3*v + 7)%16
    c1 = 8
    c2 = 8
    h = int((h0 + c1*i + c2*i*i)%16)
    return h

failed_T6 = 0
T6 = [[] for i in range(T_len)]
A6_tries = [1 for i in range(A_len)]
for a in range (0, len(A)):
    i = 0
    h6 = hashfunction6(A[a],0)
    print("Attempt Value A[",a,"] = ", A[a],": h = ",h6)
    while(T6[h6 % T_len]!=[] and i<T_len):
        i += 1
        h6 = hashfunction6(A[a],i)
        print("quadraticly probed: Value A[",a,"] = ", A[a],": h6 = ",h6)
        A6_tries[a] += 1
        if(T6[h6 % T_len]!=[] and i==(T_len - 1)):
            failed_T6 += 1
    if(T6[h6 % T_len] == []):
        T6[h6 % T_len].append(A[a])
print(T6)
print("A6_tries = ", A6_tries)
print("failed_T6 = ", failed_T6)

print()
