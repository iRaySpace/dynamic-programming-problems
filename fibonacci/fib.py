# Function for Fibonacci
def fib_start(n):
    """Accepts any n integer"""

    # Basics
    initial_mem = [0, 1]

    # Memoization Table
    mem = [-1 for _ in range(n - 1)]
    mem = initial_mem + mem

    return fib_main(n, mem)


def fib_main(n, mem):
    # If already calculated
    if mem[n] != -1:
        return mem[n]

    # If not calculated
    else:
        mem[n] = fib_main(n - 1, mem) + fib_main(n - 2, mem)
        return fib_main(n, mem)

# Get input from user
num = input("Input any number: ")

# Call the function
fibo = fib_start(int(num))
print("The result is {0}.".format(fibo))
