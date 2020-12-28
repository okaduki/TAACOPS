for n in range(2,25+1,1):
    xs = list(range(1,n+1))
    
    skip_num = 2
    i = -1
    for _ in range(n-1):
        for num in range(skip_num):
            i = (i+1) % n
            while xs[i] == None: i = (i+1) % n
        xs[i] = None
    ans = []
    for i in range(n):
        if xs[i] != None:
            ans.append(xs[i])
    print(n, ans)