from PIL import Image #Install this with `pip install pillow`
#I'm using the VS Code extension `Remote - Containers` to use Docker as my development environment

def main():
    main_font_image = Image.open("0.png")
    if (not size_is_valid(main_font_image)):
        print("This isn't a CoilSnake main font file!")
        return
    
    #Get the palette values?

    #Each character is a 16x16 bitmap
    #loop through each, starting from the right-hand side and moving downwards, looking for the first white pixel
    #Use this maybe? https://pillow.readthedocs.io/en/stable/reference/PixelAccess.html

###############
# Methods
def size_is_valid(image):
    if(image.size[0] == 256 or image.size[1] == 128):
        return True
    else:
        return False

if __name__ == "__main__":
    main()