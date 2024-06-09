import sys
import os
import src.tree as tree

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    
def step2(z, x1, y1):
    knows = [x1, y1]
    possibles = []
    z2_prime = int(((z - (x1 * y1)) / 10 )) % 10
    for x2 in DIGITS:
        for y2 in DIGITS:
            if (((x2 * y1) + (x1 * y2)) % 10 == int(z2_prime)):       
                new_possible = str(x2) + ',' + str(y2)         
                possibles.append(new_possible)
    return possibles    
    
if __name__ == '__main__':
    # import src.utils as utils
    # utils.write_versions()
    
    
    
    
    
    #step 1. get N, might want to have it come from a file
    #   also might be worth to save know p and q for testing
    
    #step 2. Create the tree
        #likely save to a file, thinking json. object is too much overhead
        #it might be nice to have some look up tables to skip ahead
        # this needs to be recursive. 
        # need to spend more time with the math to create a matrix to represent the system of linear equations that is built systematically based on the size of N

    #step 3. traverse the tree for the solution
        # have some checkpoint/resumability
        # some visualization for the traversal
        # some visualization of what branches get created give the outcome we want
        
    #step 4. save the solution to a file
    
    #step 5. profit
    
    N = 9
    potentials = tree.attempt_build(N, max_iter=2)
    result = tree.check(N, potentials)
    print(result)
    
    
    
    
        