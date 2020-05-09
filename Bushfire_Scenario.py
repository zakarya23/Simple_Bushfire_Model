def check_ignition(b_grid, f_grid, h_grid, i_threshold, w_direction, i, j):
    '''Checks if a certain cell is burning depeniding on its height, wind 
    direction, fuel load and ignition threshold'''
    pass
    
    coor = (i, j) 
    i_factor = 0
    length = range(len(b_grid[0]))
    
    # If fuel load of required cell is 0, hence it will not start burning
    if f_grid[coor[0]][coor[1]] == 0: 
        return False
        
    # Goes through b_grid and checks which cells are burning, then creates a 
    # list of tuples that would catch fire around the burning cells.
    for b_celli in length: 
        for b_cellj in length: 
            if b_grid[b_celli][b_cellj] is True: 
                coor1 = (b_celli, b_cellj)
                if f_grid[coor1[0]][coor1[1]] == 1 and coor == coor1: 
                    return False
                else: 
                    burn_cells = [(b_celli + 1, b_cellj),
                                  (b_celli, b_cellj + 1),
                                  (b_celli + 1, b_cellj + 1),
                                  (b_celli - 1, b_cellj),
                                  (b_celli - 1, b_cellj - 1),
                                  (b_celli, b_cellj - 1),
                                  (b_celli + 1, b_cellj - 1),
                                  (b_celli - 1, b_cellj + 1)] 
                    
                    # Checks height of cell and compares it to the burning 
                    # cell
                    for burning in burn_cells: 
                        if coor == burning:
                            h_coor = h_grid[coor[0]][coor[1]]
                            h_burn = h_grid[coor1[0]][coor1[1]] 
                            if h_burn < h_coor: 
                                i_factor += 2 
                            elif h_burn > h_coor: 
                                i_factor += 0.5
                            elif h_burn == h_coor:
                                i_factor += 1
                                
                            # Goes through the winds provided to check which 
                            # cells are affected as a result of the wind
                            if w_direction == 'N': 
                                ad_cells = [(i - 2, j - 1), (i - 2, j), 
                                            (i - 2, j + 1)] 
                                for c in ad_cells: 
                                    if c in burn_cells: 
                                        h_coor = h_grid[coor[0]][coor[1]]
                                        h_wind = h_grid[c[0]][1]
                                        if h_wind < h_coor: 
                                            i_factor += 2
                                        elif h_wind > h_coor: 
                                            i_factor += 0.5 
                                        elif h_wind == h_coor: 
                                            i_factor += 1
    
                            elif w_direction == 'S': 
                                ad_cells = [(i, j - 2), (i + 1, j - 2),
                                            (i - 1, j - 2)] 
                                for c in ad_cells:
                                    if c in burn_cells: 
                                        h_coor = h_grid[coor[0]][coor[1]]
                                        h_wind = h_grid[c[0]][1]
                                        if h_wind < h_coor: 
                                            i_factor += 2
                                        elif h_wind > h_coor: 
                                            i_factor += 0.5 
                                        elif h_wind == h_coor: 
                                            i_factor += 1
              
                            elif w_direction == 'E': 
                                ad_cells = [(i, j - 2), (i - 1, j - 2),
                                            (i + 1, j - 2)] 
                                for c in ad_cells: 
                                    if c in burn_cells: 
                                        h_coor = h_grid[coor[0]][coor[1]]
                                        h_wind = h_grid[c[0]][c[1]]
                                        if h_wind < h_coor: 
                                            i_factor += 2
                                        elif h_wind > h_coor: 
                                            i_factor += 0.5 
                                        elif h_wind == h_coor: 
                                            i_factor += 1
                
                            elif w_direction == 'W': 
                                ad_cells = [(i, j + 2), (i - 1, j + 2),
                                            (i + 1, j + 2)] 
                                for c in ad_cells:
                                    if c in burn_cells: 
                                        h_coor = h_grid[coor[0]][coor[1]]
                                        h_wind = h_grid[c[0]][1]
                                        if h_wind < h_coor: 
                                            i_factor += 2
                                        elif h_wind > h_coor: 
                                            i_factor += 0.5 
                                        elif h_wind == h_coor: 
                                            i_factor += 1
                                
                            elif w_direction == 'NW': 
                                ad_cells = [(i - 2, j - 1), (i - 2, j - 2),
                                            (i - 1, j - 2)] 
                                for c in ad_cells:
                                    if c in burn_cells:
                                        h_coor = h_grid[coor[0]][coor[1]]
                                        h_wind = h_grid[c[0]][1]
                                        if h_wind < h_coor: 
                                            i_factor += 2
                                        elif h_wind > h_coor: 
                                            i_factor += 0.5 
                                        elif h_wind == h_coor: 
                                            i_factor += 1
   
                            elif w_direction == 'NE': 
                                ad_cells = [(i + 2, j - 1), (i + 2, j - 2),
                                            (i + 1, j - 2)] 
                                for c in ad_cells:
                                    if c in burn_cells: 
                                        h_coor = h_grid[coor[0]][coor[1]]
                                        h_wind = h_grid[c[0]][1]
                                        if h_wind < h_coor: 
                                            i_factor += 2
                                        elif h_wind > h_coor: 
                                            i_factor += 0.5 
                                        elif h_wind == h_coor: 
                                            i_factor += 1
                
                        elif w_direction == 'SW': 
                            ad_cells = [(i + 1, j - 2), (i + 2, j - 2),
                                        (i + 2, j - 1)] 
                            for c in ad_cells: 
                                if c in burn_cells: 
                                    h_coor = h_grid[coor[0]][coor[1]]
                                    h_wind = h_grid[c[0]][1]
                                    if h_wind < h_coor: 
                                        i_factor += 2
                                    elif h_wind > h_coor: 
                                        i_factor += 0.5 
                                    elif h_wind == h_coor: 
                                        i_factor += 1
                
                        elif w_direction == 'SE': 
                            ad_cells = [(i - 1, j - 2), (i - 2, j - 2),
                                        (i - 2, j - 1)] 
                            for c in ad_cells: 
                                if c in burn_cells:
                                    h_coor = h_grid[coor[0]][coor[1]]
                                    h_wind = h_grid[c[0]][1]
                                    if h_wind < h_coor: 
                                        i_factor += 2
                                    elif h_wind > h_coor: 
                                        i_factor += 0.5 
                                    elif h_wind == h_coor: 
                                        i_factor += 1
                  
    return i_factor >= i_threshold
               
