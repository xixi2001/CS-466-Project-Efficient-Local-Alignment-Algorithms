# codes from homework 1
UP = (-1,0)
LEFT = (0, -1)
TOPLEFT = (-1, -1)
ORIGIN = (0, 0)

def traceback_local(v, w, M, init_i, init_j, pointers):
    i,j = init_i, init_j
    new_v = []
    new_w = []
    while True:
        di, dj = pointers[i][j]
        if (di,dj) == LEFT:
            new_v.append('-')
            new_w.append(w[j-1])
        elif (di,dj) == UP:
            new_v.append(v[i-1])
            new_w.append('-')
        elif (di,dj) == TOPLEFT:
            new_v.append(v[i-1])
            new_w.append(w[j-1])
        i, j = i + di, j + dj
        if (M[i][j] == 0):
            break
    return ''.join(new_v[::-1]) + '\n'+''.join(new_w[::-1])

def local_align(v, w, delta):
    """
    Returns the score of the maximum scoring alignment of all possible substrings of v and w. 
    
    :param: v
    :param: w
    :param: delta
    """
    print(v, w)
    dp = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]        
    pointers = [[ORIGIN for j in range(len(w)+1)] for i in range(len(v)+1)]
    score = -1e9
    init_i, init_j = 0,0
    for i in range(len(v)+1):
      for j in range(len(w)+1):
        dp[i][j] = 0
        a = v[i-1]
        b = w[j-1]
        # UP
        if i>0 and dp[i-1][j]+delta[a]['-']>dp[i][j]:
          dp[i][j] = dp[i-1][j]+delta[a]['-']
          pointers[i][j] = UP
        # LEFT
        if j>0 and dp[i][j-1]+delta['-'][b]>dp[i][j]:
          dp[i][j] = dp[i][j-1]+delta['-'][b]
          pointers[i][j] = LEFT
        # TOPLEFT
        if i>0 and j>0 and dp[i-1][j-1]+delta[a][b]>dp[i][j]:
          dp[i][j] = dp[i-1][j-1]+delta[a][b]
          pointers[i][j] = TOPLEFT

        #update score
        if dp[i][j] >= score:
          score = dp[i][j]
          init_i = i
          init_j = j
    
    # for i in range(len(v)+1):
    #   print(dp[i])
    alignment = traceback_local(v, w, dp, init_i, init_j , pointers)
    return score, alignment 


def traceback_global(v, w, pointers):
    i,j = len(v), len(w)
    new_v = []
    new_w = []
    while True:
        di, dj = pointers[i][j]
        if (di,dj) == LEFT:
            # print("LEFT")
            new_v.append('-')
            new_w.append(w[j-1])
        elif (di,dj) == UP:
            # print("UP")
            new_v.append(v[i-1])
            new_w.append('-')
        elif (di,dj) == TOPLEFT:
            # print("TOPLEFT")
            new_v.append(v[i-1])
            new_w.append(w[j-1])
        i, j = i + di, j + dj
        if (i <= 0 and j <= 0):
            break
    return ''.join(new_v[::-1])+'\n'+''.join(new_w[::-1])
    


def global_align(v, w, delta):
    """
    Returns the score of the maximum scoring alignment of the strings v and w, as well as the actual alignment as 
    computed by traceback_global. 
    
    :param: v
    :param: w
    :param: delta
    """
    dp = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]
    pointers = [[ORIGIN for j in range(len(w)+1)] for i in range(len(v)+1)]
    score, alignment = None, None

    for j in range(1,len(w)+1):
      dp[0][j] = -j
      pointers[0][j] = LEFT
    
    for i in range(1,len(v)+1):
      dp[i][0] = -i
      pointers[i][0] = UP

    for i in range(1,len(v)+1):
      for j in range(1,len(w)+1):
        if i==0 and j==0:
          continue
        dp[i][j] = -1e18
        a = v[i-1]
        b = w[j-1]
        # LEFT
        if j>0 and dp[i][j-1]+delta['-'][b]>dp[i][j]:
          dp[i][j] = dp[i][j-1]+delta['-'][b]
          pointers[i][j] = LEFT
        # UP
        if i>0 and dp[i-1][j]+delta[a]['-']>dp[i][j]:
          dp[i][j] = dp[i-1][j]+delta[a]['-']
          pointers[i][j] = UP
        # TOPLEFT
        if i>0 and j>0 and dp[i-1][j-1]+delta[a][b]>dp[i][j]:
          dp[i][j] = dp[i-1][j-1]+delta[a][b]
          pointers[i][j] = TOPLEFT
    alignment = traceback_global(v,w, pointers)
    score = dp[len(v)][len(w)]
    # for i in range(len(v)+1):
    #   print(dp[i])
    # for i in range(len(v)+1):
    #   print(pointers[i])
    # print(score)
    # print(alignment)
    return score, alignment


keys = ['A', 'C', 'T', 'G', '-']
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}
    
# local_align("TAGATA", "GTAGGCTTAAGGTTA", delta)
# local_align("TAGATA","GTAGGCTTAAGGTTA",delta)

res = local_align("AACCTGAC", "CTACGTAC", delta)
# print(res[0])
# print(res[1])
