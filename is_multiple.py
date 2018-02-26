def is_multiple(n, m):
    if n % m == 0:
        return True
    return False


print(is_multiple(15, 5))
print(is_multiple(45, 5))
print(is_multiple(42, 5))
print(is_multiple(5, 15))
