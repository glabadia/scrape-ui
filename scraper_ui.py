import tkinter as tk
from init import instructions

root = tk.Tk()
root.geometry('300x180')

search = tk.StringVar(None, "fast")  # type of search
houses = tk.StringVar(None, "sorted")  # type of houses


frame1 = tk.Frame(root, bd=1, relief="solid")
frame1.pack()

frame2 = tk.Frame(root, bd=1, relief="solid")
frame2.pack()

frame3 = tk.Frame(root, bd=1, relief="solid")
frame3.pack()


def display():
    print(f"You chose: speed: {search.get()}, houses: {houses.get()}")
    return instructions({"search": search.get(), "houses": houses.get()})


# Search
tk.Radiobutton(frame1,
               text="Fast Search",
               padx=10,
               variable=search,
               value="fast").pack(anchor=tk.W)
# tk.Radiobutton(frame1,
#                text="Standard Search",
#                padx=10,
#                variable=search,
#                value="slow").pack(anchor=tk.W)

# Auction Houses
tk.Radiobutton(frame2,
               text="Active Auction House/s",
               padx=10,
               variable=houses,
               value="active").pack(anchor=tk.W)
tk.Radiobutton(frame2,
               text="Sorted Auction House/s",
               padx=10,
               variable=houses,
               value="sorted").pack(anchor=tk.W)
tk.Radiobutton(frame2,
               text="One Auction House/s",
               padx=10,
               variable=houses,
               value="one").pack(anchor=tk.W)

b = tk.Button(frame3, text="Start", command=display)
b.pack(side=tk.LEFT)
b = tk.Button(frame3, text="Quit", command=quit)
b.pack(side=tk.LEFT)

root.mainloop()
