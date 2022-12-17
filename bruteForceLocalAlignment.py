from naiveLocalAlignment import local_align
from utility import print_list
A = "BOILGAI"
B = "BIOLGIA"
u,v = "",""
s = []
t = []

keys = []
for i in range(26):
    keys.append(chr(ord('A') + i))
keys.append('-')
print(keys)
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}
best_score, optimal_alignment = local_align(A, B, delta)

print("best score:" ,best_score)
# print(optimal_alignment)




def depthFirstSearch(i, j):
    if i == len(u) and j == len(v):
        score = 0
        for index in range(len(s)):
            score += delta[s[index]][t[index]]
        if score == best_score:
            print("----------------------------------------------")
            print_list(s)
            print_list(t)
            return 1
        # print_list(s)
        # print_list(t)
        # print(score)
        return 0
    
    sum = 0
    if i < len(u) and j < len(v):
        s.append(u[i])
        t.append(v[j])
        sum += depthFirstSearch(i+1,j+1)
        s.pop()
        t.pop()
    if i < len(u):
        s.append(u[i])
        t.append('-')
        sum += depthFirstSearch(i+1,j)
        s.pop()
        t.pop()
    if j < len(v):
        s.append('-')
        t.append(v[j])
        sum += depthFirstSearch(i,j+1)
        s.pop()
        t.pop()
    
    return sum

total_optiaml_alignment_count = 0
# print(A, B)
for Al in range(len(A)):
    for Ar in range(Al,len(A)):
        for Bl in range(len(B)):
            for Br in range(Bl,len(B)):
                u = A[Al:Ar+1]
                v = B[Bl:Br+1]
                # print("------------")
                # print(u)
                # print(Bl,Br, v)
                total_optiaml_alignment_count += depthFirstSearch(0,0)
print("total optiaml alignment count: ",total_optiaml_alignment_count)
