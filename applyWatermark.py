import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from tkinter import messagebox
from tkinter import Label
import os
from PIL import Image, ImageTk
from GifFom import GifFom
from watermark import applyWatermark

watermarkImagePath = "Selecione o png da marca d'agua"
inputPhotosPath = 'Selecione uma pasta'
outputPhotosPath = 'Selecione um pasta'

def loadWaterMarkImage(label):
    global watermarkImagePath
    global root
    filetypes = (
        ('text files', '*.png'),
        ('All files', '*.*')
    )

    watermarkImagePath = fd.askopenfilename(
        title='Open a file',
        initialdir='../',
        filetypes=filetypes)
    label.config(text=watermarkImagePath)


def loadInputPhotosPath(label):
    global inputPhotosPath

    inputPhotosPath = fd.askdirectory(
        title='Selecione a pasta das fotos', initialdir='../')
    label.config(text=inputPhotosPath)


def loadOutputPhotosPath(label):
    global outputPhotosPath

    outputPhotosPath = fd.askdirectory(
        title="Selecione outra pasta para as fotos com marca d'agua", initialdir='../')
    label.config(text=outputPhotosPath)


def apply(gifConclusion):
    global watermarkImagePath
    global inputPhotosPath
    global outputPhotosPath

    if watermarkImagePath == '':
        messagebox.showerror("Error", "watermarkImagePath")
        return

    if inputPhotosPath == '':
        messagebox.showerror("Error", "inputPhotosPath")
        return

    if outputPhotosPath == '':
        messagebox.showerror("Error", "outputPhotosPath")
        return

    watermarkImage = Image.open(watermarkImagePath)

    for imagePath in os.listdir(inputPhotosPath):
        targetImage = Image.open(
            inputPhotosPath + '/' + imagePath)

        applyWatermark(targetImage, watermarkImage).save(
            outputPhotosPath + '/' + imagePath, format="jpeg")
    
    gifConclusion.animate()


def createMainWindow():
    global watermarkImagePath
    global inputPhotosPath
    global outputPhotosPath
    # create the root window
    root = tk.Tk()
    root.title('Watermark 2000')
    root.resizable(False, False)
    root.geometry('900x700')

    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=20)

    # load Water Mark Image Button
    waterMarkImagePathText = ttk.Label(root, text=watermarkImagePath)
    waterMarkImagePathText.grid(column=1, row=0, sticky=tk.W, padx=5, pady=5)
    loadWaterMarkImageButton = ttk.Button(
        root,
        text='Escolher imagem',
        command=lambda: loadWaterMarkImage(waterMarkImagePathText)
    )
    loadWaterMarkImageButton.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
    
    loadInputPhotosPathText = ttk.Label(root, text=inputPhotosPath)
    loadInputPhotosPathText.grid(column=1, row=1, sticky=tk.W, padx=5, pady=5)
    loadInputPhotosPathButton = ttk.Button(
        root,
        text='Escolher pasta',
        command=lambda: loadInputPhotosPath(loadInputPhotosPathText)
    )
    loadInputPhotosPathButton.grid(
        column=0, row=1, sticky=tk.W, padx=5, pady=5)

    loadOutputPhotosPathText = ttk.Label(root, text=outputPhotosPath)
    loadOutputPhotosPathText.grid(column=1, row=2, sticky=tk.W, padx=5, pady=5)
    loadOutputPhotosPathButton = ttk.Button(
        root,
        text='Escolher pasta',
        command=lambda: loadOutputPhotosPath(loadOutputPhotosPathText)
    )
    loadOutputPhotosPathButton.grid(
        column=0, row=2, sticky=tk.W, padx=5, pady=5)

    label1 = GifFom(root, './jo.gif')
    label1.gifLabel.grid(
        column=1, row=5, sticky=tk.W, padx=5, pady=5)

    applyBUtton = ttk.Button(
        root,
        text='Apply',
        command=lambda: apply(label1)
    )
    applyBUtton.grid(column=1, row=4, sticky=tk.SE, padx=5, pady=5)

    # run the application
    root.mainloop()


if __name__ == "__main__":
    createMainWindow()
