#!/usr/local/bin/env python3
"""input_location = 'Input/day1input.txt'
with open(input_location, "r") as f:
    read_data = f.read().splitlines()
    numbers = []
    for n in read_data:
        numbers.append(int(n))
        numbers.sort()
        print(numbers)"""
from InputReader import readInput

numbers =  list(map(int, readInput("Input/day1input1.txt")))
def part1():
        outp = int()
        for s in numbers:
            t = 2020-s
            if (t in numbers):
                print("Found number {} and {}. Their product is: {}".format(s, t, s*t))
                print("took {} iterations".format(numbers.index(s)+1))
                return
part1()

def part2():
    for i in range(0,len(numbers)):
        for j in range (i+1, len(numbers)):
            t = 2020 - numbers[i] - numbers[j]
            if (t in numbers):
                print("Found number {} and {} and {}. Their product is: {}".format(numbers[i], numbers[j], t, numbers[i]*numbers[j]*t))
                print("took {} iterations".format(i))
                return
part2()