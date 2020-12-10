from InputReader import readInput
import re


class bag():
    def __init__(self, color):
        self.color = color
        self.contents = {}

    def add_child(self, count, bag):
        if (not (bag in self.contents)): 
            self.contents[bag.color] = count 
    
    def print_contents(self):
        if (len(self.contents)) > 0:    
            print("A {} can hold".format(self.color))
            for b,count in self.contents.items():
                print("\t {} :  {}".format(count, b))
        else:
            print("A {} contains no futher bags".format(self.color))
    
    def can_hold_count(self,color):
        if (color in self.contents.keys()):
            return self.contents[color]
        return False

bag_collection = []

inp = readInput('Input/day7input.txt')
for line in inp:
    section = line.split(',')
    regx = re.findall(r'^(\w+ \w+) bag', section[0])
    parent = bag(regx[0])
    
    for i in range(0, len(section)):
        test = re.findall(r'(\d{1,2}) (\w+ \w+)', section[i])
        if(test):
            k, v = test[0]
            parent.add_child(k, bag(v))
    bag_collection.append(parent)



# # PART 1
# visited = set()
# def scan_bags(visited, bag_collection, srch):    
#     if srch not in visited:
#         print(srch)
#         visited.add(srch)
#         for bag in bag_collection:
#             if(bag.can_hold_count(srch)):
#                 scan_bags(visited, bag_collection, bag.color)

# scan_bags(visited, bag_collection, 'shiny gold')
# print("shiny gold can fit in {} bags".format(len(visited)-1))

def count(name):
    print("searching for: " + name)
    for bag in bag_collection:
        if bag.color == name:
            i = 1
            print("{} bag contains: ".format(name))
            for k,v in bag.contents.items():
                print("\t {} {} bag".format(v,k))
                i = i + int(v) * count(k)
            return i
    return 0

print(count('shiny gold')-1)
# print(count('dark red'))
# print(bag_collection[0].can_hold('muted yellow'))
# print(bag_collection[0].can_hold(bag_collection[3].color))









