from tkinter import *
import random

root = Tk()
root.title("Colorizer")
root.geometry("1600x1600")
root.configure(bg="pale green")

colors = ["red", "green", "blue", "yellow", "orange", "pink", "purple", "black"]
s = 0
num1 = 7
num2 = 7

score = Label(root, text="Score: 0", font=("Arial", 15), bg="pale green")
score.place(anchor=CENTER, relx=0.05, rely=0.05)

colorN = Label(root, text="black", font=("Arial", 45), bg="pale green")
colorN.place(anchor=CENTER, relx=0.5, rely=0.3)

entry = Entry(root, font=("Arial", 40))
entry.place(anchor=CENTER, relx=0.5, rely=0.4)


def Changer():
    global s, num1, num2
    if colors[num1] == entry.get():
        s += 1
    elif colors[num2] == entry.get():
        s -= 1
    num1 = random.randrange(0, 7)
    num2 = random.randrange(0, 7)
    colorN["text"] = colors[num1]
    colorN["fg"] = colors[num2]
    score["text"] = f"Score: {s}"


btn = Button(
    root, text="Check", bg="pale turquoise", command=Changer, font=("Arial", 36)
)
btn.place(anchor=CENTER, relx=0.5, rely=0.52)

root.mainloop()
