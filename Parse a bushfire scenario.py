
import csv 
def parse_scenario(filename):
    '''Opens the contents of a file and divides them up according to the 
    criterion provided'''
    pass
    
    # Opens the files and gets the contents of the file 
    file = open(filename) 
    data = csv.reader(file)
    
    # Gives the width and height of the cells 
    length = next(data)[0]
    
    
    output = {}
    total = []
    
    # Goes through the first 'length' number of lines and makes the f_grid of 
    # the scenario
    f_grid = []
    for i in range(int(length)): 
        lis = [] 
        tot = []
        for j in next(data):
            if int(j) < 0:
                return None
            else: 
                lis.append(int(j)) 
                tot.append(j) 
        f_grid.append(lis) 
        total.append(tot) 
    output['f_grid'] = f_grid
    
    # Goes through the second 'length' number of lines and makes the h_grid of 
    # the scenario
    h_grid = []
    for i in range(int(length)): 
        lis = [] 
        for j in next(data):
            if int(j) < 0:
                return None 
            else:
                lis.append(int(j))
        h_grid.append(lis) 
    output['h_grid'] = h_grid
    
    # For the next data, it validates if the ignition threshold is between 
    # the given range and if it it adds it adds to the dict as a key, value 
    # pair
    for j in next(data):
        if int(j) <= 0 or int(j) >8: 
            return None
        else:
            output['i_threshold'] = int(j) 
     
    # Validates wind direction and if valid makes a key value pair in the 
    # dict 
    winds = ('N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW')
    out = ''
    for j in next(data):
        if j not in winds:
            return None 
        else:
            out += j 
 
    output['w_direction'] = out 
    
    # Finally checks whether the burning seeds are on the grid and if True 
    # adds a key value pair of burning seeds as a list 
    lis = []
    b_seeds = []
    for j in next(data):
        lis.append(int(j))
    if int(len(lis)) > int(length) or int(len(lis)) == 0:
        return None
         
    b_seeds.append(tuple(lis))
    output['burn_seeds'] = b_seeds
    
    # Closes file and returns output
    file.close()
    return output
 
        
     
          
                       
    
    