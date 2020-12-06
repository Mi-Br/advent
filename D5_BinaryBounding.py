import math
import re
from InputReader import readInput

# def take_upper_half(n1,n2):
#     return n1/n2


def get_upper_half(x,y):
    return (math.ceil((x+y)/2), y)

def get_lower_half(x,y):
    return (x, math.floor((x+y)/2))

operations = {
    'F' : lambda n1,n2 : get_lower_half(n1,n2),
    'B' : lambda n1,n2 : get_upper_half(n1,n2),
    'R' : lambda n1,n2 : get_upper_half(n1,n2),
    'L' : lambda n1,n2 : get_lower_half(n1,n2),
}


def scan_letters(inp, rng):
    _start, _end  = rng
    for c in inp:
        # print('Letter {} range from: {}  to: {}'.format(c, _start, _end ))
        _start, _end = operations.get(c, lambda x: False)( _start, _end)

    if (inp[-1] == "F" or inp[-1] == "L"): 
        return _start
    return _end

# print(scan_letters('FBFBBFF', (0,127)))
# print(scan_letters('RLR', (0,7)))


def get_seat_ID (inp):
    row_str = re.findall(r'([FB]+)', inp)
    col_str = re.findall(r'([RL]+)', inp)
    if(row_str and col_str):
        row_id  = scan_letters(row_str[0], (0,127))
        col_id  = scan_letters(col_str[0], (0,7))
        seat_id = row_id * 8 +col_id
        # print("{}: row {}, column {}, seat ID {}.".format(inp, row_id, col_id, seat_id))
        return seat_id


part1_inp = readInput('Input/day5input.txt')
max_id = 0
codes = []
for code in part1_inp:
    _id = get_seat_ID(code)
    # print(_id)
    if(max_id < _id): max_id = _id
    codes.append(_id)
print("Max id for part 1 is: {}".format(max_id))


codes.sort()
for i in range(36,945):
    if (not(i in codes)): print ("missing seat is : {}".format(i))

# get_seat_ID ('FBFBBFFRLR')
