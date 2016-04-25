import math
import cmath
import numpy as np 

class Qubit(object):
    '''This defines a qubit in our simulation, we will be using a spin-(1/2) particle
    spin is defined as (alpha)|0> + (beta)|1> '''
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.theta = math.atan2(math.sqrt(x**2 + y**2), math.sqrt(z**2))
        #self.theta = cmath.phase()
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
            print self.alpha**2, abs(self.beta**2)
            return True
        else:
            print "Bad spin"
            return False


    def update(self):
        self.theta = math.atan2(math.sqrt(self.x**2 + self.y**2), math.sqrt(self.z**2))
        self.phi = math.atan2(math.sqrt(self.x**2 + self.y**2), math.sqrt(self.x**2))
        self.alpha = math.cos(self.theta/2.)
        self.beta = (math.e**(1j*self.phi))*math.sin(self.theta/2.)


def flip(qubit):
    #flips a 0 and 1
    #TODO: make this flip around the middle of this range
    dif = qubit - .5
    return .5 - dif

def paulix(qubit):
    # rotates the bloch spere around the x axis by pi
    qubit.y = flip(qubit.y)
    qubit.z = flip(qubit.z)
    qubit.update()


def pauliy(qubit):
    # rotates the bloch spere around the y axis by pi
    qubit.x = flip(qubit.x)
    qubit.z = flip(qubit.z)
    qubit.update()

def pauliz(qubit):
    # rotates the bloch spere around the y axis by pi
    qubit.x = flip(qubit.x)
    qubit.y = flip(qubit.y)
    qubit.update()

def test():
    testBit = Qubit(1,1,1)
    print "start"
    testBit.check()
    paulix(testBit)
    print "paulix"
    testBit.check()
    pauliy(testBit)
    print "pauliy"
    testBit.check()
    pauliz(testBit)
    print "pauliz"
    testBit.check()

if __name__ == '__main__':
    test()