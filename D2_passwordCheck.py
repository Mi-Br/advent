#!/usr/local/bin/env python3

def pwd_policy_OLD_check(t):
         if(t):
            _from, _to, _char, sequence = t[0]
            if (sequence.count(_char) >= int(_from) and sequence.count(_char) <= int(_to)):
             #  print ("Password ok")
                return True
            return False

def pwd_policy_NEW_check(t):
         if(t):
            _from, _to, _char, sequence = t[0]
            _from = int(_from)-1 # To match array index starting at 0
            _to = int(_to)-1     # To macth array index starting at 0
            print (_from, _to, _char, sequence, len(sequence))
            if not (sequence[_from] == _char and sequence[_to] == _char):
                if (sequence[int(_from)] == _char or sequence[_to] == _char):
                    return True
                #  print ("Password ok")

from InputReader import readInput
import re

input_file = readInput("Input/day2input.txt")
valid_passwords_old = []
valid_passwords_new = []
for pwd in input_file:
    test = re.findall(r'(\d+)-(\d+) (\w): (.*)', pwd)
    if pwd_policy_OLD_check(test):
        valid_passwords_old.append(pwd)
    if pwd_policy_NEW_check(test):
        valid_passwords_new.append(pwd)

    


print("valid OLD password count is:{}".format(len(valid_passwords_old)))
print("valid NEW password count is:{}".format(len(valid_passwords_new)))
   

