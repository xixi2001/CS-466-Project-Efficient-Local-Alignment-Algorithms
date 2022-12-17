
from utility import print_reversed_list
def tracebackAll(v, w, dp, i, j, s, t):
  sum = 0
  if dp[i][j] == 0:
    print("------------------------")
    print_reversed_list(s)
    print_reversed_list(t)
    sum += 1
  a = v[i-1]
  b = w[j-1]
  if i>0 and j>0 and dp[i-1][j-1]+delta[a][b]==dp[i][j]:
    s.append(a)
    t.append(b)
    sum += tracebackAll(v, w, dp, i-1, j-1, s, t)
    s.pop()
    t.pop()
  
  if i>0 and dp[i-1][j]+delta[a]['-']==dp[i][j]:
    s.append(a)
    t.append('-')
    sum += tracebackAll(v, w, dp, i-1, j, s, t)
    s.pop()
    t.pop()
  
  if j>0 and dp[i][j-1]+delta['-'][b]==dp[i][j]:
    s.append('-')
    t.append(b)
    sum += tracebackAll(v, w, dp, i, j-1, s, t)
    s.pop()
    t.pop()
  
  return sum
  

def local_align(v, w, delta):
    """
    Returns the score of the maximum scoring alignment of all possible substrings of v and w. 
    
    :param: v
    :param: w
    :param: delta
    """
    dp = [[0 for j in range(len(w)+1)] for i in range(len(v)+1)]        
    score = -1e9
    for i in range(len(v)+1):
      for j in range(len(w)+1):
        dp[i][j] = 0
        a = v[i-1]
        b = w[j-1]
        # UP
        if i>0 and dp[i-1][j]+delta[a]['-']>dp[i][j]:
          dp[i][j] = dp[i-1][j]+delta[a]['-']
        # LEFT
        if j>0 and dp[i][j-1]+delta['-'][b]>dp[i][j]:
          dp[i][j] = dp[i][j-1]+delta['-'][b]
        # TOPLEFT
        if i>0 and j>0 and dp[i-1][j-1]+delta[a][b]>dp[i][j]:
          dp[i][j] = dp[i-1][j-1]+delta[a][b]

        #update score
        if dp[i][j] >= score:
          score = dp[i][j]
    
    # for i in range(len(v)+1):
    #   print(dp[i])
    total_optiaml_alignment_count = 0
    for i in range(len(v)+1):
      for j in range(len(w)+1):
        if dp[i][j] == score:
          total_optiaml_alignment_count += tracebackAll(v ,w, dp, i, j, [], [])
    print("total optiaml alignment count: ",total_optiaml_alignment_count)
    return None


keys = []
for i in range(26):
    keys.append(chr(ord('A') + i))
keys.append('-')
print(keys)
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}
    
local_align("BIOLGIA", "BOILGAI", delta)
local_align("ATCGAAGT", "ACCTGCA", delta)