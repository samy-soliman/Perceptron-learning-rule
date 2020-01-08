import random
import properties as prob
from pyglet.gl import *


class Perceptron():
    def __init__(self,numOfInputs):
        self.weights = []
        for i in range (0,numOfInputs):
            self.weights.append(random.uniform(-1,1))
        
        self.bias = 1.0
        self.learning_rate = 0.01

    # one point x , y 
    def dotProduct(self,inputs):
        inputs = inputs
        totalSUM = 0.0
        for i in range(len(inputs)):
            totalSUM += inputs[i] * self.weights[i]
        return totalSUM
    
    def activationFunction(self,totalSUM):
        totalSUM = totalSUM
        if totalSUM < 0.0:
            return -1
        else:
            return 1
    
    def train(self,inputs,predictedValue,targetValue):
        inputs = inputs
        predictedValue= predictedValue
        targetValue = targetValue

        error = targetValue - predictedValue

        for i in range (len(self.weights)):
            self.weights[i] += error * inputs[i] * self.learning_rate

    def drawPredictedLine(self):

        m = - (self.weights[1] / self.weights[2])
        b = - (self.weights[0] / self.weights[2])

        print('m: ' + str(m))
        print('b: ' + str(b))


        x1 = -350 /(prob.window_width/2)
        y1 = m*x1 + b


        x2 = 350 /(prob.window_width/2)
        y2 = m*x2 + b

        cordinates= [x1,y1,x2,y2]
        color = [78, 232, 255 ,78, 232,255 ]
        line = pyglet.graphics.vertex_list( 2,('v2f',cordinates),('c3B',color))

        glLineWidth(5)
        line.draw(GL_LINE_STRIP)

        

        

    


