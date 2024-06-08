DIGITS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

class Tree:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self):
        return f"TreeNode(value={self.value}, children={self.children})"

def step1(z):
    z1 = z % 10
    possibles = {}
    for x1 in DIGITS:
        for y1 in DIGITS:
            if ((x1 * y1) % 10 == z1):
                pair = sorted([x1, y1])
                new_possible = str(pair[0]) + ',' + str(pair[1])
                if (possibles.get(new_possible) == None):
                    possibles[new_possible] = ''
    possibles['digits'] = 1        
    return possibles
    
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
    print(step1(5063))
    print(step2(5063, 1, 3)) 
    
    
    
        