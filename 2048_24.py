
import random 
import copy


class game_2048:

    def __init__(self):
        self.game = []
        



        for i in range(4):
            g = [-1]*4
            self.game.append(g)

    

    def print_game(self):
        for i in range(4):
            for j in self.game[i]:
                if j == -1:
                    print("*"+'\t',end='')
                else:
                    print(str(j)+'\t',end='')
            print()

    def add(self):
        while True:
            g = random.randrange(0,16)
            if self.game[g//4][g%4] == -1:
                break

        l = random.random()
        if ( l > 0.1):
            self.game[g//4][g%4] = 2

        else:
            self.game[g//4][g%4] = 4            
        
    def up(self):
        flag = False
        for i in range(1,4):
            for j in range(4):
                stack = []
                if self.game[i][j] != -1:
                    pos = 0
                    
                    for k in range(i-1,-1,-1):
                        if self.game[k][j] != -1:
                            pos = k+1
                            
                            if self.game[k][j] == self.game[i][j]:
                                stack.append(k)
                                self.game[k][j] *= 2
                                self.game[k][j] += 1
                                self.game[i][j] = -1
                                flag = True
                                pos = -1
                            break
                    if pos != -1:
                        self.game[pos][j],self.game[i][j] = self.game[i][j],self.game[pos][j]
                        if pos != i :
                            flag = True

                for e in stack:
                        self.game[e][j] -=1
        return flag
                    


    def down(self):
        flag = False
        for i in range(3,-1,-1):
            for j in range(4):
                stack = []
                if self.game[i][j] != -1:
                    pos = 3
                    
                    for k in range(i+1,4,1):
                        if self.game[k][j] != -1:
                            pos = k-1
                            if self.game[k][j] == self.game[i][j]:
                                stack.append(k)
                                self.game[k][j] *= 2
                                self.game[k][j] += 1
                                self.game[i][j] = -1
                                flag = True
                                pos = -1
                            break
                    
                    if pos != -1:        
                        self.game[pos][j],self.game[i][j] = self.game[i][j],self.game[pos][j]
                        if pos != i:
                            flag = True
                for e in stack:
                        self.game[e][j] -=1
        return flag

    def right(self):
        flag = False
        stack = []
        for i in range(3,-1,-1):
            for j in range(4):
                
                if self.game[j][i] != -1:
                    pos = 3
                    
                    for k in range(i+1,4,1):
                        if self.game[j][k] != -1:
                            pos = k-1
                            if self.game[j][k] == self.game[j][i]:
                                stack.append([k,j])
                                flag = True
                                self.game[j][k] *= 2
                                self.game[j][k] += 1
                                self.game[j][i] = -1
                                pos = -1
                            break
                
                    if pos != -1:
                        self.game[j][pos],self.game[j][i] = self.game[j][i],self.game[j][pos]
                        if pos != i:
                            flag = True
        for e in stack:
            self.game[e[1]][e[0]] -=1
        return flag
    

    def left(self):
        flag = False
        stack = []
        for i in range(1,4):
            for j in range(4):
                
                if self.game[j][i] != -1:
                    pos = 0
                    
                    for k in range(i-1,-1,-1):
                        if self.game[j][k] != -1:
                            pos = k+1
                            if self.game[j][k] == self.game[j][i]:
                                stack.append([k,j])
                                flag = True
                                self.game[j][k] *= 2
                                self.game[j][k] +=1
                                self.game[j][i] = -1
                                pos = -1
                            break
                
                    if pos != -1:
                        self.game[j][pos],self.game[j][i] = self.game[j][i],self.game[j][pos]
                        if pos != i:
                            flag = True
        for e in stack:
            self.game[e[1]][e[0]] -=1
        return flag
def chk(self):
    cnt=0
    for x in range(0,4):
        for y in range(0,4):
            if self.game[x][y] ==-1:
                cnt+=1
    return cnt              
def chhn (self,lst):
	a2048=0
	a1024=0
	a512=0
	a256=0
	a128=0
	for x in range(0,4):
		for y in self.game[x]:
			if y ==2048:
				a2048=1
			if y ==1024:
				a1024=1
			if y==512:
				a512=1		
			if y ==256:
				a256=1
			if y ==128:
				a128=1
	lst.append(a2048)
	lst.append(a1024)
	lst.append(a512)
	lst.append(a256)
	lst.append(a128)				
			                
def cal_score(game2,l):
    score = 0
    num=[16,15,14,13,9,10,11,12,12,11,10,9,13,14,15,16]
    for i in range(0,16):
        
        if game2.game[i//4][i%4]==-1:
            score = score +  16*(16**(4-l))
        else:
                score = score + ((num[i]))*12*(game2.game[i//4][i%4]**chk(game2))
            #print((16-i)*10*game2.game[i//4][i%4],i,game2.game[i//4][i%4])
    return score

def check(game,currpath,maxscore,level):
    global maxpath
    if level == 3:
        return
    
    
    
    currpath.append("w")
    game2 = copy.deepcopy(game)
    
    game2.up()
    score = cal_score(game2,level)
    
    
    if score > maxscore[0] :
        maxscore[0] = score
        maxpath = currpath[:]
    #print('\n\n')
    #print("w",maxscore,score,maxpath,currpath,level)
    #game2.print_game()
    check(game2,currpath,maxscore,level+1)
    currpath.pop(-1)

    currpath.append("a")
    #print(maxpath,"wtf")
    game2 = copy.deepcopy(game)
    game2.left()
    score = cal_score(game2,level)
    
    
    if score > maxscore[0] :
        maxscore[0] = score
        maxpath = currpath[:]
    #print('\n\n')
    #print("a",maxscore,score,maxpath,currpath,level)
    #game2.print_game()
    check(game2,currpath,maxscore,level+1)
    currpath.pop(-1)

    currpath.append("s")
    game2 = copy.deepcopy(game)

    game2.down()
    score = cal_score(game2,level)
   
    if score > maxscore[0] :
        maxscore[0] = score
        maxpath = currpath[:]
    #print('\n\n')
    #print("s",maxscore,score,maxpath,currpath,level)
    #game2.print_game()
    check(game2,currpath,maxscore,level+1)
    currpath.pop(-1)

    currpath.append("d")
    game2 = copy.deepcopy(game)
    game2.right()
    score = cal_score(game2,level)
    
    if score > maxscore[0] :
        maxscore[0] = score
        maxpath = currpath[:]
    #print('\n\n')
    #print("d",maxscore,score,maxpath,currpath,level)
    #game2.print_game()
    check(game2,currpath,maxscore,level+1)
    currpath.pop(-1)

        



g = game_2048()
g.add()
g.print_game()


"""
while True:
    j = input()
    
    if j == 'w':
        o = g.up()
    elif j == 's':
        o = g.down()
    elif j == 'a':
        o = g.left()
    elif j == 'd':
        o = g.right()
    if o == True:
        g.add()
    else:
        print("invalid")
    g.print_game()
"""
def count(l):
    c = 0
    for i in range(4):
        for j in range(4):
            if l[i][j] == -1:
                c+=1
    return c
    
while True:
    maxpath = []
    c = count(g.game)
    if c <= 6:
        l = 0
    else:
        l = 0
    check(copy.deepcopy(g),[],[0],l)
    
    j = maxpath[0]

    if j == 'w':
        o = g.up()
    elif j == 's':
        o = g.down()
    elif j == 'a':
        o = g.left()
    elif j == 'd':
        o = g.right()
    if o == True:
        g.add()
    else:
        print("invalid")
        o = g.up() or g.left() or g.right() or g.down()
        print("wtfff")
        if not o:
            break
        else:

            g.add()

    g.print_game()
    print("\n\n")
print("Game over")
lst=[]
chhn(g,lst)
f=open("stats.txt","a")
if lst[0]==1:
	f.write("10000")
elif lst[1]==1:
	f.write("01000")
elif lst[2]==1:
	f.write("00100")		
elif lst[3]==1:
	f.write("00010")
elif lst[4]==1:
	f.write("00001")
f.write("\n")
f.close()

