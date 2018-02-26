def harmonic_list(n):

    result = []
    h = 0
    for i in range(1, n + 1):
        h += 1 / i
        result.append(h)
    return result
