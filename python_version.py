import tkinter as tk
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Greetings willage people!!!!")
root.geometry("800x400")
root.resizable(True, False)

photo = ImageTk.PhotoImage(Image.open("Halle.jpg"))
root.iconphoto(False, photo)

greetings = tk.Label(root, text="Welcome to the Tkinter tutorial!")
greetings.pack()

root.mainloop()
