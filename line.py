import turtle as t

n=50
t.bgcolor("black")
t.color("green")
t.speed(0)
for x in range(n):
    t.circle(80)
    t.left(360/n)

t.forward(200)

angle=91
t.color("yellow")
t.speed(0)
for x in range(200):
    t.forward(x)
    t.left(angle)

t.right(90)
t.forward(50)
angle=89
t.color("blue")
t.speed(0)
for x in range(200):
    t.forward(x)
    t.left(angle)
