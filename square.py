import turtle
import random

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("black")

# Create a turtle
artist = turtle.Turtle()
artist.shape("turtle")
artist.speed(10)
artist.pensize(2)

# Function to generate a random color
def random_color():
    return (random.random(), random.random(), random.random())

# Draw a crazy pattern
for _ in range(36):  # Repeat the pattern 36 times
    artist.color(random_color())  # Set a random color
    artist.forward(100)
    artist.right(45)
    artist.color(random_color())
    artist.forward(50)
    artist.right(45)
    artist.color(random_color())
    artist.forward(100)
    artist.right(45)
    artist.color(random_color())
    artist.forward(50)
    artist.right(45)

# Hide the turtle
artist.hideturtle()

# Keep the window open
turtle.done()
