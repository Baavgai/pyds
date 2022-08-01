import turtle as screen

node_size = 18
font_size = 10

def reset_pos(p):
    screen.pu()
    screen.setpos(p)
    screen.setheading(0)

def draw_tree(tree):
    def down_node(width):
        screen.pu()
        screen.setheading(90)
        screen.fd(node_size)

        (x,y) = screen.pos()
        screen.pd()
        screen.setpos((x + width, y - (node_size * 3)))
        
        screen.pu()
        screen.setheading(270)
        screen.fd(node_size)

    def draw_node(value, pos):
        reset_pos(pos)
        screen.pd()
        screen.begin_fill()
        screen.circle(node_size)
        screen.end_fill()
        screen.pu()
        screen.setheading(90)
        screen.fd(node_size // 2)
        screen.pd()
        screen.write(value, align='center', font=('Arial', font_size, 'normal'))
        screen.pu()
    

    def loop(node, width):
        (value, left, right) = node
        p = screen.pos()
        w2 = max(width // 2, node_size)
        
        if left is not None:
            down_node(-width)
            loop(left, w2)
        if right is not None:
            reset_pos(p)
            down_node(width)
            loop(right, w2)
        draw_node(value, p)

    (w, _) = screen.screensize()
    loop(tree, w)

def tree_to_screen(tree):
    print(tree, tree)
    screen.bgcolor("black")
    screen.color("green")
    screen.fillcolor("white")
    screen.speed(0)
    screen.hideturtle()
    screen.width(3)
    (_, h) = screen.screensize()
    screen.pu()
    screen.setpos((0, h))
    draw_tree(tree)
    screen.mainloop()

import tree_immutable as provider
from shared import insert_data
from tests import test_data_u


tree_to_screen(insert_data(provider, test_data_u(40)))
