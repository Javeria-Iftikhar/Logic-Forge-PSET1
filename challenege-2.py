from collections import Counter

def minWindow(log, pattern):
    need = Counter(pattern)
    left = 0
    count = len(pattern)
    min_len = float('inf')
    start = 0

    for right in range(len(log)):
        if need[log[right]] > 0:
            count -= 1
        need[log[right]] -= 1

        while count == 0:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start = left

            need[log[left]] += 1
            if need[log[left]] > 0:
                count += 1
            left += 1

    return "" if min_len == float('inf') else log[start:start + min_len]
log = "ADOBECODEBANC"
pattern = "ABD"
print(minWindow(log, pattern))