# Import module
from PIL import Image, ImageTk
import tkinter as tk

# Add image file
IMAGE_PATH = 'img2.jpg'
WIDTH, HEIGHT = 800, 600
root = tk.Tk()
root.geometry('{}x{}'.format(WIDTH, HEIGHT))
img = ImageTk.PhotoImage(Image.open(IMAGE_PATH).resize((WIDTH, HEIGHT), Image.ANTIALIAS))
lbl = tk.Label(root, image=img)
lbl.img = img  # Keep a reference in case this code put is in a function.
lbl.place(relx=0.5, rely=0.5, anchor='center')  # Place label in center of parent.
# Create Canvas
button1 = tk.Button(root, text="Exit")
button1.grid(row=0, column=0, pady=10)
button3 = tk.Button(root, text="Start")
button3.grid(row=1, column=0, pady=10)
button2 = tk.Button(root, text="Reset")
button2.grid(row=2, column=0)
# Execute tkinter
root.mainloop()