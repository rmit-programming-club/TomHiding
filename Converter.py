def im2bin (im):
    return list(im.getdata())

def bin2im (array, sizeX, sizeY):
    im = Image.new("RGB", (sizeX, sizeY))
    im.putdata(array)
    return im
