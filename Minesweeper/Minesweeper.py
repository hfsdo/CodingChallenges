import tkinter as tk

def resetGame():
    #TODO: ask size
    for widget in window.winfo_children():
        widget.destroy()
    button10 = tk.Button(master=window, text="Beginner", command= lambda: createBoard(8, 8))
    button10.pack()

    button16 = tk.Button(master=window, text="Intermediate", command= lambda: createBoard(16, 16))
    button16.pack()

    button16 = tk.Button(master=window, text="Hard", command= lambda: createBoard(16, 30))
    button16.pack()
    
def click(button):
    info = button.grid_info()
    #print(f"({info["row"]}, {info["column"]})")
    print(info)
    print((info["row"], info["column"]))

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
                borderwidth=1
            )
            frame.grid(row=i+1, column=j)
            #label = tk.Label(master=frame, text=f"row {i}\nColumn {j}")
            #label.pack()
            button = tk.Button(
                master=frame,
                text = f"({i},{j})"
            )
            button.config(command=lambda button=button: click(frame))
            button.pack()



window = tk.Tk()
resetGame()
window.mainloop()