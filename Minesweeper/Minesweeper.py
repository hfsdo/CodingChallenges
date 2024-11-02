import tkinter as tk
import random

def resetGame():
    for widget in window.winfo_children():
        widget.destroy()
    button10 = tk.Button(master=window, text="Beginner", command= lambda: createBoard(8, 8, 10))
    button10.pack()

    button16 = tk.Button(master=window, text="Intermediate", command= lambda: createBoard(16, 16, 40))
    button16.pack()

    button16 = tk.Button(master=window, text="Hard", command= lambda: createBoard(16, 30, 99))
    button16.pack()
    
def click(frame, button, leftclick):
    global grid
    global lost
    global minecount
    global labelMines
    info = frame.grid_info()
    x=info["row"]-1
    y=info["column"]
    print(f"({x}, {y})")
    if lost:
        return
    if not leftclick:
        if button["text"] == "":
            minecount -= 1
            button.config(text="F")
            labelMines.config(text=f"{minecount:03d}")
        else:
            minecount += 1
            button.config(text="")
            labelMines.config(text=f"{minecount:03d}")
    elif button["text"] != "F":
        button.config(relief=tk.SUNKEN, text=grid[x][y])
        count = 0
        if grid[x][y] == "":
            for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    if i >= 0 and i < len(grid):
                        if j >= 0 and j < len(grid[i]):
                            if grid[i][j] == "*":
                                count += 1
            if count != 0:
                button.config(text=count)
        elif grid[x][y] == "*":
            button.config(bg='red')
            lost = True



def rightClick(event):
    print("right")
    button = event.widget
    frame = button.master
    click(frame, button, False)
    
    
def createGrid(x, y, mines):
    global grid
    global lost
    global minecount
    grid = []
    lost = False
    minecount = mines
    for i in range(x):
        row = []
        for j in range(y):
            field = ""#f"{i},{j}"
            row.append(field)
        grid.append(row)
    curmines = 0
    while curmines < mines:
        i = random.randint(0,x-1)
        j = random.randint(0,y-1)
        print(f"{i},{j}")
        if grid[i][j] == "":
            grid[i][j] = "*"
            curmines+=1



def createBoard(x, y, mines):
    createGrid(x,y,mines)
    global labelMines
    
    for widget in window.winfo_children():
        widget.destroy()

    frame1 = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame1.grid(row=0,column=0)
    labelMines = tk.Label(master=frame1, text="010")
    labelMines.pack()

    frame2 = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame2.grid(row=0,column=int(y/2-1),columnspan=2)
    button = tk.Button(master=frame2, text="reset",command=resetGame)
    button.pack()

    frame3 = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame3.grid(row=0,column=y-1)
    label2 = tk.Label(master=frame3, text="000")
    label2.pack()
    for i in range(x): 
        for j in range(y):
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1,
            )
            frame.grid(row=i+1, column=j)
            button = tk.Button(
                master=frame,
                width=2,
                height=1
                #text = f"({i},{j})"
            )
            button.config(command=lambda frame=frame, button=button: click(frame,button,True))
            button.bind("<Button-3>", rightClick)
            button.pack()

window = tk.Tk()
resetGame()
window.mainloop()