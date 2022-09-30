#Author: Yoshiki Hoshinaga
#
#Date:June 9
#

def invert(filename):
    """ loads a PNG image from the file with the specified filename
        and creates a new image in which the colors of the pixels are
        inverted.
        input: filename is a string specifying the name of the PNG file
               that the function should process.
        No value is returned, but the new image is stored in a file
        whose name is invert_filename, where filename is the name of
        the original file.
    """
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)

    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()

    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r, c)            
            red = rgb[0]
            green = rgb[1]
            blue = rgb[2]

            # invert the colors of the pixel at row r, column c
            new_rgb = [255 - red, 255 - green, 255 - blue]
            img.set_pixel(r, c, new_rgb)

    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename = 'invert_' + filename
    img.save(new_filename)


def brightness(rgb):
    """ takes the RGB values of a pixel (an [R, G, B] list) and returns a value
        between 0 and 255 that represents the brightness of that pixel.
    """
    red = rgb[0]
    green=rgb[1]
    blue = rgb[2]
    return (21*red + 72*green + 7*blue) // 100

### PUT YOUR WORK FOR PROBLEM 4 BELOW. ###
#part1
def grayscale(filename):
    # create an image object for the image stored in the
    # file with the specified filename
    img=load_image(filename)
    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    # process the image, one pixel at a time
    for x in range(0,img.get_height()):
        for y in range(0,img.get_width()):
            # get the RGB values of the pixel at row r, column c
            rgb=img.get_pixel(x,y)
            brightness(rgb)
            #Call function and saving result into new result called new_vals
            new_vals=brightness(rgb)
            #Need to create pixel as 1 list contains 3 nums
            new_pixel=[new_vals,new_vals,new_vals]
            img.set_pixel(x,y,new_pixel)
    # save the modified image, using a filename that is based on the
    # name of the original file.            
    new_filename='gray_'+ filename
    img.save(new_filename)
    

#2

def bw(filename, threshold):
    # create an image object for the image stored in the
    # file with the specified filename
    img=load_image(filename)
    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    bw_image=img
    # process the image, one pixel at a time
    for r in range(0,img.get_height()):
        for c in range(0,img.get_width()):
            # get the RGB values of the pixel at row r, column c
            rgb=img.get_pixel(r,c)
            if (brightness(rgb) > threshold):
                img.set_pixel(r,c,[255,255,255])
            else:
                img.set_pixel(r,c,[0, 0, 0])
    # save the modified image, using a filename that is based on the
    # name of the original file. 
    new_filename='bw_'+filename
    img.save(new_filename)

#3

def fold_diag(filename):
    # create an image object for the image stored in the
    # file with the specified filename
    img=load_image(filename)
    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    # process the image, one pixel at a time
    for r in range(0,img.get_height()):
        for c in range(0,img.get_width()):
            # get the RGB values of the pixel at row r, column c
            rgb=img.get_pixel(r,c)
            if (c<r):
                img.set_pixel(r,c,[255,255,255])
            else:
                img.set_pixel(r,c,rgb)
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename='fold_'+filename
    img.save(new_filename)

#test
if __name__=='__main__':
    invert('test.png')
    grayscale('spam.png')
    bw('spam.png',100)
    fold_diag('spam.png')
