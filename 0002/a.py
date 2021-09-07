fib = [1, 2]

while fib[-1] + fib[-2] < 4*10**6:
    fib.append(fib[-1] + fib[-2])

answer = sum(x for x in fib if x % 2 == 0)
print(answer)