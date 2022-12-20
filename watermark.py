from PIL import Image


def applyWatermark(photo, mark):
    rotate = False
    photoW = photo.size[0]
    photoH = photo.size[1]

    if photoH >= photoW:
        rotate = True
        photo = photo.rotate(90,  expand = 1)
        photoW = photo.size[0]
        photoH = photo.size[1]

    mark = mark.resize((photoW, photoH))

    markW = mark.size[0]
    markH = mark.size[1]

    photo.paste(mark, (int((photoW/2 - markW/2)),
              int((photoH/2 - markH/2))), mark)

    if rotate:
        photo = photo.rotate(-90,  expand = 1)

    return photo
