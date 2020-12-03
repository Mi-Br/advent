from InputReader import readInput

slope = readInput("Input/day3input.txt")
#print(slope_pattern[0])

height = len(slope)

# helpers

# .............#...#....#.....##.

# evaluate if we reached bottom yet
def count_trees_downSlope(s, l):
    step = s
    trees = 0
    # height = 30
    for h in range(0+l,height,l):
        # move down the slope   
            # print ("level {} step {} value {}".format(h, step +1,slope[h][step]))
            # print(step)
            if slope[h][step] == "#":
                trees +=1
            if (step +  s  < len(slope[h])):
                step +=s
                # print("moved to {} step {}".format(h,step))
            else:
                step = (step + s) - len(slope[h])
                # print("Stepped over, moving to {} step {}".format(h+1,step))
            
    # print("Number of trees on the path is: {}".format(trees))
    return trees


print(count_trees_downSlope(1,1))
print(count_trees_downSlope(3,1))
print(count_trees_downSlope(5,1))
print(count_trees_downSlope(7,1))
print(count_trees_downSlope(1,2))

print(count_trees_downSlope(1,1)* count_trees_downSlope(3,1)* count_trees_downSlope(5,1)* count_trees_downSlope(7,1)* count_trees_downSlope(1,2))