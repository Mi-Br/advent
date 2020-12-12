from InputReader import readInput

adapters = [int(x) for x in readInput('Input/day10input.txt')]
adapters.append(0)
adapters.append(max(adapters) + 3)  
adapters.sort()
inp = adapters.copy()

ussage = {}
inn = 0
while adapters:
    a = adapters.pop(0)
    outp = a - inn 
    if outp in ussage: ussage[outp]+=1
    else: ussage[outp]=1
    inn = a
print("part1:{}".format(ussage))


dp = {}
def count_branches(i):
    if(i == len(inp)-1): 
        return 1 
    if (i in dp): 
        return dp[i]
    answ = 0
    for j in range(i+1,len(inp)):
        if (inp[j] - inp[i]) <= 3:
            answ += count_branches(j)
    dp[i] = answ
    return answ
print(count_branches(0))



