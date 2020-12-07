from InputReader import readInput


inp = readInput('Input/day6input.txt')

# print(inp)

answers = []
group = set()

for line in inp:
    if (not(line=='')):
        for l in line:
            group.add(l)
    else:
        answers.append(group)
        group = set()
answers.append(group)

# print(answers)
s=0
for a in answers:
    s=s+len(a)

# print("total answers: {}".format(s))

survey = []
group = []
person = set()
i = 0
for line in inp:
    if(not(line=='')):
        for  l in line:
           person.add(l)
        group.append(person)
        person = set()
    else:
        survey.append(group)
        group = []
survey.append(group)



s = 0
for group in survey:
    cross = set()
    for i in range(len(group)):
        if (i == 0):
            cross = set(group[0])
        else:
            cross = cross.intersection(set(group[i]))
    s+=len(cross)

print("number of intersecting groups (where all answered yes) is:{}".format(s))