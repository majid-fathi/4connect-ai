from game import GameBoard
class Player:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_drop_input(self, game_map):
        pass


class Person(Player):
    def __init__(self, name, number):
        super().__init__(name, number)

    def get_drop_input(self, game_map):
        raise Exception("get_drop_input() called from Person class")


class AIPlayer(Player):
    def __init__(self, name, number):
        super().__init__(name, number)


    def check_Opponentـwin(self,game_map,player_num) :


        #vertical                   
        for x in range(len(game_map[0])):
            
            for y in range(len(game_map) -2):
                if game_map[y][x] != player_num:
                    continue
                elif game_map[y+1][x] == player_num and game_map[y+2][x] == player_num :
                    print("ddddddddddddddd")
                    
                    if  y-1>0:
                        if game_map[y-1][x]==0:
                            return x
                       
                        


                        



        #horizantal

        for x in range(len(game_map)):
            
            for y in range(len(game_map[0]) -3):
                if game_map[x][y] != player_num:
                    continue
                elif game_map[x][y+1] == player_num and game_map[x][y+2] == player_num :
                    if y-1>-1 :
                        if x==5 and game_map[x][y-1] == 0:
                            return y-1
                        
                        elif x<5 and game_map[x+1][y-1]!=0 and game_map[x][y-1]==0:
                            return y-1
                    if y+3<7:

                        if x==5 and game_map[x][y+3] == 0:
                            return y+3
                        
                        elif x<5 and game_map[x+1][y+3]!=0 and game_map[x][y+3]==0:
                            return y+3                        


        # check Diagonal
        for x in range(len(game_map[0]) - 3):
            for y in range(len(game_map) - 2):
                if game_map[y][x] != player_num:
                    continue
                elif game_map[y+1][x+1] == player_num and game_map[y+2][x+2] == player_num :

                    if y+3<5 and x+3>7:
                        if game_map[y+4][x+3]!=0 and game_map[y+3][x+3]==0 :
                            return x+3
                        

                    if y+3==5 and x+3<7:
                        if game_map[y+3][x+3]==0:
                            return x+3

                    if y-1>=0 and x-1>=0:
                        if game_map[y][x-1]!=0 and game_map [y-1][x-1]==0:
                            return x-1
                          
                                        
        for x in range(3, len(game_map[0])):
            for y in range(len(game_map) - 2):
                if game_map[y][x] != player_num:
                    continue
                elif game_map[y+1][x-1] == player_num and game_map[y+2][x-2] == player_num :


                    if y+3<5 and x-3>=0:
                        if game_map[y+4][x-3]!=0 and game_map[y+3][x-3]==0 :
                            return x-3
                        

                    elif y+3==5 and x-3>=0:
                        if game_map[y+3][x-3]==0:
                            return x-3

                    if y-1>=0 and x-1>=0:
                        if game_map[y][x-1]!=0 and game_map [y-1][x-1]==0:
                            return x-1                                           
                                                   








        return 0  

        


    def win_check_AI(self,map,player_num,game_map1,column_num):
        flag=0

        if game_map1[0][column_num] == 0:
            for c in range(5,0,-1):
                if game_map1[c-1][column_num]==0 and game_map1[c][column_num]==0 :
                    flag=1
                    break
            
        else :
            return 1
        if flag==0:
            return 0
            
        map[c-1][column_num]=player_num           

        gm = map

        # check horizontal
        for row in gm:
            for i in range(len(row) - 3):
                if row[i] != player_num:
                    continue
                elif row[i+1] == player_num and row[i+2] == player_num and row[i+3] == player_num:
                    return 1

        # check vertical
        for x in range(len(gm[0])):
            for y in range(len(gm) - 3):
                if gm[y][x] != player_num:
                    continue
                elif gm[y+1][x] == player_num and gm[y+2][x] == player_num and gm[y+3][x] == player_num:
                    return 1

        # check Diagonal
        for x in range(len(gm[0]) - 3):
            for y in range(len(gm) - 3):
                if gm[y][x] != player_num:
                    continue
                elif gm[y+1][x+1] == player_num and gm[y+2][x+2] == player_num and gm[y+3][x+3] == player_num:
                    return 1

        for x in range(3, len(gm[0])):
            for y in range(len(gm) - 3):
                if gm[y][x] != player_num:
                    continue
                elif gm[y+1][x-1] == player_num and gm[y+2][x-2] == player_num and gm[y+3][x-3] == player_num:
                    return 1

        return 0
        











            

    def get_drop_input(self, game_map):

        if self.number==1:
            Opponent=2
            
        else :
            Opponent=1


        print(Opponent)
        print(self.number)    





        res1=self.check_Opponentـwin(game_map,self.number)
        res=self.check_Opponentـwin(game_map,Opponent)

        if res1!=0:
            return res1


        if res!=0:
            return res

                                       
                    










              
 
#3

        map2=[[0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0]] 
        for x in range(len(game_map)):
            for y in range(len(game_map[0])):
                map2[x][y]=game_map[x][y]
                                    
        

        
        check_list=[3,4,2,5,1,0,6]
        for x in range(len(check_list)):
            print("aaavvvvvvvaaaaaaal")
            print(x)
            if self.win_check_AI(map2,1,game_map,check_list[x])==0:
                return check_list[x]
           
            else :
                print("pppppppppppa")

        for x in range(len(check_list)):
            
            if game_map[0][check_list[x]]==0:
                print(check_list[x])
                print("gfgfg")
                return 0
             
        return 1    
            


   