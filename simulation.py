import math
import numpy as np 

class Qubit(object):
    '''This defines a qubit in our simulation, we will be using a spin-(1/2) particle
    spin is defined as (alpha)|0> + (beta)|1> '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.theta = math.atan2(math.sqrt(x**2 + y**2), math.sqrt(z**2))
        self.phi = math.atan2(math.sqrt(x**2 + y**2), math.sqrt(x**2))
        self.alpha = math.cos(self.theta/2.)
        self.beta = (math.e**(1j*self.phi))*math.sin(self.theta/2.)
        # zero  probablility is alpha^2
        # one probability is beta ^2

    def check(self):
        if abs(self.alpha)**2 + abs(self.beta)**2 == 1:
            print "Good spin"
            print self.x, self.y, self.z
            print self.theta, self.phi
            print self.alpha, self.beta
            return True
        else:
            print "Bad spin"
            return False

class Gate(object):
    '''Base class to define other gates from,
    Matrix needs to be numpy matrix'''
    def __init__(self, matrix):
        self.operation = matrix
    



def test():
    testBit = Qubit(0,1,0)
    testBit.check()

if __name__ == '__main__':
    test()
