from reference import check_ignition

def run_model(f_grid, h_grid, i_threshold, w_direction, burn_seeds):
    '''Takes in arguemnts and returns final state of cells and total number 
    of cells burnt'''
    pass
    length = len(f_grid) 
    
    # Creates a initial b_grid which is all False
    
    b_grid = []
    for i in range(length): 
        grid = []
        for j in range(length): 
            grid.append(False) 
        b_grid.append(grid) 
        
    for b_cell in burn_seeds: 
        if not b_cell: 
            burning = False 
        burning = True
        b_grid[b_cell[0]][b_cell[1]] = True
        
    # While loop keeps iterating until no cells are burning 
    count = 0
   
    while burning: 
        
        # Creating a duplicate b_grid 
        nb_grid =[]
        q = 0
        for a in range(length):
            gri = []
            for b in range(length): 
                gri.append(False) 
            nb_grid.append(gri)
            
        
       
        for i in range(length): 
            for j in range(length):         
                if b_grid[i][j] is False and f_grid[i][j] != 0: 
                    nb_grid[i][j] = check_ignition(b_grid, f_grid, h_grid,
                                   i_threshold, w_direction, i, j)
                elif b_grid[i][j] is True: 
                    if f_grid[i][j] != 0: 
                        f_grid[i][j] -=1
                        nb_grid[i][j] = True
                    else: 
                        count+=1

        b_grid = nb_grid 
 
  
                        
        
        # Checking whether all values of b_grid are False or not
        
        for item in nb_grid: 
            for thing in item: 
                if thing is True: 
                    q+=1  
        if q == 0: 
            burning = False
                    
       
        
    return (f_grid, count) 
       
      
         
        
                 
                    
            
            
     
        
        
    
    
        
   
