from InputReader import readInput
inp = readInput('Input/day11input.txt') 
# print (inp)
def log(a):
    print ("_" * 10)
    for x in (a):
        print(x)
    print ("_" * 10)

_r = len(inp)
_c = len(inp[0])


def empty_seat(arr, i, j, limit):
    occupied_count = 0
    # print("is seat {}:{} empty?".format(i,j))
    for ii in range (i-1, i+2):
        for jj in range (j-1, j+2):
            if (not i == ii or not j == jj):
                if ii in range (0, _r) and jj in range (0, _c):
                    # print('checking{}:{}- value {}'.format(ii,jj,arr[ii][jj])) 
                    if arr[ii][jj] == '#':
                        occupied_count +=1
    # print('seat {} {} is occupied by {} adjasent seats'.format(i,j,occupied_count))                        
    if occupied_count >=limit: 
        return False
    else:     
        return True

def simulate_seats(ar): 
    outp = []
    for i in range(0, len(ar)):
        outp.append([])
        seat = ""
        for j in range(0, len(ar[i])):
            if ar[i][j] == '.': seat = seat+"."
            else: 
                if ar[i][j] == 'L' and empty_seat(ar, i, j, 1):
                    seat = seat + '#' 
                elif ar[i][j] == '#' and not empty_seat(ar, i, j, 4):
                    seat = seat + "L"
                else: 
                    seat = seat + ar[i][j]
        outp[i] = seat
    return outp


def run_continuously(inp, ctn = 0):
    outp = simulate_seats(inp)
    notChanging = True
    for i in range (0,_r):
        notChanging = notChanging and (outp[i] == inp[i])
    if notChanging: 
        print ('stopped chaning after {} iterations'.format(ctn))
        log(inp)
        log(outp)
        total_seats = 0
        for x in inp:
            for y in x:
                if y == '#': total_seats+=1
        print(total_seats)
        return ctn
    else:
        ctn+=1
        run_continuously(outp, ctn)

print(run_continuously(inp))




