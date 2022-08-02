import tkinter as tk

bg_color = 'black'
fg_color = 'green'
node_color = 'white'

def draw_node(canvas, center, size, value):
    h_size = size // 2
    cx, cy = center
    x1, x2 = cx - h_size, cx + h_size
    y1, y2 = cy - h_size, cy + h_size
    canvas.create_oval(x1, y1, x2, y2, fill=node_color, outline=fg_color, width=3)
    canvas.create_text(cx, cy, text=value, fill=fg_color, font=('Arial', h_size // 2, 'normal') )

def draw_edge(canvas, p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    canvas.create_line(x1, y1, x2, y2, fill=fg_color, width=1)
    

def draw_tree(canvas, node_pos, width, node_size, tree, parent = None):
    if tree is not None:
        value, left, right = tree
        px, py = node_pos
        w2, py2 = width // 2, py + node_size * 2
        if parent is not None:
            draw_edge(canvas, parent, node_pos)
        draw_tree(canvas, (px - w2, py2), w2, node_size, left, node_pos)
        draw_tree(canvas, (px + w2, py2), w2, node_size, right, node_pos)
        draw_node(canvas, node_pos, node_size, value)


def tree_to_screen(tree, width = 1200, height = 800, node_size = 30, title = 'Tree Viewer'):
    root = tk.Tk()
    root.title(title)
    canvas = tk.Canvas(root, bg=bg_color, width=width, height=height)
    canvas.pack()
    
    start = (width // 2, node_size * 2)
    draw_tree(canvas, start, width // 2, node_size, tree)
    root.mainloop()

if __name__ == "__main__":
    # import tree_util as util
    import tree_immutable as provider
    from shared import insert_data
    from tests import test_data_u

    tree_to_screen(insert_data(provider, test_data_u(40)))
