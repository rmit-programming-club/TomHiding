from PIL import Image


def split(number, parts):
    size = int(8 / parts)
    segments = []
    for i in range(parts):
        segments.append((number & 3 << i * size) >> (i * size))
    return segments


def flatten(pixel_array):
    return [rgb_value for pixel in pixel_array for rgb_value in pixel]


def replace_last_bits(number, replacement, bit_count):
    return ((number >> bit_count) << bit_count) + replacement


if __name__ == "__main__":
    # Opens an image in RGB "tuples" [(143, 35, 29), (255, 115, 0) ... ]
    cover = Image.open("IMG_20180501_145013.jpg")
    message_data = iter(Image.open("mini_tom.png").getdata())
    result_image = Image.new("RGB", cover.size)
    current_pixel_data = []
    message_ended = False
    result_data = []
    for pixel in cover.getdata():
        new_tuple = []
        if not message_ended:
            try:
                for value in pixel:
                    # If we have run out of data to write with the current message pxel
                    if len(current_pixel_data) == 0:
                        # Generate new data from the next pixel
                        message_pixel = message_data.__next__()
                        current_pixel_data = flatten([split(value, 4) for value in message_pixel])

                    # Get the next piece of message data
                    data = current_pixel_data[0]
                    current_pixel_data = current_pixel_data[1:]

                    # Hide it in the cover image
                    new_data = replace_last_bits(value, data, 2)
                    new_tuple.append(new_data)
                # append the new pixel
                result_data.append(tuple(new_tuple))
            except StopIteration:
                # Finished the message! quickly copy the next few values for the pixel
                message_ended = True
                for value in pixel[len(new_tuple):]:
                    new_tuple.append(value)
                result_data.append(tuple(new_tuple))
        else:
            # No message to write, just copy over cover
            result_data.append(pixel)

    result_image.putdata(result_data)
    result_image.save("result.png")

    print("Success")
