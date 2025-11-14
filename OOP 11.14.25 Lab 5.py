
import tkinter as tk
from tkinter import Button


class Queue:
    def __init__(self):
        self.element = []

    def enqueue(self, item):
        self.element.append(item)

    def dequeue(self):
        self.element.pop(0)

    def display_queue(self):
        return " ".join(self.element) \
            if self.element \
            else "Queue is empty"


# Create the main window
top = tk.Tk()
top.geometry("600x600")
top.title("Queue GUI")

# Create a Queue instance
queue = Queue()

answer = tk.Text(width=35, height=2)

# Text box to show output
answer.place(x=200, y=100)

# Entry box for enqueue input
entry = tk.Entry(top, width=30, font=("Arial", 12))
entry.place(x=200, y=200)


def show(action):
    answer.delete("1.0", tk.END)

    if action == "Create Queue":
        queue.elements = []
        answer.insert(tk.END, "New queue created.")

    elif action == "Enqueue":
        item = entry.get()
        if item:
            queue.enqueue(item)
            answer.insert(tk.END, f"Enqueued: {item}")
            entry.delete(0, tk.END)
        else:
            answer.insert(tk.END, "Please enter an element to enqueue.")

    elif action == "Dequeue":
        item = queue.dequeue()
        if item:
            answer.insert(tk.END, f"Dequeued: {item}")
        else:
            answer.insert(tk.END, "Dequeued first item.")

    elif action == "Display Queue":
        answer.insert(tk.END, f"Queue: {queue.display_queue()}")


# Buttons
B1 = Button(top, text="Create Queue", width=10, height=5, command=lambda: show("Create Queue"))
B1.place(x=100,y=150)

B2 = Button(top, text="Enqueue", width=10, height=5, command=lambda: show("Enqueue"))
B2.place(x=100,y=250)

B3 = Button(top, text="Dequeue", width=10, height=5, command=lambda: show("Dequeue"))
B3.place(x=100,y=350)

B4 = Button(top, text="Display Queue", width=10, height=5, command=lambda: show("Display Queue"))
B4.place(x=100,y=450)


top.mainloop()


import tkinter as tk
from tkinter import Button

class Stack:
    def __init__(self):
        self.element = []

    def push(self, item):
        self.element.append(item)

    def pop(self):
        self.element.pop()

    def display_Stack(self):
        return " ".join(self.element) \
            if self.element \
            else "Queue is empty"


# Create the main window
top = tk.Tk()
top.geometry("600x600")
top.title("Queue GUI")

# Create a Queue instance
stack = Stack()

answer = tk.Text(width=35, height=2)

# Text box to show output
answer.place(x=200, y=100)

# Entry box for stack input
entry = tk.Entry(top, width=30, font=("Arial", 12))
entry.place(x=200, y=200)


# noinspection PyUnreachableCode
def show(action):
    answer.delete("1.0", tk.END)

    if action == "Create Stack":
        stack.element = []
        answer.insert(tk.END, "New stack created.")

    elif action == "Push":
        item = entry.get()
        if item:
            stack.push(item)
            answer.insert(tk.END, f"Pushed: {item}")
            entry.delete(0, tk.END)
        else:
            answer.insert(tk.END, "Please enter an element to push.")

    elif action == "Pop":
        item = stack.pop()
        if item:
            answer.insert(tk.END, f"Removed: {item}")
        else:
            answer.insert(tk.END, f"Removed last item.")

    elif action == "Display Stack":
        answer.insert(tk.END, f"Stack: {stack.display_Stack()}")


# Buttons
B1 = Button(top, text="Create Stack", width=10, height=5, command=lambda: show("Create Stack"))
B1.place(x=100,y=150)

B2 = Button(top, text="Push", width=10, height=5, command=lambda: show("Push"))
B2.place(x=100,y=250)

B3 = Button(top, text="Pop", width=10, height=5, command=lambda: show("Pop"))
B3.place(x=100,y=350)

B4 = Button(top, text="Display Stack", width=10, height=5, command=lambda: show("Display Stack"))
B4.place(x=100,y=450)


top.mainloop()