from InputReader import readInput
inp = readInput('Input/day11input.txt') 

grid = []
for line in inp:
    seats = []
    for s in line:
        seats.append(s)
    grid.append(seats)            
inp = grid

def empty_seat(inp, i, j):
        def count_occupied_around (inp, i, j):
            occ = 0
            for ii in range (i-1,i+2):
                for jj in range (j-1,j+2):           
                    if (ii in range(0,len(inp))  and jj in range(0, len(inp[0]))): 
                       if (not(ii == i) and not (jj ==  j)):
                            if (inp[ii][jj] == "#"): 
                                occ +=1
            return occ
        if count_occupied_around(inp, i, j) >= 4:
            return False
        return True


class Grid():
    def __init__(self, inp):
        self.grid = []
        for line in inp:
            seats = []
            for s in line:
                seats.append(s)
            self.grid.append(seats)            
    
    def log(self):
        head = "\t"
        for c in range(len(self.grid[0])):
            head += str(c) + " "
        print (head + "\n")
        for r in self.grid:
            st = ""
            for c in r:
                st = st + c + " "
            print("{} \t {}".format(self.grid.index(r), st))
        print ("\n")

    def model(self,inp):
        i = 0
        for r in inp:
            j=0
            for c in r:
                if not (c == '.'): 
                    if (empty_seat(inp, i, j)):
                        self.grid[i][j] = "#"
                    else:
                        self.grid[i][j] = "L"
                j+=1
            i+=1
        

G = Grid(inp)
G.log()
G.model(inp)
G.log()
G.model(G.grid)
G.log()
G.model(G.grid)
G.log()
    # build internal state grid 
    # 
    # 
    # occupy each cell
    # 
    # 
    # export grid as outp 



# class seat():
#     def __init__(self, state, r, c, g):
#         self.state  = state
#         self.r = r
#         self.c = c
#         self.G = g
    
#     def model(self, G_copy):
#         if(not (self.state == '.')): 
#             r = self.r.rid 
#             c = self.c.cid
#             occupied = 0 
#             for i in range (c-1, c+1):
#                 for j in range(r-1, r+1):
#                     if not( j == c and i == r):
#                         occupied = occupied + G_copy.occupied_count(j, i) 
#             if (occupied>=4): self.state = "L"
#             else: self.state = "#"
    

            
# class row():
#     def __init__(self, rid):
#         self.rid = rid
#         self.seats= []
#     def log(self):
#         content = " \t"
#         for s in self.seats:
#             content += str(s.state) + " " 
#         return content
    
# class column():
#     def __init__(self, cid):
#         self.cid = cid
#         self.seats= []
# # TODO: Diagonale

# class grid():
#     def __init__ (self, r, c):
#         self.rows    = []
#         self.cols    = []
#         for j in range (r):
#             self.rows.append(row(j))
#         for j in range (c):
#             self.cols.append(column(j))
    
#     def occupied_count(self, r,c):
#         if (r not in range(len(self.rows))): return 0 
#         if (c not in range(len(self.cols))): return 0 
#         if (self.rows[r].seats[c].state == '.'): return 0
#         if (self.rows[r].seats[c].state == 'L'): return 0
#         if (self.rows[r].seats[c].state == '#'): return 1
#         return False

#     def log(self):
#         head = "\t"
#         for c in range(len(self.cols)):
#             head += str(c) + " "
#         print (head + "\n")
#         for r in self.rows:
#             if (not r is None):
#                 pass
#                 print("{} {}".format(r.rid, r.log()))
#         print ("\n")
    
#     def complete_round(self):
#     #   Create deep copy of the Grid
#         G_copy = grid(len(self.rows), len(self.cols))
#         r = 0
#         for _ in self.rows:
#             c = 0
#             for _ in self.cols:
#                 s = seat(self.rows[r].seats[c].state, G_copy.rows[r], G_copy.cols[c], G_copy)
#                 G_copy.rows[r].seats.append(s)
#                 G_copy.cols[c].seats.append(s)
#                 c+=1
#             r+=1
#     #   Modify stated of the grid based on the deep copy 

#         for r in self.rows:
#             for s in r.seats:
#                 s.model(G_copy)



# # Create GRID

# #  number of rows 
# r_count = len(inp[0])
# c_count = len(inp)
# #  number of columns

# G = grid(r_count, c_count)

# r = 0
# for line in inp:
#     c = 0
#     for l in line:
#         s = seat(l, G.rows[r], G.cols[c], G)
#         G.rows[r].seats.append(s)
#         G.cols[c].seats.append(s)
#         c+=1
#     r+=1

# G.log()
# G.complete_round()
# G.log()
# G.complete_round()
# G.log()
