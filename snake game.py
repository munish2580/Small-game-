import turtle
import time
import random

# Game delay and score
delay = 0.15
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)  # Turn off automatic screen updates

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# Snake food
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# Score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Score: {score}     High Score: {high_score}", align="center", font=("Courier", 22, "normal"))

# Movement functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)
    elif head.direction == "down":
        head.sety(head.ycor() - 20)
    elif head.direction == "left":
        head.setx(head.xcor() - 20)
    elif head.direction == "right":
        head.setx(head.xcor() + 20)

# Keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")

# Function to update the score
def update_score():
    pen.clear()
    pen.write(f"Score: {score}   High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

# Function to reset the game
def reset_game():
    global score, delay
    score = 0
    delay = 0.15
    update_score()

# Function to reset the snake
def reset_snake():
    head.goto(0, 0)
    head.direction = "stop"
    for segment in segments:
        segment.goto(1000, 1000)  # Moves the body segments out of the screen
    segments.clear()

# Function to check if food is placed on top of the snake
def place_food():
    x = random.randint(-290, 290)
    y = random.randint(-290, 290)
    
    # Ensure food is not placed on the snake
    for segment in segments:
        if segment.xcor() == x and segment.ycor() == y:
            return place_food()  # Recursively call until valid position is found
    food.goto(x, y)

# Main game loop
while True:
    wn.update()

    # Border collision check
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        time.sleep(1)
        reset_snake()
        reset_game()

    # Food collision check
    if head.distance(food) < 20:
        place_food()  # Place the food at a valid random position

        # Add a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay (increase game speed)
        delay -= 0.0025
        score += 10
        if score > high_score:
            high_score = score
        update_score()

    # Move the segments in reverse order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)

    # Move the first segment to the head's position
    if segments:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    # Move the head
    move()

    # Check for head collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            reset_snake()
            reset_game()

    time.sleep(delay)

wn.mainloop()
