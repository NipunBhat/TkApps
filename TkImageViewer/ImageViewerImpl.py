from pathlib import Path
from PIL import ImageTk,Image
import os
class CImageViewerImpl:
    def __init__(self) -> None:
        self.idx = 0
        self.imgdirPath = Path(r"C:\Users\Nipun Bhat\Documents\TKApps\Images")
        self.listImages = self.listImages = os.listdir(self.imgdirPath)
        for indx,path in enumerate(self.listImages):
            self.listImages[indx] = Path.joinpath(self.imgdirPath, path)
     
    def curImgPath(self) -> Path:
        return self.listImages[self.idx]
       
    def nextImagePath(self) -> Path:
        if self.idx == len(self.listImages) - 1:
            self.idx = 0
        else: 
            self.idx += 1
        return self.listImages[self.idx+1]

    def prevImagePath(self) -> Path:
        if self.idx == 0:
            self.idx = len(self.listImages) - 1
        else:
            self.idx -= 1
        return self.listImages[self.idx+1]
    