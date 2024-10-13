import tkinter as tk

window = tk.Tk()

Frame1 = tk.Frame(master=window, height=10)
Frame1.pack(fill=tk.X, expand=True)

Frame2 = tk.Frame(master=window)
Frame2.pack()

label1 = tk.Label(master=Frame1, text="010")
label1.pack(fill=tk.Y, side=tk.LEFT, expand=False)

button = tk.Button(master=Frame1, text="reset")
button.pack(fill=tk.Y, side=tk.TOP, expand=False)

label2 = tk.Label(master=Frame1, text="000")
label2.pack(fill=tk.Y, side=tk.RIGHT, expand=False)

for i in range(10):
    for j in range(10):
        frame = tk.Frame(
            master=Frame2,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j)
        #label = tk.Label(master=frame, text=f"row {i}\nColumn {j}")
        #label.pack()
        button = tk.Button(
            master=frame,
            text = f"({i},{j})"
        )
        button.pack()




window.mainloop()