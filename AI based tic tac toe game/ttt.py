import random
def pos(n):
    l=[]
    if(n==1):
        l=[0,0]
    elif(n==2):
        l=[0,1]
    elif(n==3):
        l=[0,2]
    elif(n==4):
        l=[1,0]
    elif(n==5):
        l=[1,1]
    elif(n==6):
        l=[1,2]
    elif(n==7):
        l=[2,0]
    elif(n==8):
        l=[2,1]
    elif(n==9):
        l=[2,2]
    return l
class TTT:
    board=[]
    pc='N'
    cc='N'
    def __init__(self,x):
        self.pc=x;
        for i in range(3):
            c=['N','N','N']
            self.board.append(c)
        if(self.pc=='x'):
            self.cc='o'
        else:
            self.cc='x'
    def show(self):
        for i  in range(3):
            for j in range(3):
                if(self.board[i][j]=='N'):
                    print('_',end="")
                else:
                    print(self.board[i][j],end="")
                    
                print('|',end="")
            print()
    def pm(self):
        while(True):
            k=int(input('enter position-'))
            l=pos(k)
            if(self.board[l[0]][l[1]]=='N'):
                self.board[l[0]][l[1]]=self.pc
                break
            else:
                print('This position is occupied')
    def win(self,b,x):
        if(b[0][0]==b[1][1] and b[2][2]==b[1][1] and b[0][0]==x and b[2][2]==x ):
            return True
        if( b[0][0]==b[0][1] and b[0][2]==b[0][1] and b[0][0]==x and b[0][2]==x ):
            return True
        if(b[0][0]==b[1][0] and b[2][0]==b[1][0] and b[0][0]==x and b[1][0]==x ):
            return True
        if(b[0][1]==b[1][1] and b[2][1]==b[1][1] and b[0][1]==x and b[1][1]==x):
            return True
        if(b[0][2]==b[1][2] and b[2][2]==b[1][2] and b[0][2]==x and b[2][2]==x):
            return True
        if(b[1][0]==b[1][1] and b[1][2]==b[1][1] and b[1][0]==x and b[1][2]==x):
           # print('f')
            return True
        if( b[2][0]==b[2][1] and b[2][2]==b[2][1] and b[2][0]==x and b[2][2]==x):
            return True
        if(b[0][2]==b[1][1] and b[2][0]==b[1][1] and b[0][2]==x and b[2][0]==x):
            return True
        return False
    def c_m(self):
        c=[]
        b=[]
        #print('C m')
        for i in range(3):
            ro=[]
            for j in range(3):
                if(self.board[i][j]=='N'):
                    a=[i,j]
                    c.append(a)
                ro.append(self.board[i][j])
            b.append(ro)
        k=[]
        flag=False
        cdho=0
        for i in range(len(c)):
            cdho+=1
            a=c[i]
            b[a[0]][a[1]]=self.cc
            if(self.win(b,self.cc)==True):
               # print(a)
                #print(cdho,'ete')
                flag=True
                k=c[i]
                break
            b[a[0]][a[1]]='N'

        if(flag):
            
            self.board[k[0]][k[1]]=self.cc
            return
        for i in range(len(c)):
            a=c[i]
            b[a[0]][a[1]]=self.pc
            if(self.win(b,self.pc)==True):
                flag=True
                k=c[i]
                break        
            b[a[0]][a[1]]='N'
        if(flag):
            self.board[k[0]][k[1]]=self.cc
            return

        cor=[[0,0],[0,2],[2,0],[2,2]]
        for i in cor:
            if(i in c):
               self.board[i[0]][i[1]]=self.cc
               return
        if(self.board[1][1]=='N'):
            self.board[1][1]=self.cc
            return
        l=random.randint(0,len(c)-1)
        k=c[l]
        self.board[k[0]][k[1]]=self.cc
    def p_win(self):        
        return self.win(self.board,self.pc)
    def c_win(self):        
        return self.win(self.board,self.cc)
    #win(self.board,self.cc)
    def draw(self):
        k=True
        for i  in range(3):
            for j in range(3):
                if(self.board[i][j]=='N'):
                    k=False
                    break
        return k
p='N'
while True:
    p=input('Enter x or o-')
    if(p=='o' or p=='x'):
        break
    else:
        print('Not a valid option')
t=TTT(p)
a=random.randint(0,1)
if(a==0):
    print('Computer  will go first')
    
    while(True):
        
        t.c_m()
        t.show()
        if(t.c_win()):
            print('You lost')
            break
        
        if(t.draw()):
            t.show()
            print('match  drawn')
            break
        t.pm()
        if(t.c_win()):
            t.show()
            print('You won')
            break
        if(t.draw()):
            t.show()
            print('match  drawn')
            break
else:
    print('Player will go first')
    while(True):
        t.show()
        t.pm()
        if(t.p_win()):
            print('You won')
            break
        if(t.draw()):
            t.show()
            print('match  drawn')
            break
        t.c_m()
        if(t.c_win()):
            t.show()
            print('You lost')
            break
        if(t.draw()):
            t.show()
            print('match  drawn')
            break
