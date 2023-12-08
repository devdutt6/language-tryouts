from tkinter import *

window = Tk()  # creates instance of window
# window.geometry("480x480")
window.title("first GUI")

icon = PhotoImage(file="image.png")
window.iconphoto(True, icon)
window.config(background="cyan")

# LABEL
# label = Label(
#     window,
#     text="Bro do you even code?",
#     font=("Arial", 40, "bold"),
#     fg="#00FF00",
#     bg="black",
#     relief=RAISED,
#     bd=10,
#     padx=10,
#     pady=20,
#     image=icon,
#     compound="bottom",
# )
# label.pack()

# BUTTON
# count = 0
# def click():
#     global count
#     count += 1
#     print(count)
# button = Button(
#     window,
#     text="click me",
#     fg="#00FF00",
#     bg="black",
#     activeforeground="#00FF00",
#     activebackground="black",
#     command=click,
#     image=icon,
#     compound="bottom",
#     state=ACTIVE,
#     font=("Comic Sans", 30),
# )
# button.pack()


# ENTRY
# text = ""
# entry = Entry(window, textvariable=text, fg="black", bg="white")
# entry.insert(0, "password")
# entry.config(show="*")
# entry.pack(side=LEFT)
# def submit():
#     print(entry.get(), "submitted")
#     entry.delete(0, END)
# def backspace():
#     entry.delete(len(entry.get()) - 1, END)
# def delete():
#     entry.delete(0, END)
# backspace = Button(window, text="backspace", command=backspace)
# delete = Button(window, text="delete", command=delete)
# submit = Button(window, text="submit", command=submit)
# backspace.pack(side=RIGHT)
# delete.pack(side=RIGHT)
# submit.pack(side=RIGHT)

# CHECKBOX variable, onvalue, offvalue, IntVar, StringVar, BooleanVar
# checkList = ["Pizza", "Fries", "Burger"]
# pizzamark = IntVar()
# friesmark = IntVar()
# burgermark = IntVar()
# def var_value(food):
#     if food == "Pizza":
#         return pizzamark
#     if food == "Fries":
#         return friesmark
#     if food == "Burger":
#         return burgermark
# for i in checkList:
#     check = Checkbutton(
#         window,
#         text=i,
#         font=("Comic Sans", 20),
#         variable=var_value(i),
#         onvalue=1,
#         offvalue=0,
#         width=20,
#     )
#     check.pack()

# RADIO button loop through list variable and give radio a variable and value parameter indicatoron
# foods = ["Pizza", "Fries", "Burger"]
# selected = IntVar()
# for i in range(len(foods)):
#     radio = Radiobutton(window, text=foods[i], variable=selected, value=i, width=20)
#     radio.pack()
# def click():
#     print(foods[selected.get()])
# button = Button(
#     window,
#     text="submit",
#     state=ACTIVE,
#     font=("Comic Sans", 10),
# )
# button.pack()


# SCALE from, to, length, orient, tickInterval, showValue, throughColor
# scale = Scale(
#     window,
#     from_=0,
#     to=100,
#     length=1000,
#     orient=HORIZONTAL,
#     tickinterval=10,
#     # showvalue=False,
# )
# scale.pack()
# def click():
#     print(scale.get())
# button = Button(
#     window,
#     text="submit",
#     command=click,
# )
# button.pack()

# LIST BOX insert(index, value), listbox.curselection
# food = []
# listed = Listbox(
#     window, width=12, bg="#f74a78", font=("Arial", 20), selectmode=MULTIPLE
# )
# listed.pack()
# listed.config(height=listed.size())
# text = ""
# entry = Entry(window, width=28, textvariable=text)
# entry.pack()
# def submit():
#     print(listed.curselection())
#     print(listed.get(0, END))
#     listed.config(height=listed.size())
# def add():
#     listed.insert(listed.size(), entry.get())
#     entry.delete(0, END)
#     listed.config(height=listed.size())
# def remove():
#     for i in listed.curselection():
#         listed.delete(i)
#     listed.config(height=listed.size())
# Button(
#     window,
#     text="submit",
#     command=submit,
# ).pack()
# Button(
#     window,
#     text="add",
#     command=add,
# ).pack()
# Button(
#     window,
#     text="remove",
#     command=remove,
# ).pack()


# MESSAGEBOXES .showinfo(title, message), .showwarning, .showerror, .askokcancel, .askretrycancel, .askyesno, .askquestion, .askyesnocancel
# TEXT
# MENUBAR
# NEW WINDOW
# COLORCHOOSER
# TABS TTKNOTEBOOK
# FILE DIALOG open read
# GRID

# FRAME
# frame = Frame(window)
# frame.pack()
# Button(frame, text="W", font=("Consolas", 25), width=3).pack(side=TOP)
# Button(frame, text="A", font=("Consolas", 25), width=3).pack(side=LEFT)
# Button(frame, text="S", font=("Consolas", 25), width=3).pack(side=LEFT)
# Button(frame, text="D", font=("Consolas", 25), width=3).pack(side=LEFT)


# PROGRESS_BAR
# from tkinter.ttk import *
# import time
# bar = Progressbar(window, orient=HORIZONTAL, length=300)
# bar.pack(pady=10)
# percentage = StringVar()
# taskv = StringVar()
# def click():
#     download = 0
#     speed = 1
#     GB = 100
#     while download < GB:
#         time.sleep(0.05)
#         bar["value"] += (speed / GB) * 100
#         download += speed
#         percentage.set(str(int((download / GB) * 100)) + "%")
#         taskv.set(str(str(download) + "/" + str(GB) + " GB downloaded"))
#         bar.update_idletasks()
# label = Label(window, textvariable=percentage).pack()
# task_label = Label(window, textvariable=taskv).pack()
# Button(window, text="download", command=click).pack()

