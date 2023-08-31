import turtle
MOVE_DISTANCE = 20
(RIGHT, UP, LEFT, DOWN) = (0, 90, 180, 270)

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        (x, y) = (0, 0)
        for i in range(3):
            self.add_segment((x, y))
            x -= 20
    
    def add_segment(self, position):
        segment = turtle.Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.segments.append(segment)

    def add_tail(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for i in range(len(self.segments) - 1 , 0, -1):
            self.segments[i].goto(self.segments[i-1].position())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)