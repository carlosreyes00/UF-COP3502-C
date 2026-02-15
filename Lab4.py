
def fibonacci(n):
    a = 0
    b = 1
    c = 0

    if n == 2:
        return fibonacci(3)

    for i in range(n-2):
        c = a + b
        a = b
        b = c
    return c

def is_prime(n):
    if n <= 0:
        return False

    m = 3

    if n == 1:
        return False

    if n == 2:
        return True

    while m*m <= n:
        if n % m == 0:
            return False
        m += 2

    return True

def print_prime_factors(n):
    result = f"{n} = "

    if is_prime(n):
        result += f"{n}"
        print(result)
        return

    i = 2
    while i * i <= n:
        if n % i == 0 and is_prime(i):
            while n % i == 0:
                n //= i
                if n == 1:
                    result += f"{i}"
                else:
                    result += f"{i} * "
        i += 1

    if n > 1:
        if result.endswith(" * "):
            result += f"{n}"
        else:
            result += f"{n}"

    print(result)
