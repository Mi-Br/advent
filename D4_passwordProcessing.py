from InputReader import readInput
import re


input = readInput("Input/day4input.txt")
passports_data = []
passport = {}
i = 0
# print(input)
for entry in input:
    
    if not (entry == ""):
        line = re.findall(r'(\w+):([\w#]+)', entry)
        for pair in line:
            k,v = pair
            passport[k]=v
    elif entry =="":
        passports_data.append(passport) #add object to list
        passport = {} #reset object
passports_data.append(passport) #putting last passport to the data list


mand = ["byr","iyr","eyr","hgt","hcl","ecl","pid"]
opt = ["cid"]

def validate_passport(p, mand, opt):
    # print("checking passport {} ......".format(p))
    if len(p.keys()) < len(mand):      
        # print("failed mand field count check. Nr of keys: {} Mand: {} ".format(len(p.keys()), len(mand)))
        return False
    for m in mand:
        if not (m in p.keys()):
            # print("failed mandatory field presence. field {} not in {}".format(m, p.keys()))
            return False
    # print("password is OK")
    return True
 
# byr (Birth Year) - four digits; at least 1920 and at most 2002.
def byr(x):
    test = re.match(r'^\d{4}$',x)
    if(test):
        return int(x)>=1920 and int(x)<=2002
    return False

#eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
def eyr(x):
    test = re.match(r'^\d{4}$',x)
    if(test):
        return int(x)>=2020 and int(x)<=2030
    return False

#iyr (Issue Year) - four digits; at least 2010 and at most 2020.
def iyr(x): 
    test = re.match(r'^\d{4}$',x)
    if(test):
        return int(x)>=2010 and int(x)<=2020
    return False

#hgt (Height) - a number followed by either cm or in:
    #If cm, the number must be at least 150 and at most 193.
    #f in, the number must be at least 59 and at most 76.
def hgt(x): 
    test = re.findall(r'^(\d{3})cm$',x)
    if(test):
        return int(test[0])>=150 and int(test[0])<=193
    test = re.findall(r'^(\d{2})in$',x)
    if(test):
        return int(test[0])>=59 and int(test[0])<=76
    return False

#hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
def hcl(x):
    test = re.match(r'^#[0-9a-f]{6}',x)
    if(test):
        return True
    return False
    
#ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
def ecl(x):
    test = re.match(r'^(amb|blu|brn|gry|grn|hzl|oth)$', x)
    if(test):
        return True
    return False

#pid (Passport ID) - a nine-digit number, including leading zeroes.
def pid(x):
    test = re.match(r'^\d{9}$',x)
    if(test):
        return True
    return False

#cid (Country ID) - ignored, missing or not.
def cid(x):
    return True

validations = {
    'byr': lambda x: byr(x),
    'iyr': lambda x: iyr(x),
    'eyr': lambda x: eyr(x),
    'hgt': lambda x: hgt(x),
    'hcl': lambda x: hcl(x),
    'ecl': lambda x: ecl(x),
    'pid': lambda x: pid(x),
    'cid': lambda x: cid(x),
}

scanned_passports = [p for p in  passports_data if validate_passport(p,mand,opt)]
print("Number of scanned passports is: {}".format(len(scanned_passports)))

validated = []
for p in scanned_passports:
    print("scanning {}".format(p))
    # for k,v in p.items():
    #     print(validations.get(k, lambda x: False)(v))
    valid = all(validations.get(k, lambda x: False)(v) for (k, v) in p.items())
    if(valid): validated.append(p)

print("Number of validated passports is: {}".format(len(validated)))
