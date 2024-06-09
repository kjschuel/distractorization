import re


# we are going to need a tree structure.
# but might go with arrays first when getting started,.
# should be fine with small numbers and is easier for me to understand 
# as I get off the ground

# I don't think an onject is a good idea because it will be big

# And when I say big... I mean BIG. Like take all your RAM big.

# So maybe we save it to a file. Maybe we make it a json.
# but if it's take all your RAM big... lets not be saving files that big...

# We will also need to traverse this tree... so we will want some sort 
# traversal, checkpoint, resumable aspect.


def build(N):
    
    print(step1(N))
    
    
    return None


def traverse():
    # need some sort of checkpoint and resume here
    return None



def write():
    # thinking a json with some info, including checkpoint info at the top level
    return None

def step1(n1):
    potentials = []
    for p1 in range(10):
        for q1 in range(p1, 10): # because at this point we dont care which we pick to be p or q
            if ((p1 * q1) % 10 == n1):
                potentials.append([p1, q1])
    return potentials


def step1_tree_attempt(n1):
    possibles = {}
    for p1 in range(10):
        for q1 in range(10):
            if ((p1 * q1) % 10 == n1):
                # since this is the last digit, what we choose to be P or Q does not matter
                # in fact, we don't need BOTH combinations
                pair = sorted([p1, q1])
                new_possible = str(pair[0]) + ',' + str(pair[1])
                if (possibles.get(new_possible) == None):
                    possibles[new_possible] = {}
    possibles['digits'] = 1
    return possibles

def adjust():
    return None


def terminate(max_iter, iter):
    # TODO: maybe detemrined by len(P)+len(Q) and how it compares to len(N)
    return max_iter == iter

def check(N, potentials):
    for potential in potentials:
        P = potential[0]
        Q = potential[1]
        # TODO: this will need to be a string multiplication eventually
        if (P*Q == N):
            return [P, Q]
    print('failure')
    return False
        

def attempt_build(N, max_iter = 1, ps=[], qs=[]):
    # TODO: error checking of ps and qs. 
    #   should begin empty.
    #   should be same length
    #   each entry should be the same number of digits

    potentials = step1(N % 10)

    iter = 1
    
    while not terminate(max_iter, iter):
        for potential in potentials:
            P = potential[0]
            Q = potential[1]
            N_prime = int((N - P*Q) / (10**iter))
            # TODO: need to build the next digit finder
            # p1q2 + p2q1 mod 10  = N_prime 
            print(N_prime)
        # keep building
        iter += 1
    
    
    
    return potentials

# def step2(n2_prime, p1, q1):
#     possibles = {}
#     n2_prime = int(((z - (x1 * y1)) / 10 )) % 10
#     for x2 in DIGITS:
#         for y2 in DIGITS:
#             if (((x2 * y1) + (x1 * y2)) % 10 == int(z2_prime)):       
#                 new_possible = str(x2) + ',' + str(y2)         
#                 possibles.append(new_possible)
#     return possibles    