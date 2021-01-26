from InputReader import readInput 
inp = readInput('Input/s.txt')

print(inp)

def empty_direction(arr, i, j):
    print(i, j)
    _r = len(arr)
    _c = len(arr[0])
    if (i in range( 0, _r) and j in range(0, _c)):
        if arr[i][j] == '#': return 1
        else: return empty_direction(arr, i, j-1) + empty_direction(arr, i,j+1)
    else: return 0
    return 0
    

print(empty_direction(inp, 1, 1))




