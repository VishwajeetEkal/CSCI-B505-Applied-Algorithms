def who_wins(n, k):
    length = [ i for i in range(1,n+1)]
    run = len(length)
    while run !=1:
        for i in range(k-1):
            length.append(length.pop(0))
        length.pop(0)
        run = len(length)
    winner = length.pop()

    return winner




