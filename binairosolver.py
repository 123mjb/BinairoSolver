def solve(inp:list[list[int]]):
    numbersdown = [0,0,0]
    numbersacross = [0,0,0]
    for i in range(0,len(inp)):
        for g in range(0,len(inp[i])):
            if inp[i][g] == 3:
                if len(inp[i])-g>3:
                    if inp[i][g+1] == 1 and inp[i][g+2] == 1:
                        inp[i][g] = 0
                        if len(inp[i])-g >3 and inp[i][g+3] == 3:
                            inp[i][g+3] = 0
                    if inp[i][g+1] == 0 and inp[i][g+2] == 0:
                        inp[i][g] = 1
                        if len(inp[i])-g >3 and inp[i][g+3] == 3:
                            inp[i][g+3] = 1
                if len(inp)-i >3:
                    if inp[i+1][g] == 1 and inp[i+2][g] == 1:
                        inp[i][g] = 0
                        if len(inp)-i >3 and inp[i+3][g] == 3:
                            inp[i+3][g] = 0
                    if inp[i+1][g] == 0 and inp[i+2][g] == 0:
                        inp[i][g] = 1
                        if len(inp)-i >3 and inp[i+3][g] == 3:
                            inp[i+3][g] = 1
                if g > 0 and len(inp[i]) - g > 1:
                    if inp[i][g-1] == 1 and inp[i][g+1] == 1:
                        inp[i][g] = 0
                    if inp[i][g-1] == 0 and inp[i][g+1] == 0:
                        inp[i][g] = 1
                if i > 0 and len(inp) - i > 1:
                    if inp[i-1][g] == 1 and inp[i+1][g] == 1:
                        inp[i][g] = 0
                    if inp[i-1][g] == 0 and inp[i+1][g] == 0:
                        inp[i][g] = 1
            if inp[i][g] == 3:
                if g>1:
                    if inp[i][g-1] == 1 and inp[i][g-2] == 1:
                        inp[i][g] = 0
                        if g >2 and inp[i][g-3] == 3:
                            inp[i][g-3] = 0
                    if inp[i][g-1] == 0 and inp[i][g-2] == 0:
                        inp[i][g] = 1
                        if g >2 and inp[i][g-3] == 3:
                            inp[i][g-3] = 1
                if i >1:
                    if inp[i-1][g] == 1 and inp[i-2][g] == 1:
                        inp[i][g] = 0
                        if i >2 and inp[i-3][g] == 3:
                            inp[i-3][g] = 0
                    if inp[i-1][g] == 0 and inp[i-2][g] == 0:
                        inp[i][g] = 1
                        if i >2 and inp[i-3][g] == 3:
                            inp[i-3][g] = 1
    for i in range(0,len(inp)):
        numbersdown=[0,0,0]
        for g in inp[i]:
            if g==0: numbersdown[0]+=1
            if g==1: numbersdown[1]+=1
            if g==3: numbersdown[2]+=1
        if numbersdown[0] == 4:
            for k in range(0,len(inp[i])):
                if inp[i][k] == 3: inp[i][k] = 1
        if numbersdown[1] == 4:
            for k in range(0,len(inp[i])):
                if inp[i][k] == 3: inp[i][k] = 0
    for i in range(0,len(inp[0])):
        numbersacross=[0,0,0]
        for g in inp:
            if g[i]==0: numbersacross[0]+=1
            if g[i]==1: numbersacross[1]+=1
            if g[i]==3: numbersacross[2]+=1
        if numbersacross[0] == 4:
            for k in range(0,len(inp)):
                if inp[k][i] == 3: inp[k][i] = 1
        if numbersacross[1] == 4:
            for k in range(0,len(inp)):
                if inp[k][i] == 3: inp[k][i] = 0
    return inp
def printer(output:list[list[int]]):
    printout=""
    for i in range(0,len(output[0])):
        for g in range(0,len(output)):
            printout += str(output[g][i])
        if i < len(output[0])-1:
            printout += "\n"
    print(printout)


"""printer(solve([
    [3,1,3,3],
    [1,0,0,1],
    [1,0,0,3],
    [3,1,3,3]
]))"""