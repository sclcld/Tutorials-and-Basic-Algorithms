
import os
import time


# [1,]
#  2
# 2
        
class graph:


    def __init__(self, map):

        self.place_holder = "@"
        self.labirynth = [[col for col in row] for row in map]        
        self.set_position()
        self.adjacency_list = {}
        self.adj_compile()
        print("compiled")
        self.show_path()
        self.x_pos = None
    
    def visualize(self):

        for row in self.labirynth:

            print("".join(str(col) for col in row))
        print("\n")
    
    def set_position(self):

        for r_i, row in enumerate(self.labirynth):

            for c_i, col in enumerate(row):

                if col == "@":

                    self.current_pos = (r_i, c_i)
                    self.current_x = r_i
                    self.current_y = c_i
    print
    
    def adj_compile(self):
        
        research_cords = [(0,-1), (-1, 0), (0, 1), (1, 0)]
        queue = [self.current_pos]
        visited = set()
        
        temp_path = []
        
        while queue:
            
            current = queue.pop(0)
            cur_x, cur_y = current
            neigs = []
            for st_x, st_y in research_cords:

                new_x = cur_x + st_x
                new_y = cur_y + st_y 
                in_row_range = 0 <= new_x < len(self.labirynth)
                
                if in_row_range \
                    and 0 <= new_y < len(self.labirynth[new_x])\
                    and self.labirynth[new_x][new_y] != "#"\
                    and (new_x, new_y) not in visited :

                    
                    
                    
                    if self.labirynth[new_x][new_y] == "X":
                        
                        self.x_pos = (new_x,new_y)
                        
                        return True
                    
                    visited.add((new_x, new_y))
                    temp_path.append((new_x, new_y))

                    neigs.append((new_x, new_y))    
           
            for neig in neigs:        
                
              
                queue.append(neig)
                
            if len(neigs) > 1 or len(neigs) == 0:


                if current not in self.adjacency_list:

                    self.adjacency_list[current] = []
                self.adjacency_list[current] = [*temp_path, current]
                
                temp_path = []
                
            temp_path.append(neig) 

        
    
    
    def show_path(self):


        for x in self.adjacency_list.keys():

            for y in self.adjacency_list[x]:
                
                self.labirynth[y[0]][y[1]] = "@"
                print("\n\n")
                self.visualize()
                
                time.sleep(.1)
                os.system("clear")
        
        if self.x_pos:
                    print("\n\n\n")
                    self.visualize()
                    print(f"X found at position {self.x_pos}")
                    return True        
        print("X not found")
        return False        

""" 
                    0123456789112355
                    ################0",
                    ################1",
                    #####   ########2",
                    ####### #### ###3",
                    #####   #### ###4",
                    ####### #### ###5",
                    ####### #### ###6",
                    #####        ###7",
                    ####### ########8",
                    #######@########9",
                    ################10"
"""   
    
prova1= [       
                
                
                "################",
                "################",
                "####### #### ###",
                "#####X  #### ###",
                "####### #### ###",
                "####### #### ###",
                "#####        ###",
                "####### ########",
                "#######@########",
                "################"               
]

prova2 = [
           "###############",
           "#             #",
           "#      X      #",
           "#         @   #",
           "#             #",
           "###############"
]

prova3 = [
            "                      X",
            "                       ",
            "                       ",
            "                      @"]

prova4 = [
            "#########################################",
            "######          ####                  ##",
            "##############  ###################### ##",
            "##############                         ##",
            "# ##########    #########################",
            "# ########## ############################",
            "#       ####    #########################",
            "# ##### ####### #########################",
            "# #####         #########################",
            "# #######################################",
            "#                                     ###",
            "##################################### ###",
            "######                                ###",
            "###### ##### ######################    ##",
            "###### #####        #############  ##  ##",
            "###### ############ ############  ###  ##",
            "###################              #####@##",
            "#########################################"
]

b = graph(  prova4
                )                