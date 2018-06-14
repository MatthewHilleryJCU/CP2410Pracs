def all_distinct(seq):
    for i in range(0, len(seq) - 1):
        for j in range(i + 1, len(seq)):
            if seq[i] == seq[j]:
                return False
    return True

print (all_distinct("348761"))