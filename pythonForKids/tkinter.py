import Tkinter
import turtle

# def hello():
#     print("hello")

tk = Tkinter.Tk()
# btn = Tkinter.Button(tk, text="click me", command=hello)
# btn.pack()
canvas = Tkinter.Canvas(tk, width=500, height=500)
canvas.pack()
canvas.create_line(0, 0, 500, 500)

turtle.setup(width=500, height=500)
t = turtle.Pen()
t.up()
t.goto(-250, 250)
t.down()
t.goto(500, -500)

tk.mainloop()
