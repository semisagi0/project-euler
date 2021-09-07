def is_palindrome(n):
    return str(n) == ''.join(reversed(str(n)))

answer = 0
for x in range(100, 1000):
    for y in range(100, 1000):
        if is_palindrome(x * y):
            answer = max(answer, x * y)
print(answer)