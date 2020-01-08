import pyglet
import properties as prob
from perceptron import Perceptron
from pyglet.gl import *

class Line():
    def __init__(self,x1,y1,x2,y2,color):
        self.x1 = x1 /(prob.window_width/2)
        self.y1 = y1 /(prob.window_height/2)
        self.x2 = x2 /(prob.window_width/2)
        self.y2 = y2 /(prob.window_height/2)

        self.cordinates= [self.x1,self.y1,self.x2,self.y2]
        self.color = color 
        self.line = pyglet.graphics.vertex_list( 2,('v2f',self.cordinates),('c3B',self.color))


    def drawLine(self):
        glLineWidth(5)
        self.line.draw(GL_LINE_STRIP)
  


class MyWindow(pyglet.window.Window):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)

        # background color red green blue alpha
        glClearColor(1,1,1,0)

        self.lineX = Line(-int(prob.window_width/2),0,int(prob.window_width/2),0,[38, 58, 87 ,38, 58, 87 ])
        self.lineY = Line(0,-int(prob.window_height/2),0,int(prob.window_height/2),[38, 58, 87 ,38, 58, 87 ])
        self.seprable_line = Line(-350,prob.line_equation(-350),350,prob.line_equation(350),[38, 58, 87 ,38, 58, 87 ])
        
        self.points = prob.points
        self.pointIndex = 0

        self.perceptron = Perceptron(3)


    def on_draw(self):
        self.clear()
        self.lineX.drawLine()
        self.lineY.drawLine()
        self.seprable_line.drawLine()

        self.perceptron.drawPredictedLine()

        for point in self.points:
            point.drawpoint()

        


    def update(self,dt):

        for point in self.points:
            inputs = [self.perceptron.bias, (point.x/(prob.window_width/2)),(point.y/(prob.window_height/2))]
            
            predictedValue = self.perceptron.activationFunction( self.perceptron.dotProduct(inputs) )
            targetValue = point.classType
            
            if predictedValue != targetValue:
                point.classification = False
            else :
                point.classification = True
        

        
        indexpoint = self.points[self.pointIndex]
        if self.pointIndex +1 == len(self.points):
            self.pointIndex =0
        else:
            self.pointIndex +=1

        inputs = [self.perceptron.bias, (indexpoint.x/(prob.window_width/2)),(indexpoint.y/(prob.window_height/2))]
        
        predictedValue = self.perceptron.activationFunction( self.perceptron.dotProduct(inputs) )
        targetValue = indexpoint.classType
        
        if predictedValue != targetValue:
            # inputs,predictedValue,targetValue
            self.perceptron.train(inputs ,predictedValue, targetValue)
        else :
            pass


    def on_resize(self,width,height):
        glViewport(0,0,width,height)
        pass



if __name__=="__main__":
    window = MyWindow(prob.window_width,prob.window_height,"perceptron trianing ",resizable = False)
    window.set_location( 300, 50)
    pyglet.clock.schedule_interval(window.update,10/60.0)
    
    pyglet.app.run()