from PIL import Image


def im2bin (im):
    return list(im.getdata())

def bin2im (array, sizeX, sizeY):
    im = Image.new("RGB", (sizeX, sizeY))
    im.putdata(array)
    return im

def unbinify(binArray):
    result = []
    for pixel_index in range(0, len(binArray), 12):
        pixel = binArray[pixel_index: pixel_index + 12]
        pixel_value_list = []
        for value_index in range(0, 12, 4):
            value = pixel[value_index:value_index + 4]
            pixel_value_list.append(value[0] + (value[1] << 2) + (value[2] << 4) + (value[3] << 6))
        result.append(tuple(pixel_value_list))
    return result

hidden = Image.open("result.png")
dimensions = Image.open("mini_tom.png").size

hidden_data = im2bin(hidden)

print("Retreiving")

message = []
for pixel in hidden_data:
    for value in pixel:
        message.append(value % 4)

print("Opened files")
bin_hiding = unbinify(message)[:dimensions[0] * dimensions[1]]

result = bin2im(bin_hiding, dimensions[0], dimensions[1])
result.save("back.png", "PNG")
print("Success")
