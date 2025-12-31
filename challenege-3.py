
def median(scoreA, scoreB):
    m = len(scoreA)
    n = len(scoreB)
    total = m + n

    i = j = 0
    count = 0
    prev = curr = 0

    while count <= total // 2:
        prev = curr

        if i < m and (j >= n or scoreA[i] <= scoreB[j]):
            curr = scoreA[i]
            i += 1
        else:
            curr = scoreB[j]
            j += 1

        count += 1

    if total % 2 != 0:
        return float(curr)
    else:
        return (prev + curr) / 2
print(median([1, 2], [3, 4]))