# SHAPES
# canvas = Canvas(window, height=500, width=500)
# canvas.pack()
# canvas.create_line(0, 0, 500, 500, width=5, fill="blue")
# canvas.create_line(0, 500, 500, 0, width=5, fill="red")
# canvas.create_rectangle(50, 50, 250, 250, fill="red", width=3)
# points = [250, 0, 500, 500, 0, 500]
# canvas.create_polygon(points, fill="yellow", width=2)
# canvas.create_arc(0, 0, 500, 500, style=PIESLICE, start=-30, extent=180)
# pokeball
# canvas.create_arc(0, 0, 500, 500, style=PIESLICE, extent=180, fill="red", width=7)
# canvas.create_arc(
#     0, 0, 500, 500, style=PIESLICE, extent=180, start=180, fill="white", width=7
# )
# canvas.create_oval(200, 200, 300, 300, fill="white", width=7)

# Key events
# key = StringVar()
# def keyBoard(e):
#     key.set(e.keysym)
# window.bind("<Key>", keyBoard)
# label = Label(window, textvariable=key, font=("Consolas", 20))
# label.pack()

# mouse events
# key = StringVar()
# def mouse(e):sne", e.x, e.y)
# window.bind("<Button-1>", mouse)
# window.bind("<Button-2>", mouse)
# window.bind("<Button-3>", mouse)
# window.bind("<ButtonReleased>", mouse)
# window.bind("<Enter>", mouse)
# window.bind("<Leave>", mouse)
# window.bind("<Motion>", mouse)
# window.config(width=500, height=500)
# label = Label(window, text="mouse", font=("Consolas", 20))
# label.pack()

# drag drop
# def drag_start(e):
#     widget = e.widget
#     widget.startX = e.x
#     widget.startY = e.y
# def dragged(e):
#     widget = e.widget
#     x = widget.winfo_x() - widget.startX + e.x
#     y = widget.winfo_y() - widget.startY + e.y
#     widget.place(x=x, y=y)
# label = Label(window, width=10, height=5)
# label.pack()
# label.bind("<Button-1>", drag_start)
# label.bind("<B1-Motion>", dragged)
# label2 = Label(window, width=10, height=5)
# label2.pack()
# label2.bind("<Button-1>", drag_start)
# label2.bind("<B1-Motion>", dragged)
# window.config(width=500, height=500)


# move image in window
# def get_X(x):
#     if x < 0:
#         return 0
#     elif x > window.winfo_width() - label.winfo_width():
#         return window.winfo_width() - label.winfo_width()
#     else:
#         return x
# def get_Y(y):
#     if y < 0:
#         return 0
#     elif y > window.winfo_height() - label.winfo_height():
#         return window.winfo_height() - label.winfo_height()
#     else:
#         return y
# def move_up(e):
#     x = get_X(label.winfo_x())
#     y = get_Y(label.winfo_y() - 10)
#     label.place(x=x, y=y)
# def move_down(e):
#     x = get_X(label.winfo_x())
#     y = get_Y(label.winfo_y() + 10)
#     label.place(x=x, y=y)
# def move_left(e):
#     x = get_X(label.winfo_x() - 10)
#     y = get_Y(label.winfo_y())
#     label.place(x=x, y=y)
# def move_right(e):
#     x = get_X(label.winfo_x() + 10)
#     y = get_Y(label.winfo_y())
#     label.place(x=x, y=y)
# window.bind("<w>", move_up)
# window.bind("<Up>", move_up)
# window.bind("<a>", move_left)
# window.bind("<Left>", move_left)
# window.bind("<s>", move_down)
# window.bind("<Down>", move_down)
# window.bind("<d>", move_right)
# window.bind("<Right>", move_right)
# label = Label(window, image=icon)
# label.place(x=0, y=0)
# window.config(width=500, height=500)


# move images on canvas
# def move_up(e):
#     canvas.move(image, 0, 10)
# def move_left(e):
#     canvas.move(image, -10, 0)
# def move_down(e):
#     canvas.move(image, 0, 10)
# def move_right(e):
#     canvas.move(image, 10, 0)
# window.bind("<w>", move_up)
# window.bind("<a>", move_left)
# window.bind("<s>", move_down)
# window.bind("<d>", move_right)
# canvas = Canvas(window, width=500, height=500)
# image = canvas.create_image(0, 0, image=icon, anchor=NW)
# canvas.pack()

# alien
# import time
# x_velocity = 2
# y_velocity = 3
# canvas = Canvas(window, width=500, height=500)
# image = canvas.create_image(0, 0, image=icon, anchor=NW)
# canvas.pack()
# while True:
#     coords = canvas.coords(image)
#     if coords[0] > canvas.winfo_width() - icon.width() or coords[0] < 0:
#         x_velocity = -x_velocity
#     if coords[1] > canvas.winfo_height() - icon.height() or coords[1] < 0:
#         y_velocity = -y_velocity
#     canvas.move(image, x_velocity, y_velocity)
#     time.sleep(0.02)
#     window.update()


window.mainloop()  # places window and listens to events
