def count_removals(s):
    lrem = rrem = 0
    for ch in s:
        if ch == '(':
            lrem += 1
        elif ch == ')':
            if lrem > 0:
                lrem -= 1
            else:
                rrem += 1
    return lrem, rrem
def removeInvalidParentheses(expr):
    lrem, rrem = count_removals(expr)
    result = set()

    def dfs(index, path, open_count, lrem, rrem):
        # End of string
        if index == len(expr):
            if open_count == 0 and lrem == 0 and rrem == 0:
                result.add(path)
            return

        ch = expr[index]

        # Option 1: Remove '('
        if ch == '(' and lrem > 0:
            dfs(index + 1, path, open_count, lrem - 1, rrem)

        # Option 2: Remove ')'
        if ch == ')' and rrem > 0:
            dfs(index + 1, path, open_count, lrem, rrem - 1)

        # Option 3: Keep character
        if ch not in "()":
            dfs(index + 1, path + ch, open_count, lrem, rrem)
        elif ch == '(':
            dfs(index + 1, path + ch, open_count + 1, lrem, rrem)
        elif ch == ')' and open_count > 0:
            dfs(index + 1, path + ch, open_count - 1, lrem, rrem)

    dfs(0, "", 0, lrem, rrem)
    return list(result)
print(removeInvalidParentheses("()())()"))