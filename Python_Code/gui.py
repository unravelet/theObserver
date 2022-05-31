import tkinter as tk

window = tk.Tk()
window.title('theObserver')
window.state('zoomed')

frame = tk.Frame(master=window, width=150, height=150)

button1 = tk.Button(
    text="Home",
    width=25,
    height=5,
    bg="#467fd7",
    fg="white",
    master=frame
)
button1.pack(side=tk.LEFT)

button2 = tk.Button(
    text="Statistics",
    width=25,
    height=5,
    bg="#e3e6e8",
    fg="black",
    master=frame
)
button2.pack(side=tk.LEFT)

button3 = tk.Button(
    text="Settings",
    width=25,
    height=5,
    bg="#e3e6e8",
    fg="black",
    master=frame
)
button3.pack(side=tk.LEFT)

label = tk.Label(text="Video")
label.pack()

frame.pack(side="bottom", fill=tk.Y)

window.mainloop()