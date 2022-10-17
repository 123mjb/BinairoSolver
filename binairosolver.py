def solve(inp:list[list[int]]):
    for i in range(0,len(inp)):
        for g in range(0,len(inp[i])):
            if inp[i][g] == 3:
                if len(inp[i])-g >1:
                    if inp[i][g+1] == 1 and inp[i][g+2] == 1:
                        inp[i][g] = 0
                        if len(inp[i])-g >2 and inp[i][g+3] == 3:
                            inp[i][g+3] = 0
                    if inp[i][g+1] == 0 and inp[i][g+2] == 0:
                        inp[i][g] = 1
                        if len(inp[i])-g >2 and inp[i][g+3] == 3:
                            inp[i][g+3] = 1
                if len(inp)-i >1:
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
                if i > 1 and len(inp) - 1 - i > 0:
                    if inp[i-1][g] == 1 and inp[i+1][g] == 1:
                        inp[i][g] = 0
                    if inp[i-1][g] == 0 and inp[i+1][g] == 0:
                        inp[i][g] = 1
    return inp
def printer(output:list[list[int]]):
    printout=""
    for i in range(0,len(output[0])):
        for g in range(0,len(output)):
            printout += str(output[g][i])
        printout += "\n"
    print(printout)


printer(solve([
    [3,1,3,3],
    [1,0,0,1],
    [1,0,0,3],
    [3,1,3,3]
]))