import sympy

l = 1
for i in range(1, 21):
    l = sympy.lcm(l, i)
print(l)