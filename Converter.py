from PIL import Image


def im2bin (im):
    return list(im.getdata())

def bin2im (array, sizeX, sizeY):
    im = Image.new("RGB", (sizeX, sizeY))
    im.putdata(array)
    return im

def binify(pixelArray):
    result = []
    for pixel in pixelArray:
        for value in pixel:
            for i in range(4):
                result.append((value & 3 << i * 2)  >> (i * 2))
    return result

cover = Image.open("IMG_20180501_145013.jpg")
hiding_data = Image.open("mini_tom.png")

cover_data = im2bin(cover)
hiding_data = im2bin(hiding_data)

print("Opened files")
bin_hiding = binify(hiding_data)

print("Turned to binary len " + str(len(bin_hiding)))
hidden_data = []

i = 0
for pixel in cover_data:
    
    rgb_data = []
    for value in pixel:
        if i < len(bin_hiding):
            rgb_data.append(int((value // 4) * 4 + bin_hiding[i]))
            i += 1
        else: 
            rgb_data.append(value)
    hidden_data.append(tuple(rgb_data))

result = bin2im(hidden_data, cover.size[0], cover.size[1])
result.save("result.png", "PNG")

print("Success")
