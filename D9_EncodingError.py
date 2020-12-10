from InputReader import readInput
inp = [int(x) for x in readInput('Input/day9input.txt')]

def number_appears(arr, nr):
    for s in arr:
        test = nr - s
        if not(test == s) and (test in arr):
            return (test, s)
    return False

j=0
cont_num = 0 
for i in range (25, len(inp)):
    seq = inp[j:i]
    num = inp[i]
    if number_appears(inp[j:i],num):
        a,b = number_appears(inp[j:i],num)
        # print("{} is a sum of nr {} and {}  in sequence {}".format(num,a,b,seq))
        j+=1
    else:
        # print("{} is not matching sum of any previous numbers {}".format(num,seq))
        cont_num = num
        break

# print(num)
# print(inp.index(num))
# print(sum(inp[0:2]))

mn = 0
mx = 0 
l = 0
while mn == 0 and mx ==0:
    for i in range(0, inp.index(num)):
        seq = inp[i:i+l]
        print(seq)
        if sum(seq) == num:
            print ("{} sum is {}".format(seq,num))
            mn = min(seq)
            mx = max(seq)
            print(mn," ",mx, "=", mn+mx) 
            break
    l+=1

