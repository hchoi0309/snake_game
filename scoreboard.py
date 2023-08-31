from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.curr_score = 0
        self.goto(0, 270)
        self.color("white")
        self.display()

    def score(self):
        self.curr_score += 1
        self.display()
    
    def display(self):
        self.clear()
        self.write(f"Score: {self.curr_score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def game_over(self):
        self.home()
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()