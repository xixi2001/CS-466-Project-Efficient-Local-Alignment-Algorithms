import hirschbergLocalAlignment, utility, linearSpaceCounting, tracebackAll

def compute(sequence1, sequence2):

    print("Local Alignment for ", sequence1, " and ", sequence2)
    delta = hirschbergLocalAlignment.delta
    local_alignment = hirschbergLocalAlignment.linear_space_local_align_solution(sequence1, sequence2, delta)
    best_score = utility.computeScore(local_alignment[0], local_alignment[1], delta)
    num_of_alignment = linearSpaceCounting.linear_space_local_align(sequence1, sequence2, delta)
    tracebackAll.list.clear()
    tracebackAll.local_align(sequence1, sequence2, delta) 
    print("Optimal Score: ", best_score) 
    print("One Optimal Local Alignment: ", local_alignment)
    print("Total Number of Local Alignment: ", num_of_alignment)
    print("Printing All Local Alignments:")
    for i in tracebackAll.list:
        print(i)

if __name__=="__main__":
    a = input("Enter First Sequence: ")
    b = input("Enter Second Sequence: ")
    compute(a, b)