def countValidAlignments(A, B):
    count_matrix = [[0] * (B+1) for _ in range(A+1)]


    for k in range(A+1):
        count_matrix[k][0] = 1

    for p in range(B+1):
        count_matrix[0][p] = 1


    for k in range(1, A+1):
        for p in range(1, B+1):
            count_matrix[k][p] = count_matrix[k-1][p] + count_matrix[k][p-1] + count_matrix[k-1][p-1]
            

    return count_matrix[-1][-1]

  
