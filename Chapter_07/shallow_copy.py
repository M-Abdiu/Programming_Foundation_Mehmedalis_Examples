# Kopieren von Listen
# Shallow copies

# Option 1:
original = [1, 2, 3, 4]
copied = []

for item in original:
    copied.append(item)

print("Original:", original)
print("Copied:", copied)
original.append(5)
print("Original:", original)
print("Copied:", copied)
print()

# Option 2:
original = [1, 2, 3, 4]
copied = []
copied = copied + original   # or copied += original

print("Original:", original)
print("Copied:", copied)
original.append(5)
print("Original:", original)
print("Copied:", copied)
print()

# Option 3:
original = [1, 2, 3, 4]
copied = original[:]
print("Original:", original)
print("Copied:", copied)
original.append(5)
print("Original:", original)
print("Copied:", copied)
print()

# Option 4:
original = [1, 2, 3, 4]
copied = list(original)
print("Original:", original)
print("Copied:", copied)
original.append(5)
print("Original:", original)
print("Copied:", copied)
print()

# Option 5:
original = [1, 2, 3, 4]
copied = original.copy()
print("Original:", original)
print("Copied:", copied)
original.append(5)
print("Original:", original)
print("Copied:", copied)
print()

# Zuweisung vs. shallow copy!!
a = [1, 2, 3]
b = a   # Zuweisung, kein Kopieren
print("a", a)
print("b", b)
print()
a.append(4)
print("a", a)
print("b", b)
