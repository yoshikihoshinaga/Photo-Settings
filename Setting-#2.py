#Name; Yoshiki Hoshinaga
#Date; 8/9/2020
# Image processing with loops and image objects



#1
def flip_vert(filename):
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)
    # determine the dimensions of the image
    height = img.get_height()
    width = img.get_width()
    new_img = Image(height,width)
    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(height-r-1,c)
            new_img.set_pixel(r,c,rgb)
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename='flipv_' + filename
    new_img.save(new_filename)
#2
def mirror_vert(filename):
    # create an image object for the image stored in the
    # file with the specified filename
    img=load_image(filename)
    # determine the dimensions of the image
    height=img.get_height()
    width=img.get_width()
    new_img = img
    # process the image, one pixel at a time
    for r in range(height//2,height):
        for c in range(width):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(height-r-1,c)
            img.set_pixel(r,c,rgb)
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename='mirrorv_' + filename
    new_img.save(new_filename)
#3
def reduce(filename):
    # create an image object for the image stored in the
    # file with the specified filename
    img=load_image(filename)
    # determine the dimensions of the image
    height=img.get_height()
    width=img.get_width()
    new_img=Image(height//2,width//2)
    # process the image, one pixel at a time
    for r in range(height):
        for c in range(width):
            if (r%2==1 and c%2==1):
                # get the RGB values of the pixel at row r, column c
                rgb = img.get_pixel(r,c)
                new_img.set_pixel(r//2,c//2,rgb)
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename='reduce_' + filename
    new_img.save(new_filename)
#4
def extract(filename,rmin,rmax,cmin,cmax):
    # create an image object for the image stored in the
    # file with the specified filename
    img = load_image(filename)
    # determine the dimensions of the image
    height=img.get_height()
    width=img.get_height()
    new_img=Image((rmax-rmin),(cmax-cmin))
    # process the image, one pixel at a time
    for r in range(rmin,rmax):
        for c in range(cmin,cmax):
            # get the RGB values of the pixel at row r, column c
            rgb = img.get_pixel(r,c)
            new_img.set_pixel(r-rmin,c-cmin,rgb)
    # save the modified image, using a filename that is based on the
    # name of the original file.
    new_filename='extract_' + filename
    new_img.save(new_filename)

#test
if __name__=='__main__':
    flip_vert('spam.png')
    mirror_vert('spam.png')
    reduce('spam.png')
    extract('spam.png',90, 150, 75, 275)
