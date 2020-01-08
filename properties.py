#import pandas as pd
import random
from pyglet.gl import *


window_width = 700
window_height = 700

scale_value = 8

'''
data = pd.read_csv("Iris.csv")
setosa =    ((data[["SepalLengthCm","SepalWidthCm"]]) [(data.Species =="Iris-setosa")])
virginica = ((data[["SepalLengthCm","SepalWidthCm"]]) [(data.Species =="Iris-virginica")])
'''

class Point():
    def __init__(self,x,y,classType,color,classification):
        self.classType = classType
        self.color = color
        self.x = x
        self.y = y
        self.classification = classification

    def drawpoint(self):
        if self.classType == 1:
            x1 = (self.x - scale_value) /(window_width/2)
            y1 = (self.y + scale_value) /(window_height/2)
            x2 = (self.x + scale_value) /(window_width/2)
            y2 = (self.y + scale_value) /(window_height/2)
            x3 = (self.x + scale_value) /(window_width/2)
            y3 = (self.y - scale_value) /(window_height/2)
            x4 = (self.x - scale_value) /(window_width/2)
            y4 = (self.y - scale_value) /(window_height/2)
            color = self.color 
            
            glBegin(GL_QUADS)
            glColor3f(color[0],color[1],color[2]) #You can set RGB color for you vertex
            glVertex2f(x1,y1)
            glVertex2f(x2,y2)
            glVertex2f(x3,y3 )
            glVertex2f(x4,y4)
            glEnd()
            
            if self.classification == True:
                glLineWidth(3)
                glBegin(GL_LINE_LOOP);
                glColor3f(0,1,0);
                glVertex2f(x1,y1)
                glVertex2f(x2,y2)
                glVertex2f(x3,y3)
                glVertex2f(x4,y4)
                glEnd();
            elif self.classification == False:
                glLineWidth(3)
                glBegin(GL_LINE_LOOP);
                glColor3f(1,0,0);
                glVertex2f(x1,y1)
                glVertex2f(x2,y2)
                glVertex2f(x3,y3)
                glVertex2f(x4,y4)
                glEnd();
            else:
                pass

        elif self.classType == -1:
            x1 = (self.x) /(window_width /2)
            y1 = (self.y + scale_value) /(window_height /2)
            x2 = (self.x - scale_value) /(window_width /2)
            y2 = (self.y - scale_value) /(window_height /2) 
            x3 = (self.x + scale_value) /(window_width /2)
            y3 = (self.y - scale_value) /(window_height /2)

            color = self.color 
            
            glBegin(GL_TRIANGLE_STRIP);
            
            glColor3f(color[0], color[1], color[2]) #You can set RGB color for you vertex
            glVertex2f(x1, y1);
            glVertex2f(x2, y2);
            glVertex2f(x3, y3);
            glEnd()
            
            if self.classification == True:
                glLineWidth(3)
                glBegin(GL_LINE_LOOP);
                glColor3f(0,1,0);
                glVertex2f(x1, y1);
                glVertex2f(x2, y2);
                glVertex2f(x3, y3);
                glEnd();
            elif self.classification == False:
                glLineWidth(3)
                glBegin(GL_LINE_LOOP);
                glColor3f(1,0,0);
                glVertex2f(x1, y1);
                glVertex2f(x2, y2);
                glVertex2f(x3, y3);
                glEnd();
            else :
                pass

points = []

def line_equation(x):
    return (-1.5*x)+50

for i in range (0,100):
    x = random.uniform(-int(window_width/2),int(window_width/2))
    y = random.uniform(-int(window_height/2),int(window_height/2))

    line = line_equation(x)
    if y < line:
        points.append(Point(x,y,-1,[1,1,0],None))
    else:
        points.append(Point(x,y,1,[0,0,0],None))

