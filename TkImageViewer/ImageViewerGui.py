from tkinter import *
from pathlib import Path
from PIL import ImageTk,Image
from ImageViewerImpl import *

#Root
root = Tk()
root.title("Image Viewer App")
root.iconbitmap(Path(r"C:\Users\Nipun Bhat\Documents\TKApps\IconFiles\Python.ico"))

#Get First Img
imgViewImpl = CImageViewerImpl()
curImg = ImageTk.PhotoImage(Image.open(imgViewImpl.curImgPath()))
imgLabel = Label(image= curImg)
imgLabel.grid(row="0", column="0", columnspan=3)
  
def OnNextButtonClick():
    global imgLabel  
    
    imgLabel.grid_forget()
    
    nextImg = ImageTk.PhotoImage(Image.open(imgViewImpl.nextImagePath()))
    imgLabel = Label(image= nextImg)
    
    imgLabel.grid(row="0", column="0", columnspan=3)
    
def OnPrevButtonClick():
    global imgLabel  
    
    imgLabel.grid_forget()
    
    prevImg = ImageTk.PhotoImage(Image.open(imgViewImpl.prevImagePath()))
    imgLabel = Label(image= prevImg)
    
    imgLabel.grid(row="0", column="0", columnspan=3)

button_prev = Button(root, text= "<<", command= OnPrevButtonClick)
button_prev.grid(row = "1", column= "0")

button_quit = Button(root, text = "Close", command = root.quit)
button_quit.grid(row="1", column="1")

button_next = Button(root, text = ">>", command=OnNextButtonClick)
button_next.grid(row = "1", column="2")

root.mainloop()