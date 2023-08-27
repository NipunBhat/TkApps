from tkinter import *
from pathlib import Path
from PIL import ImageTk,Image

root = Tk()
root.title("Image Viewer App")
root.iconbitmap(Path("IconFiles\Python.ico"))

my_img = ImageTk.PhotoImage(Image.open(Path("Images\Mayweather.png")))
imgLabel = Label(image=my_img)
imgLabel.pack()
quitButton = Button(root, text = "ClickToExit", command=root.quit)
quitButton.pack()

root.mainloop()