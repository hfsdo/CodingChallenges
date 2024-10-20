import tkinter as tk

window = tk.Tk()

#Frame1 = tk.Frame(master=window, height=10)
#Frame1.pack(fill=tk.X, expand=True)

#Frame2 = tk.Frame(master=window)
#Frame2.pack()

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
frame2.grid(row=0,column=4,columnspan=2)
button = tk.Button(master=frame2, text="reset")
button.pack()

frame3 = tk.Frame(
    master=window,
    relief=tk.RAISED,
    borderwidth=1
)
frame3.grid(row=0,column=9)
label2 = tk.Label(master=frame3, text="000")
label2.pack()



for i in range(10):
    for j in range(10):
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
        button.pack()




window.mainloop()