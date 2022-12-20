import tkinter as tk
from PIL import Image

class GifFom:
    def __init__(self, tkContainer, gifImagePath):
        self.__tkContainer = tkContainer

        self.__gifImage = Image.open(gifImagePath)

        self.__frames = self.__gifImage.n_frames

        self.__imageObject = [tk.PhotoImage(
            file=gifImagePath, format=f"gif -index {i}") for i in range(self.__frames)]

        self.gifLabel = tk.Label(self.__tkContainer, image="")

    def animate(self, count=0):
        newImage = self.__imageObject[count]
        self.gifLabel.configure(image=newImage)
        count += 1
        if count == self.__frames:
            count = 0
        self.__tkContainer.after(16, lambda: self.animate(count))