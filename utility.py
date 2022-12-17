def print_list(s):
    str = ""
    for c in s:
        str += c
    print(str)

def print_reversed_list(s):
    str = ""
    for i in range(len(s)-1,0-1,-1):
        str += s[i]
    print(str)
    return str

def computeScore(u, v, delta):
    sum = 0
    for i in range(len(u)):
        sum += delta[u[i]][v[i]]
    return sum