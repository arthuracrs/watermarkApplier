import tkinter as tk
from PIL import Image


class GifFom:
    def __init__(self, tkContainer, gifImagePath):
        self.tkContainer = tkContainer

        self.gifImagePath = gifImagePath
        self.gifImage = Image.open(gifImagePath)

        self.frames = self.gifImage.n_frames

        self.imageObject = [tk.PhotoImage(
            file=gifImagePath, format=f"gif -index {i}") for i in range(self.frames)]

        self.gifLabel = tk.Label(self.tkContainer, image="")
        self.gifLabel.place(
            x=155, y=20, width=self.gifImage.size[0], height=self.gifImage.size[1])

    def animate(self, count=0):
        newImage = self.imageObject[count]
        self.gifLabel.configure(image=newImage)
        count += 1
        if count == self.frames:
            count = 0
        self.tkContainer.after(16, lambda: self.animate(count))


root = tk.Tk()
root.title('Watermark 2000')
# root.resizable(False, False)
root.geometry('900x700')

gifImagePath = './jo.gif'


gif = GifFom(root, gifImagePath)

gif.animate()

root.mainloop()
