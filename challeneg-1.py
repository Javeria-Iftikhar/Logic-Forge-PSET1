# challnege-1
def overall_performnaec(contributions):
    n = len(contributions)
    impact = [1] * n

    # Prefix products
    before = 1
    for i in range(n):
        impact[i] = before
        before *= contributions[i]

    # Suffix products
    after = 1
    for i in range(n - 1, -1, -1):
        impact[i] *= after
        after *= contributions[i]

    return impact

print(overall_performnaec([2,1,3,9]))
