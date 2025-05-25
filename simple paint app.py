import turtle

# === PRINT INSTRUCTIONS TO CONSOLE ===
print("""
🎨 Welcome to Turtle Paint App!

🖱️ Mouse Controls:
  - Left-click and drag to draw
  - Right-click to lift the pen

🎨 Color Shortcuts:
  - [r] Red
  - [g] Green
  - [b] Blue
  - [k] Black
  - [e] Eraser

🖋️ Pen Size:
  - [Up Arrow] to increase size
  - [Down Arrow] to decrease size

🧹 Other:
  - [c] Clear the screen
  - Or use on-screen buttons!

Enjoy drawing!
""")

# === SETUP ===
screen = turtle.Screen()
screen.title("Enhanced Turtle Paint App")
screen.bgcolor("white")
screen.setup(width=800, height=600)

# Pen turtle
pen = turtle.Turtle()
pen.shape("circle")
pen.color("black")
pen.penup()
pen.speed(0)
pen.pensize(5)

# UI writer turtle
ui_writer = turtle.Turtle()
ui_writer.hideturtle()
ui_writer.penup()

# Instruction writer turtle
instr_writer = turtle.Turtle()
instr_writer.hideturtle()
instr_writer.penup()
instr_writer.goto(-390, 270)
instr_writer.write("Left-click to draw | Right-click to lift | r/g/b/k/e for colors | c to clear | Up/Down to resize",
                   font=("Arial", 10, "normal"))

# Variables
pen_size = 5
current_color = "black"
eraser_on = False

# === FUNCTIONS ===

def draw(x, y):
    pen.goto(x, y)
    pen.pendown()

def lift(x, y):
    pen.penup()

def update_ui():
    ui_writer.clear()
    ui_writer.goto(-380, 260)
    ui_writer.write(f"Pen Size: {pen_size}   Color: {current_color}   Mode: {'Eraser' if eraser_on else 'Draw'}",
                    font=("Arial", 12, "bold"))

def set_color(color):
    global current_color, eraser_on
    current_color = color
    eraser_on = False
    pen.color(color)
    update_ui()

def increase_size():
    global pen_size
    if pen_size < 50:
        pen_size += 1
        pen.pensize(pen_size)
        update_ui()

def decrease_size():
    global pen_size
    if pen_size > 1:
        pen_size -= 1
        pen.pensize(pen_size)
        update_ui()

def clear_screen():
    pen.clear()
    update_ui()

def use_eraser():
    global eraser_on
    eraser_on = True
    pen.color("white")
    update_ui()

# === BUTTONS ===

def make_button(label, x, y, color, action):
    b = turtle.Turtle()
    b.hideturtle()
    b.speed(0)
    b.penup()
    b.goto(x, y)
    b.shape("square")
    b.shapesize(stretch_wid=2, stretch_len=4)
    b.fillcolor(color)
    b.showturtle()
    b.onclick(lambda x, y: action())

    label_t = turtle.Turtle()
    label_t.hideturtle()
    label_t.penup()
    label_t.goto(x, y - 10)
    label_t.write(label, align="center", font=("Arial", 10, "bold"))

# === CREATE BUTTONS ===
make_button("Red", -350, 200, "red", lambda: set_color("red"))
make_button("Green", -250, 200, "green", lambda: set_color("green"))
make_button("Blue", -150, 200, "blue", lambda: set_color("blue"))
make_button("Black", -50, 200, "black", lambda: set_color("black"))
make_button("Eraser", 50, 200, "white", use_eraser)
make_button("+ Size", 150, 200, "gray", increase_size)
make_button("- Size", 250, 200, "gray", decrease_size)
make_button("Clear", 350, 200, "orange", clear_screen)

pen.penup()

def click_draw(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()

def lift_pen(x, y):
    pen.penup()

screen.onscreenclick(click_draw, 1)   # Left-click draws a dot or starts drawing
screen.onscreenclick(lift_pen, 3)     # Right-click lifts pen
pen.ondrag(draw)                       # Drag draws continuously


# Keyboard bindings
screen.listen()
screen.onkey(lambda: set_color("red"), "r")
screen.onkey(lambda: set_color("green"), "g")
screen.onkey(lambda: set_color("blue"), "b")
screen.onkey(lambda: set_color("black"), "k")
screen.onkey(clear_screen, "c")
screen.onkey(use_eraser, "e")
screen.onkey(increase_size, "Up")
screen.onkey(decrease_size, "Down")

# Initial UI display
update_ui()

turtle.done()
