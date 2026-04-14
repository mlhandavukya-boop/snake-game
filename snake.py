from turtle import Turtle
POSITION=[(0,0),(-20,0),(-40,0)]
DISTANCE=20
RIGHT=0
LEFT=180
UP=90
DOWN=270
class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.snake_list=[]
        self.snakes_object()
        self.head=self.snake_list[0]
    def snakes_object(self):
        for t in POSITION:
            self.add_segment(t)
    def add_segment(self,t):
        tini = Turtle(shape="square")
        tini.color("white")
        tini.penup()
        tini.goto(t)
        self.snake_list.append(tini)
    def reset_game(self):
        for s in self.snake_list:
            self.goto(1000,1000)
        self.snake_list.clear()
        self.snakes_object()
        self.head = self.snake_list[0]

    def extend(self):
        self.add_segment(self.snake_list[-1].position())

    def move(self):
        for s in range(len(self.snake_list) - 1, 0, -1):
            new_x = self.snake_list[s - 1].xcor()
            new_y = self.snake_list[s - 1].ycor()
            self.snake_list[s].goto(new_x, new_y)
        self.head.forward(DISTANCE)
    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)






