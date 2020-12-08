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




contains_gold_bag = set()
seen = []
while len(seen) < len(bag_collection):
    for bag in bag_collection:
        if(bag.can_hold('shiny gold')):
            contains_gold_bag.add(bag.color)


def get_bag_set(bag, collection):
    seen = set()
    found= set()
    for b in collection:
        if (b.can_hold_count(bag.color)):
            found.add(bag)
        seen.add(bag)

    


def scan_bags(bag, set):
    seen = set()
    


# print(bag_collection[0].can_hold('muted yellow'))
# print(bag_collection[0].can_hold(bag_collection[3].color))









