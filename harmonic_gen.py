def harmonic_gen(n):
    h = 0
    for i in range(1, n + 1):
        h += 1/i
        yield h
