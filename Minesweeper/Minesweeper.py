import tkinter as tk

def resetGame():
    for widget in window.winfo_children():
        widget.destroy()
    button10 = tk.Button(master=window, text="Beginner", command= lambda: createBoard(8, 8))
    button10.pack()

    button16 = tk.Button(master=window, text="Intermediate", command= lambda: createBoard(16, 16))
    button16.pack()

    button16 = tk.Button(master=window, text="Hard", command= lambda: createBoard(16, 30))
    button16.pack()
    
def click(frame, button):
    info = frame.grid_info()
    x=info["row"]-1
    y=info["column"]
    print(f"({x}, {y})")
    button.config(relief=tk.SUNKEN)
    

def createBoard(x, y):
    for widget in window.winfo_children():
        widget.destroy()

    frame1 = tk.Frame(
        master=window,
        relief=tk.RAISED,
        borderwidth=1
    )
    frame1.grid(row=0,column=0)
    label1 = tk.Label(master=frame1, text="010")
    label1.pack()

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
            button.config(command=lambda frame=frame, button=button: click(frame,button))
            button.pack()

window = tk.Tk()
resetGame()
window.mainloop()