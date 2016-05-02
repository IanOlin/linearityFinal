import math
import numpy 

class Qubit(object):
    '''This defines a qubit in our simulation, we will be using a spin-(1/2) particle
    spin is defined as (alpha)|0> + (beta)|1> '''
    def __init__(self, x, y, z):
        self.spinVector = numpy.array([x,y,z])
        self.theta = math.atan2(math.sqrt(x**2 + y**2), math.sqrt(z**2))
        self.phi = math.atan2(math.sqrt(x**2 + y**2), math.sqrt(x**2))
        self.alpha = math.cos(self.theta/2.)
        self.beta = (math.e**(1j*self.phi))*math.sin(self.theta/2.)
        # zero  probablility is alpha^2
        # one probability is beta ^2

    def check(self):
        if self.alpha**2 + abs(self.beta**2) < 1.001 and self.alpha**2 + abs(self.beta**2)> .999:
            print "Good spin"
            print self.spinVector[0],self.spinVector[1], self.spinVector[2]
            '''print self.theta, self.phi
            print self.alpha, self.beta
            print self.alpha**2, abs(self.beta**2)'''
            return True
        else:
            print "Bad spin"
            print self.spinVector[0],self.spinVector[1], self.spinVector[2]
            print self.alpha**2+ abs(self.beta**2)
            return False


    def update(self):
        self.theta = math.atan2(math.sqrt(self.spinVector[0]**2 + self.spinVector[1]**2), math.sqrt(self.spinVector[2]**2))
        self.phi = math.atan2((self.spinVector[1]**2), math.sqrt(self.spinVector[0]**2))
        self.alpha = math.cos(self.theta/2.)
        self.beta = (math.e**(1j*self.phi))*math.sin(self.theta/2.)


def piflip(qubit):
    #flips a 0 and 1
    dif = qubit - .5
    return .5 - dif

def rotate(qubit,axis,amount):
    #rotate by pi
    xMatrix = numpy.array([[1, 0, 0], [0, math.cos(amount), -1*math.sin(amount)], [0, math.sin(amount), math.cos(amount)]])
    yMatrix = numpy.array([[math.cos(amount), 0, math.sin(amount)], [0, 1, 0], [-1*math.sin(amount), 0, math.cos(amount)]])
    zMatrix = numpy.array([[math.cos(amount), -1*math.sin(amount), 0], [math.sin(amount), math.cos(amount), 0], [0, 0, 1]])
    axes = ['x', 'y', 'z']
    thisAxis=axes.index(axis)
    operations = [xMatrix, yMatrix, zMatrix]
    operation = operations[thisAxis]
    qubit.spinVector = numpy.matmul(qubit.spinVector, operation)


def rotateTest():
    testBit = Qubit(1,1.0,1)
    testBit.check()
    rotate(testBit, 'y', math.pi)
    testBit.check()
    

def paulix(qubit):
    # rotates the bloch spere around the x axis by pi
    rotate(qubit, 'x', math.pi)
    qubit.update()


def pauliy(qubit):
    # rotates the bloch spere around the y axis by pi
    rotate(qubit, 'y', math.pi)
    qubit.update()

def pauliz(qubit):
    # rotates the bloch spere around the z axis by pi
    rotate(qubit, 'z', math.pi)
    qubit.update()

def hadamard(qubit):
    rotate(qubit, 'y', math.pi/2)
    rotate(qubit, 'x', math.pi)

def testxyz():
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

def testHadamard():
    testBit = Qubit(1,1.0,1)
    print "start"
    testBit.check()
    print "hadamard"
    hadamard(testBit)
    testBit.check()


if __name__ == '__main__':
    testxyz()
    #testHadamard()
    #rotateTest()