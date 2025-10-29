import tkinter

root = tkinter.Tk()
root.resizable(False,False)

## create canvas
myCanvas = tkinter.Canvas(root, bg = "white", height = 500, width = 500)

## creates oval
shape1 = myCanvas.create_oval(200,400,100,100, fill = "blue")

## creates rectangle
shape2 = myCanvas.create_rectangle(50, 80, 100, 100, fill = "pink")

## create line
shape3 = myCanvas.create_line(1000,75, 400, 400, fill = "yellow")

## create arc (basically a half circle)
shape4 = myCanvas.create_arc(50, 180, 150, 250, start = 0, extent = 180, fill = "green")

myCanvas.pack()
root.mainloop()