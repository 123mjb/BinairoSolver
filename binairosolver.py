def solve(inp:list[list[int]]):
    g_threes = 0
    g_ones = 0
    g_zeros = 0
    p_threes = 0
    p_ones = 0
    p_zeros = 0
    for i in range(0,len(inp)):
        for g in range(0,len(inp[i])):
            if inp[i][g] == 3:
                if len(inp[i])-1-g>=2:
                    if inp[i][g+1] == 1 and inp[i][g+2] == 1:
                        inp[i][g] = 0
                        if len(inp[i])-g >2 and inp[i][g+3] == 3:
                            inp[i][g+3] = 0
                    if inp[i][g+1] == 0 and inp[i][g+2] == 0:
                        inp[i][g] = 1
                        if len(inp[i])-g >2 and inp[i][g+3] == 3:
                            inp[i][g+3] = 1
                if len(inp)-i-1 >=2:
                    if inp[i+1][g] == 1 and inp[i+2][g] == 1:
                        inp[i][g] = 0
                        if len(inp)-i >2 and inp[i+3][g] == 3:
                            inp[i+3][g] = 0
                    if inp[i+1][g] == 0 and inp[i+2][g] == 0:
                        inp[i][g] = 1
                        if len(inp)-i >2 and inp[i+3][g] == 3:
                            inp[i+3][g] = 1
                if g > 0 and len(inp[i]) - 1 - g > 0:
                    if inp[i][g-1] == 1 and inp[i][g+1] == 1:
                        inp[i][g] = 0
                    if inp[i][g-1] == 0 and inp[i][g+1] == 0:
                        inp[i][g] = 1
                if i > 0 and len(inp) - 1 - i > 0:
                    if inp[i-1][g] == 1 and inp[i+1][g] == 1:
                        inp[i][g] = 0
                    if inp[i-1][g] == 0 and inp[i+1][g] == 0:
                        inp[i][g] = 1
                g_threes += 1
            if inp[i][g] == 1:g_ones += 1
            if inp[i][g] == 0:g_zeros += 1
            if g_zeros == len(inp[i])/2:
                for l in range(0,len(inp[i])):
                    if inp[i][l] == 3: inp[i][l] = 1
            if g_ones == len(inp[i])/2:
                for l in range(0,len(inp[i])):
                    if inp[i][l] == 3: inp[i][l] = 1
    for k in range(0,len(inp[1])):
        for p in range(0,len(inp)):
            if inp[p][k] == 1:p_ones+=1
            if inp[p][k] == 0:p_zeros+=1
            if p_zeros == len(inp)/2:
                for l in range(0,len(inp)):
                    if inp[p][p] == 3: inp[p][p] = 1
            if p_ones == len(inp)/2:
                for l in range(0,len(inp)):
                    if inp[p][p] == 3: inp[p][p] = 1
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