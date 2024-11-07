import turtle
import random


class Polygon():
    def __init__(self):
        self._num_sides = random.randint(3, 5)
        self._size = random.randint(50, 150)
        self._orientation = random.randint(0, 90)
        self._location = [random.randint(-300, 300), random.randint(-200, 200)]
        self._color = (255, 255, 255)
        self._border_size = random.randint(1, 10)

    @property
    def num_sides(self):
        return self._num_sides
    
    @num_sides.setter
    def num_sides(self, value):
        if not isinstance(value, int) or not 3 <= value <= 5:
            raise ValueError
        self._num_sides = value

    @property
    def size(self):
        return self._size
    
    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise ValueError
        self._size = value

    @property
    def orientation(self):
        return self._orientation
    
    @orientation.setter
    def orientation(self, value):
        if not isinstance(value, int) or not 0 <= value <= 90:
            raise ValueError
        self._orientation = value

    @property
    def location(self):
        return self._location
    
    @location.setter
    def location(self, value):
        if not isinstance(value, list):
            raise ValueError
        self._location = value

    def __getitem__(self, ids):
        return self._location[ids]

    def __setitem__(self, ids, value):
        self._location[ids] = value

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        if not isinstance(value, tuple):
            raise ValueError
        self._color = value

    @property
    def border_size(self):
        return self._border_size
    
    @border_size.setter
    def border_size(self, value):
        if not isinstance(value, int) or not 1 <= value <= 10:
            raise ValueError
        self._border_size = value

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self._location[0], self._location[1])
        turtle.setheading(self._orientation)
        turtle.color(self._color)
        turtle.pensize(self._border_size)
        turtle.pendown()
        for _ in range(self._num_sides):
            turtle.forward(self._size)
            turtle.left(360/self._num_sides)
        turtle.penup()

    def get_new_color():
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


class EmbeddedPolygon(Polygon):
    def __init__(self,
                 reduction_ratio = 0.618):
        self._num_sides = random.randint(3, 5)
        self._size = random.randint(50, 150)
        self._orientation = random.randint(0, 90)
        self._location = [random.randint(-300, 300), random.randint(-200, 200)]
        self._color = (255, 255, 255)
        self._border_size = random.randint(1, 10)
        self._rep_time = random.randint(2, 4)
        self._reduction_ratio = reduction_ratio

    def draw_polygon(self):
        turtle.penup()
        turtle.goto(self._location[0], self._location[1])
        turtle.setheading(self._orientation)
        turtle.color(self._color)
        turtle.pensize(self._border_size)
        for i in range(self._rep_time):
            turtle.pendown()
            for _ in range(self._num_sides):
                turtle.forward(self._size * (self._reduction_ratio ** (i - 1)))
                turtle.left(360/self._num_sides)
            turtle.penup()
            turtle.forward(self._size*(1-(self._reduction_ratio))/(i + 1))
            turtle.left(90)
            turtle.forward(self._size*(1-(self._reduction_ratio))/(i + 1))
            turtle.right(90)
            self._location[0] = turtle.pos()[0]
            self._location[1] = turtle.pos()[1]

class Run():
    choice = 0

    def __init__(self):
        self.choice = int(input("Which art do you want to generate? Enter a number between 1 to 9 inclusive: "))
        if not isinstance(self.choice, int) or not 1 <= self.choice <= 9:
            raise ValueError("pls chooseing between 1 - 9")
        
    def Run_by_Choices(self):
        if self.choice == 1:
            for i in range(25):
                g = Polygon()
                g.num_sides = 3
                g._color = Polygon.get_new_color()
                Polygon.draw_polygon(g)
        elif self.choice == 2:
            for i in range(25):
                g = Polygon()
                g.num_sides = 4
                g._color = Polygon.get_new_color()
                Polygon.draw_polygon(g)
        elif self.choice == 3:
            for i in range(25):
                g = Polygon()
                g.num_sides = 5
                g._color = Polygon.get_new_color()
                Polygon.draw_polygon(g)
        elif self.choice == 4:
            for i in range(25):
                g = Polygon()
                g._color = Polygon.get_new_color()
                Polygon.draw_polygon(g)
        elif self.choice == 5:
            for i in range(25):
                g = EmbeddedPolygon()
                g.num_sides = 3
                g._rep_time = 3
                g._color = Polygon.get_new_color()
                EmbeddedPolygon.draw_polygon(g)
        elif self.choice == 6:
            for i in range(25):
                g = EmbeddedPolygon()
                g.num_sides = 4
                g._rep_time = 3
                g._color = Polygon.get_new_color()
                EmbeddedPolygon.draw_polygon(g)
        elif self.choice == 7:
            for i in range(25):
                g = EmbeddedPolygon()
                g.num_sides = 5
                g._rep_time = 3
                g._color = Polygon.get_new_color()
                EmbeddedPolygon.draw_polygon(g)
        elif self.choice == 8:
            for i in range(25):
                g = EmbeddedPolygon()
                g._rep_time = 3
                g._color = Polygon.get_new_color()
                EmbeddedPolygon.draw_polygon(g)
        else:
            for i in range(25):
                g = EmbeddedPolygon()
                g._color = Polygon.get_new_color()
                EmbeddedPolygon.draw_polygon(g)


"""main code"""


n = Run()

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

Run.Run_by_Choices(n)

turtle.done()
