import os, time, math 
from abc import ABC, abstractmethod
from multipledispatch import dispatch

# Version 17/12/22 20:34

class Tela:
    def __init__(self, x, y):
        self.width = x
        self.height = int(y/2)
        self.surface = []
        for i in range(self.height):
            self.surface.append([])
            for j in range(self.width):
                self.surface[i].append(" ")
        self.surface_save = self.surface.copy()
    
    def getHeight(self):
        return self.height*2

    def getWidth(self):
        return self.width

    def center(self):
        return Point(self.getWidth()/2, self.getHeight()/2)

    def clear(self):
        for i in range(self.height):
            for j in range(self.width):
                self.surface[i][j] = ' '

    def toString(self) -> str:
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                output += self.surface[i][j]
            output += "\n"
        return output

    def drawObject(self, object):
        object.draw(self)

    def drawPoint(self, character, x, y):
        y /= 2
        if x >= self.width or x < 0:
            return False
        if y >= self.height or y < 0:
            return False
        i = int(y)
        j = int(x)
        self.surface[i][j] = character
        return True

    def drawLine(self, character, xo, yo, length):
        for i in range(length):
            self.drawPoint(character, xo + i, yo)

    def drawCollumn(self, character, xo, yo, height):
        for j in range(height):
            self.drawPoint(character, xo, yo + j)

    def drawDivisionLine(self, character, yo):
        self.drawLine(character, 0, yo, self.getWidth())

    def drawDivisionCollumn(self, character, xo):
        self.drawCollumn(character, xo, 0, self.getHeight())

    def drawBorder(self, cornerChar='@', horizontalChar='-', verticalChar='|'):
        self.drawDivisionLine(horizontalChar, 0)
        self.drawDivisionLine(horizontalChar, self.getHeight()-1)
        self.drawDivisionCollumn(verticalChar, 0)
        self.drawDivisionCollumn(verticalChar, self.getWidth()-1)
        self.drawPoint(cornerChar, 0, 0)
        self.drawPoint(cornerChar, 0, self.getHeight()-1)
        self.drawPoint(cornerChar, self.getWidth()-1, 0)
        self.drawPoint(cornerChar, self.getWidth()-1, self.getHeight()-1)

    def write(self, text, xo, yo):
        for i in range(len(text)):
            self.drawPoint(text[i], xo+i, yo)

    def drawCircle(self, char, xo, yo, radius):
        for i in range(360):
            x = xo + radius*math.cos(math.pi/180 * i)
            y = yo + radius*math.sin(math.pi/180 * i)
            self.drawPoint(char, x, y)


class Object2D(ABC):
    def __init__(self):
        self.points = []

    @abstractmethod
    def draw(self, tela):
        pass

    def rotateAroundPoint(self, point, degree):
        for myPoint in self.points:
            myPoint.rotateAroundPoint(point, degree)
    
    @dispatch(list)
    def translateBy(self, vector: list):
        for point in self.points:
            point.translateBy(vector)

    @dispatch(float, float)
    def translateBy(self, dx: float, dy: float):
        for point in self.points:
            point.translateBy(dx, dy)


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def draw(self, tela):
        tela.drawPoint('o', self.x, self.y)

    def translateTo(self, x: int, y: int):
        self.x = x
        self.y = y

    def translateToPoint(self, point):
        self.x = point.x
        self.y = point.y

    @dispatch(list)
    def translateBy(self, vector):
        self.x += vector[0]
        self.y += vector[1]

    @dispatch(float, float)
    def translateBy(self, dx, dy):
        self.x += dx
        self.y += dy

    def rotateAroundPoint(self, point, degree):
        n_division_focus = 8
        error_limit = 0.01
        distance = math.sqrt(pow(self.x-point.x, 2) + pow(self.y-point.y, 2))
        try:
            angle = math.atan((self.y-point.y)/(self.x-point.x))
            if self.x < point.x:
                angle += math.pi
        except ZeroDivisionError:
            if self.y - point.y > 0:
                angle = math.pi/2
            else: 
                angle = -1*math.pi/2
        angle += degree
        for i in range(n_division_focus):
            if abs(angle - i*2*math.pi/n_division_focus) < error_limit:
                angle = i*2*math.pi/n_division_focus
                break
        self.translateToPoint(Point(point.x + distance*math.cos(angle), point.y +
            distance*math.sin(angle)))



