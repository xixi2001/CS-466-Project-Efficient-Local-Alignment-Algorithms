from naiveLocalAlignment import global_align
from utility import computeScore
def linear_space_global_alignment(v, w, delta):
    
    dp_pre = [0 for i in range(len(w)+1)]
    dp_cur = [0 for i in range(len(w)+1)]

    dp_cur[0] = 0
    for j in range(1,len(w)+1):
        dp_cur[j] = dp_cur[j-1] + delta['-'][w[j-1]]
    
    max_score = -1e9
    
    for i in range(1,len(v)+1):
        for j in range(len(w)+1):
            dp_pre[j] = dp_cur[j]
            dp_cur[j] = -1e9
        
        for j in range(len(w)+1):
            a,b = v[i-1], w[j-1]
            if i>0 and dp_pre[j]+delta[a]['-']>dp_cur[j]:
                dp_cur[j] = dp_pre[j]+delta[a]['-']
            if j>0 and dp_cur[j-1]+delta['-'][b]>dp_cur[j]:
                dp_cur[j] = dp_cur[j-1]+delta['-'][b]
            if i>0 and j>0 and dp_pre[j-1]+delta[a][b]>dp_cur[j]:
                dp_cur[j] = dp_pre[j-1]+delta[a][b]
            
            if dp_cur[j] > max_score:
                max_score = dp_cur[j]
    return dp_cur

def linear_space_backward(v, w, delta):
    dp_pre = [0 for i in range(len(w)+1)]
    dp_cur = [0 for i in range(len(w)+1)]
    
    dp_cur[len(w)] = 0
    max_score = 0
    max_i,max_j = 0,0
    for j in range(len(w)-1,-1,-1):
        dp_cur[j] = dp_cur[j+1] + delta['-'][w[j]]
    # print(dp_cur)
    for i in range(len(v)-1,-1,-1):
        for j in range(len(w),-1,-1):
            dp_pre[j] = dp_cur[j]
            dp_cur[j] = -1e9
        
        for j in range(len(w),-1,-1):
            a = v[i]
            if dp_pre[j]+delta[a]['-']>dp_cur[j]:
                    dp_cur[j] = dp_pre[j]+delta[a]['-']
            if j == len(w):
                continue
            b = w[j]
            if dp_cur[j+1]+delta['-'][b]>dp_cur[j]:
                    dp_cur[j] = dp_cur[j+1]+delta['-'][b]
            if dp_pre[j+1]+delta[a][b]>dp_cur[j]:
                    dp_cur[j] = dp_pre[j+1]+delta[a][b]
            if dp_cur[j] > max_score:
                max_score = dp_cur[j]
                max_i = i
                max_j = j
        # print(dp_cur)
    return dp_cur,(max_i,max_j)


def Hirschberg(v, w, delta):
    if len(v) == 0:
        return '-'*len(w),w
    if len(w) == 0:
        return v,'-'*len(v)
    if len(v) == 1:
        score, alignment = global_align(v, w, delta)
        return alignment.split('\n')
    mid = len(v)//2
    vl = v[0:mid]
    vr = v[mid:]
    prefix = linear_space_global_alignment(vl, w, delta)
    suffix = linear_space_backward(vr, w, delta)[0]
    max_score = -1e9
    w_mid = 0
    for j in range(len(w)+1):
        if prefix[j] + suffix[j] > max_score:
            max_score = prefix[j] + suffix[j]
            w_mid = j
    
    wl = w[0:w_mid]
    wr = w[w_mid:]

    # xxxxxx = input()
    
    resl = Hirschberg(vl, wl, delta)
    resr = Hirschberg(vr, wr, delta)

    # print("-----------------------------------")
    # print(v)
    # print(w)
    # print(vl," , ", vr)
    # print(max_score)
    # for j in range(len(w)+1):
    #     print(j, prefix[j], suffix[j])

    return resl[0]+resr[0], resl[1]+resr[1]

def linear_space_local_align(v, w, delta):
    if len(v) < len(w):
        v, w = w, v
    
    dp_pre = [0 for i in range(len(w)+1)]
    dp_cur = [0 for i in range(len(w)+1)]

    dp_cur[0] = 0
    for j in range(1,len(w)+1):
        dp_cur[j] = max(dp_cur[j-1] + delta['-'][w[j-1]],0)
    
    max_score = 0
    max_i,max_j = 0,0
    
    for i in range(1,len(v)+1):
        for j in range(len(w)+1):
            dp_pre[j] = dp_cur[j]
            dp_cur[j] = 0
        
        for j in range(len(w)+1):
            a,b = v[i-1], w[j-1]
            if i>0 and dp_pre[j]+delta[a]['-']>dp_cur[j]:
                dp_cur[j] = dp_pre[j]+delta[a]['-']
            if j>0 and dp_cur[j-1]+delta['-'][b]>dp_cur[j]:
                dp_cur[j] = dp_cur[j-1]+delta['-'][b]
            if i>0 and j>0 and dp_pre[j-1]+delta[a][b]>dp_cur[j]:
                dp_cur[j] = dp_pre[j-1]+delta[a][b]
            
            if dp_cur[j] > max_score:
                max_score = dp_cur[j]
                max_i = i
                max_j = j
    print("best score: ",max_score)
    return max_i,max_j

def linear_space_local_align_solution(v, w, delta):
    i,j = linear_space_local_align(v, w, delta)
    v = v[:i]
    w = w[:j]
    i,j = linear_space_backward(v, w, delta)[1]
    v = v[i:]
    w = w[j:]
    return Hirschberg(v, w, delta)

keys = []
for i in range(26):
    keys.append(chr(ord('A') + i))
keys.append('-')
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}

res = linear_space_local_align_solution("AACCTGAC", "CTACGTAC", delta)
print("score: ", computeScore(res[0],res[1],delta))
print(res[0] + "\n" + res[1])


