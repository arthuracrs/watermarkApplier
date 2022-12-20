import os
from PIL import Image

def applyWatermark(im1, im2):
    im1W = im1.size[0]
    im1H = im1.size[1]

    im2 = im2.resize((im1W, im1H))

    im2W = im2.size[0]
    im2H = im2.size[1]

    im1.paste(im2, (int((im1W/2 - im2W/2)),
              int((im1H/2 - im2H/2))), im2)

    return im1

watermarkImagePath = './watermark.png'
watermarkImage = Image.open(watermarkImagePath).convert("RGBA")

inputPhotosPath = './inputPhotos'
outputPhotosPath = './outputPhotos'

dirsThatShouldExists = [inputPhotosPath, outputPhotosPath]

for dir in dirsThatShouldExists:
  isExist = os.path.exists(dir)
  if isExist == False:
    os.mkdir(dir)

for imagePath in os.listdir(inputPhotosPath):
    targetImage = Image.open(inputPhotosPath + '/' + imagePath).convert("RGBA")
    
    applyWatermark(targetImage, watermarkImage).save(
        outputPhotosPath + '/' + imagePath, format="png")