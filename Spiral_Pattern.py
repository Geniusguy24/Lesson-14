import turtle
import time

spiral = turtle.Screen()
spiral.bgcolor("light blue")
spiral.title("Infinite Spiral")
spiral_pen = turtle.Turtle()
size = 0

while True:
    for i in range(4):
        spiral_pen.fd(size + 1)
        time.sleep(0.15)
        spiral_pen.left(90)
        size = size - 5
    size = size + 1

turtle.done()