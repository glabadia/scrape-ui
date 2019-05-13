import tkinter as tk

root = tk.Tk()
root.title("Python UI Window")
logo = tk.PhotoImage(file="python_logo_small.png")

w1 = tk.Label(root, image=logo).pack(side="right")

explanation = """At present, only GIF and PPM/PGM
formats are supported, but an interface 
exists to allow additional image file
formats to be added easily.
"""
w2 = tk.Label(root,
              justify=tk.LEFT,
              fg="green",
              padx=10,
              text=explanation).pack(side="left")

# w = tk.Label(root, text="Hello Tkinter!")
# w.pack()

root.mainloop()
