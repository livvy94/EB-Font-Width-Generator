from PIL import Image
from yaml import dump 
import time

verbose = False
infile = "0.png"
outfile = "0_widths.yml"
empty_char_value = 2

main_font_image = Image.open(infile)
white = 0  # aka the first palette value. CoilSnake fonts are usually 0 [White], 1 [Black], 2 [Blue], 3 [Blue], etc. [junk data]


def main():
    validate_image_size(main_font_image)

    list_of_lengths = []
    currentX = 0
    currentY = 0

    # loop through the pixels of each character
    while currentY < 128:  # the loop ends when it reaches the bottom of the image
        length = get_character_length(currentX, currentY)
        list_of_lengths.append(length)

        currentX = currentX + 16
        if currentX >= 256:
            currentY = currentY + 16  # move down a row
            currentX = 0  # move back to the left-hand side of the image

    save_yaml_file(list_of_lengths)
    print("Done!")


###############
# Methods
def get_character_length(x, y):
    starting_point = [x, y]
    x = x + 15  # start at the right-hand side of the character

    while x > starting_point[0]:
        if pixel_is_white(x, y):  # find the rightmost pixel
            if verbose:
                print("Found one at (" + str(x) + ", " + str(y) + ")!")
                time.sleep(3)
            return (x + 1) - starting_point[0]

        y = y + 1  # go down a pixel and look again

        if y > starting_point[1] + 15:  # if we've reached the bottom of the 16px square
            y = starting_point[1]  # go back to the top
            x = x - 1  # move left one pixel and continue searching

        if verbose:
            time.sleep(0.05)

    if verbose:
        print("(Nothing found, returning a length of 2)")
        time.sleep(3)
    return empty_char_value  # For characters with no pixels in them, like space


def pixel_is_white(x, y):
    pixel = main_font_image.getpixel((x, y))
    if verbose:
        print("Value for (" + str(x) + ", " + str(y) + "): " + str(pixel))

    return pixel == white


def save_yaml_file(result):
    data = dump(result, default_flow_style=False)
    print(data)

    with open(outfile, "w") as file:
        file.write(data)


def validate_image_size(image):
    if image.size[0] == 256 and image.size[1] == 128:
        return True
    else:
        print("This isn't a CoilSnake main font file!")
        exit()


if __name__ == "__main__":
    main()
