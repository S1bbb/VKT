def sum_of_digits(n):
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_of_digits(n // 10)


n = int(input())
print(sum_of_digits(n))
