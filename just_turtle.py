import turtle as screen

def window_size():
    return (screen.window_width(), screen.window_height())

def circle_at(pos, size, value):
    screen.pu()
    screen.setpos(pos)
    screen.setheading(0)
    screen.pd()
    screen.begin_fill()
    screen.circle(size)
    screen.end_fill()
    screen.pu()

    screen.setheading(90)
    screen.fd(size // 2)
    screen.pd()
    screen.write(value, align='center', font=('Arial', size - 4, 'normal'))
    screen.pu()

def run1():

    screen.bgcolor("black")
    screen.color("green")
    screen.fillcolor("white")
    screen.speed(0)
    screen.hideturtle()
    screen.width(3)

    foot_size = 64

    (w, h) = (screen.window_width(), screen.window_height())

    size = w // foot_size
    h_size = size // 2
    print('size', size)

    y = 0
    x = (foot_size // 2) * -size
    for i in range(64):
        print(i, (x, y))
        circle_at((x, y), size // 2, i)
        x += size

    y = size * 2
    x = (foot_size // 2) * -size
    x += h_size * 1
    for i in range(32):
        print(i, (x, y))
        circle_at((x, y), size // 2, i)
        x += size * 2

    y = size * 4
    x = (foot_size // 2) * -size
    x += h_size * 3

    for i in range(16):
        print(i, (x, y))
        circle_at((x, y), size // 2, i)
        x += size * 4

    y = size * 6
    x = (foot_size // 2) * -size
    x += h_size * 7

    for i in range(8):
        print(i, (x, y))
        circle_at((x, y), size // 2, i)
        x += size * 8

    y = size * 8
    x = (foot_size // 2) * -size
    x += h_size * 15

    for i in range(4):
        print(i, (x, y))
        circle_at((x, y), size // 2, i)
        x += size * 16

    y = size * 10
    x = (foot_size // 2) * -size
    x += h_size * 31

    for i in range(2):
        print(i, (x, y))
        circle_at((x, y), size // 2, i)
        x += size * 32

    y = size * 12
    x = (foot_size // 2) * -size
    x += h_size * 63

    circle_at((x, y), size // 2, i)
    x += size * 64

    screen.mainloop()

run1()