class Line(Object2D):
    def __init__(self, pointA, pointB):
        self.points = [pointA, pointB]

    def draw(self, tela: Tela):
        xo = min(self.points[0].x, self.points[1].x)
        x1 = max(self.points[0].x, self.points[1].x)
        if xo == self.points[0].x:
            yo = self.points[0].y
            y1 = self.points[1].y
        else:
            yo = self.points[1].y
            y1 = self.points[0].y
        dx = x1 - xo
        dy = y1 - yo

        if abs(dy) > abs(dx):
            density = int(abs(dy) + 1)
            switch = 1  # Decides if the +0.5 offset is on x (1) or y (0)
        else:
            density = int(abs(dx) + 1)
            switch = 0

        char = 'o'
        angle = self.inclinationAngle()
        if -1*math.atan(2)/2 < angle and angle <= math.atan(2)/2:
            char = '-'
        elif math.atan(2)/2 < angle and angle <= (math.pi/2 + math.atan(2))/2:
            char = '\\'
        elif (math.pi/2 + math.atan(2))/2 < angle and angle <= math.pi/2 or -1*math.pi/2 < angle and angle <= -1*(math.pi/2 + math.atan(2))/2:
            char = '|'
        elif -1*(math.pi/2 + math.atan(2))/2 < angle and angle <= -1*math.atan(2)/2:
            char = '/'

        for i in range(density):
            x = xo + i/density*dx + 0.5*switch
            y = yo + i/density*dy + 0.5*(abs(switch-1))
            tela.drawPoint(char, x, y)
        for point in self.points:
            tela.drawObject(point)
   
    def lenght(self):
        A = self.points[0]
        B = self.points[1]
        lenght = math.sqrt(pow(A.x - B.x, 2) + pow(A.y - B.y, 2))
        return lenght

    def middlePoint(self):
        media_x = 0
        media_y = 0
        for point in self.points:
            media_x += point.x
            media_y += point.y
        media_x /= len(self.points)
        media_y /= len(self.points)
        return Point(media_x, media_y)
    
    def inclinationAngle(self):
        try:
            angle = math.atan((self.points[1].y-self.points[0].y)/(self.points[1].x-self.points[0].x))
        except ZeroDivisionError:
            angle = math.pi/2
        return angle

    def center(self):
        return self.middlePoint()


class Polygon(Object2D):
    def __init__(self, *points):
        if len(points) == 1 and type(points[0]).__name__ == 'list':
            self.points = points[0]
        else:
            self.points = []
            for point in points:
                self.points.append(point)

        self.lines = []
        for i in range(len(self.points)):
            if i < len(self.points) - 1:
                self.lines.append(Line(self.points[i], self.points[i+1]))
            else:
                self.lines.append(Line(self.points[i], self.points[0]))

    def draw(self, tela):
        for line in self.lines:
            line.draw(tela)

    def center(self):
        soma_x = 0
        soma_y = 0
        for point in self.points:
            soma_x += point.x
            soma_y += point.y
        soma_x /= len(self.points)
        soma_y /= len(self.points)
        return Point(soma_x, soma_y)

    def translateToPoint(self, point):
        translation = point - self.center()
        for myPoint in self.points:
            myPoint.translateBy(translation.x, translation.y)

    def rotate(self, degrees):
        self.rotateAroundPoint(self.center(), degrees)


class Triangle(Polygon):
    def __init__(self, A: Point, B: Point, C: Point):
        super().__init__(A, B, C)  
   
    def baricenter(self):
       return self.center()


class RegularPolygon(Polygon):
    def __init__(self, central_point: Point, n_sides: int, radius: float, teta=0, step=1):
        points = []
        for i in range(n_sides):
            points.append(Point())
        i = 0
        for point in points:
            angle = step*i*2*math.pi/n_sides + teta
            point.translateTo(central_point.x + radius*math.cos(angle),
                    central_point.y + radius*math.sin(angle))
            i += 1
        super().__init__(points)


class Star(RegularPolygon): # Compatibility only
    def __init__(self, central_point, radius, teta=-math.pi/10, n_sides=5):
        super().__init__(central_point, n_sides, radius, teta, step=2)


class ShapeGroup(Object2D):
    def __init__(self, *shapesList):
        if len(shapesList) == 1 and type(shapesList[0]).__name__ == 'list':
            self.shapes = shapesList[0]
        else:
            self.shapes = []
            for shape in shapesList:
                self.shapes.append(shape)

    def draw(self, tela):
        for shape in self.shapes:
            tela.drawObject(shape)

    def rotateAroundPoint(self, point, degree):
        for shape in self.shapes:
            shape.rotateAroundPoint(point, degree)
   
    @dispatch(list)
    def translateBy(self, vector: list):
        for shape in self.shapes:
            shape.translateBy(vector)
            
    @dispatch(float, float)
    def translateBy(self, dx, dy):
        for shape in self.shapes:
            shape.translateBy(dx, dy)


class Circunference(Object2D):
    def __init__(self, xo: float, yo: float, radius: float):
        self.center = Point(xo, yo)
        self.radius = radius
   
    def draw(self, tela):
       char = 'o'
       tela.drawCircle(char, self.center.x, self.center.y, self.radius)
 
