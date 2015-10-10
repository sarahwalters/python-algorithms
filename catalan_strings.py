# 10/10/15 from Cracking the Coding Interview

def catalan_strings(n):
    if n == 0:
        return [""]
    else:
        prev_layer = catalan_strings(n-1)
        print len(prev_layer)
        res = []
        for cstring in prev_layer:
            res = res + add_parens(cstring)
        return set(res)

def add_parens(item):
    res = []

    # add () inside each set of parentheses, in turn
    for (i, char) in enumerate(item):
        if char == "(":
            new_str = item[:i+1]+"()"+item[i+1:]
            res.append(new_str)

    res.append(item + "()")

    return res
