def linear_space_local_align(v, w, delta):
    if len(v) < len(w):
        v, w = w, v
    
    dp_pre = [0 for i in range(len(w)+1)]
    dp_cur = [0 for i in range(len(w)+1)]
    cnt_pre = [0 for i in range(len(w)+1)]
    cnt_cur = [0 for i in range(len(w)+1)]

    dp_cur[0] = 0
    cnt_cur[0] = 1
    for j in range(1,len(w)+1):
        dp_cur[j] = max(dp_cur[j-1] + delta['-'][w[j-1]],0)
        if dp_cur[j] == dp_cur[j-1] + delta['-'][w[j-1]]:
            cnt_cur[j] += cnt_cur[j-1]
        if dp_cur[j] == 0:
            cnt_cur[j] += 1
    
    max_score = 0
    total_optiaml_alignment_count = 0
    
    for i in range(1,len(v)+1):
        for j in range(len(w)+1):
            dp_pre[j] = dp_cur[j]
            dp_cur[j] = 0
            cnt_pre[j] = cnt_cur[j]
            cnt_cur[j] = 0
        
        for j in range(len(w)+1):
            a,b = v[i-1], w[j-1]
            if i>0 and dp_pre[j]+delta[a]['-']>dp_cur[j]:
                dp_cur[j] = dp_pre[j]+delta[a]['-']
            if j>0 and dp_cur[j-1]+delta['-'][b]>dp_cur[j]:
                dp_cur[j] = dp_cur[j-1]+delta['-'][b]
            if i>0 and j>0 and dp_pre[j-1]+delta[a][b]>dp_cur[j]:
                dp_cur[j] = dp_pre[j-1]+delta[a][b]
            
            if i>0 and dp_pre[j]+delta[a]['-'] == dp_cur[j]:
                cnt_cur[j] += cnt_pre[j]
            if j>0 and dp_cur[j-1]+delta['-'][b] == dp_cur[j]:
                cnt_cur[j] += cnt_cur[j-1]
            if i>0 and j>0 and dp_pre[j-1]+delta[a][b] == dp_cur[j]:
                cnt_cur[j] += cnt_pre[j-1]
            if dp_cur[j] == 0:
                cnt_cur[j] += 1
            
            if dp_cur[j] > max_score:
                max_score = dp_cur[j]
                total_optiaml_alignment_count = 0
            if dp_cur[j] == max_score:
                total_optiaml_alignment_count += cnt_cur[j]
                if max_score == 2:
                    print(i,j,": ", cnt_cur[j])
    # print("best score: ",max_score)
    # print("total optiaml alignment count: ",total_optiaml_alignment_count)
    return total_optiaml_alignment_count

keys = []
for i in range(26):
    keys.append(chr(ord('A') + i))
keys.append('-')
delta = {}
for i in range(len(keys)):
    delta[keys[i]] = {k : v for (k,v) in zip(keys, [1 if keys[i] == keys[j]  else -1 for j in range(len(keys))])}
# linear_space_local_align("BIOLGIA", "BOILGAI", delta)
# linear_space_local_align("ATCGAAGT", "ACCTGCA", delta)