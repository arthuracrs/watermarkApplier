import os
from PIL import Image
from watermark import applyWatermark

import time
start_time = time.time()

watermarkImagePath = './marca.png'
watermarkImage = Image.open(watermarkImagePath)

inputPhotosPath = './inputPhotos'
outputPhotosPath = './outputPhotos'

dirsThatShouldExists = [inputPhotosPath, outputPhotosPath]

for dir in dirsThatShouldExists:
  isExist = os.path.exists(dir)
  if isExist == False:
    os.mkdir(dir)

for imagePath in os.listdir(inputPhotosPath):
    targetImage = Image.open(inputPhotosPath + '/' + imagePath)
    
    applyWatermark(targetImage, watermarkImage).save(
        outputPhotosPath + '/' + imagePath, format="jpeg")

print('done')
print("--- %s seconds ---" % (time.time() - start_time))