from PIL import Image


if __name__ == "__main__":
    hidden = Image.open("result.png")
    dimensions = Image.open("mini_tom.png").size

    result_data = []

    i = 0
    rgb_tuple = []
    value_elements = []
    for pixel in hidden.getdata():
        # Do the rest of the pixels contain no message?
        if i >= dimensions[1] * dimensions[1] * 4:
            break
        
        # Get the data at the end of the pixel
        for value in pixel:
            message = value % 4
            value_elements.append(message)
        
            # If we have enough for a RGB Value, place it in the tuple
            if len(value_elements) == 4:
                rgb_tuple.append(value_elements[0] + (value_elements[1] << 2) + (value_elements[2] << 4) + (value_elements[3] << 6))
                value_elements = []

            # If we have enough for a pixel, add it to the end data
            if len(rgb_tuple) == 3:
                result_data.append(tuple(rgb_tuple))
                rgb_tuple = []

        i += 1

    result_image = Image.new("RGB", dimensions)
    result_image.putdata(result_data)
    result_image.save("back.png")

    print("Success")
