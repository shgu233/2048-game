import random 
def start_game():
    mat=[]
    for i in range(4):
        mat.append([0]*4)
    return mat 

def add_new_2(mat):
    
    r= random.randint(0,3)
    c= random.randint(0,3)
    while (mat[r][c]!=0):
        r=random.randint(0,3)
        c=random.randint(0,3)
    mat[r][c]=2
    
def get_current_state(mat):
    
    for i in range(4):
        for j in range(4):
            if (mat[i][j]==2048):
                return 'WON'
            
    for i in range(4):
        for j in range(4):
            if (mat[i][j]==0):
                return 'GAME NOT OVER'
            
    for i in range(3):
        for j in range(3):
            if(mat[i][j]==mat[i][j+1] or mat[i][j]==mat[i+1][j]):
                return 'GAME NOT OVER'
            
    for j in range(3):
        if mat[3][j]==mat[3][j+1]:
            return 'GAME NOT OVER'
                    
    for i in range(3):
        if mat[i][3]==mat[i+1][3]:
            return 'GAME NOT OVER'   
    return "LOST"

def compress(mat):
    change=False
    
    new_mat=[]
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos=0
        for j in range(4):
            if mat[i][j]!=0:
                new_mat[i][pos]=mat[i][j]
                if j!=pos:
                    change=True
                pos+=1
    return new_mat,change
            
def merge(mat):
    change=False
    for i in range(4):
        for j in range(3):
            if mat[i][j]==mat[i][j+1] and mat[i][j]!=0:
                mat[i][j]=(mat[i][j])*2
                mat[i][j+1] =0
                change=True
    return mat,change
                        
def reverse(mat): 
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
            
    return new_mat

def transpose(mat):
    
    new_mat=[]
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
            
    return new_mat
        
def move_left(grid):
    new_grid,change1=compress(grid)
    new_grid,change2=merge(new_grid)
    change=change1 or change2
    
    new_grid,temp=compress(new_grid)
    
    return new_grid,change

def move_up(grid):
    print("Move up called")
    transpose_grid=transpose(grid)
    new_grid,change1=compress(transpose_grid)
    new_grid,change2=merge(new_grid)
    change=change1 or change2
    new_grid,temp=compress(new_grid)
    final_transpose_grid=transpose(new_grid)
    return final_transpose_grid,change
    
def move_down(grid):
    print("Move dowm called")
    transpose_grid=transpose(grid)
    reverse_grid=reverse(transpose_grid)
    new_grid,change1=compress(reverse_grid)
    new_grid,change2=merge(new_grid)
    change=change1 or change2
    new_grid,temp=compress(new_grid)
    final_reverse_grid=reverse(new_grid)
    final_transpose_grid=transpose(final_reverse_grid)
    return final_transpose_grid,change
  
def move_right(grid):
    
    reverse_grid=reverse(grid)
    new_grid,change1=compress(reverse_grid)
    new_grid,change2=merge(new_grid)
    change=change1 or change2
    new_grid,temp=compress(new_grid)
    reverse_grid=reverse(new_grid)
    return reverse_grid,change
    
    

     