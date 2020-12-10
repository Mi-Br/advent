from InputReader import readInput


inp = readInput('Input/day8input.txt')

instructions = []
for line in inp:
    oper = line.split()[0]
    arg = line.split()[1]
    instructions.append([oper, int(arg)])


#breaks the instruction if i becomes larger than len

step=0
acc = 0
i = 0
#infinite loop is if we step into the seen 

def run_instruction(i, step, acc, instructions):
    visited = set()
    while True:
        if (i in visited):
            print ("infinite loop at {} {} {}".format(i, step, acc))
            return False
        if(i > len(instructions)-1):
            print ("broke out of the loop at :{} {} {}".format(i, step, acc))
            return True
        else:
            visited.add(i)
            oper, arg = (instructions[i][0], instructions[i][1])
            # print(oper,"\t",arg, "\n")
            if oper == 'acc':
                acc+=arg
                i+=1
            if oper == 'jmp':
                i+=arg
            if oper == 'nop':
                    i+=1

# # exchange ONE jmp to nop or nop to jump


# tmp = instructions.copy()
# print(instructions)
# print(tmp)


for i in range(len(instructions)):
    print ("step {}".format(i)) 
    tmp=instructions.copy()
    print(instructions)
    # print(tmp)
    if (instructions[i][0] == 'jmp'):
        tmp[i] = instructions[i].copy()
        tmp[i][0] = 'nop' 
        print(tmp)
        if (run_instruction(0,0,0,tmp)):
            break
    if (instructions[i][0] == 'nop'):
        tmp[i] = instructions[i].copy()
        tmp[i][0] = 'jmp'
        print(tmp)
        if (run_instruction(0,0,0,tmp)):
            break
     
