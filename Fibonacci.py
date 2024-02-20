def fibonacci(n):
    fib = [0, 1]
    if n in [0, 1]:
        return n
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib


n = int(input("Fibonacci Num: "))
print(fibonacci(n))

# OR


def fibonacci(num):
    if num in [0, 1]:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)


num = int(input("Fibonacci Num: "))
for i in range(num):
    print(fibonacci(i), end=" ")
