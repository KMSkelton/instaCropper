# instaCropper
Python tool to rotate and crop photos for Instagram. As a social media manager for a theatre group I find that most talent will submit portrait size images (vert or horiz). Instagram hates those. 

While I -can- crop to size by hand... why when I can Python? The eventual idea is for this to batch-process horizontal and vertical images, and crop those equally well. 


# Use
instaCropper was built for OSX and Python3. "yes" and 0 are the default values, please `return` your way though the prompts if you don't need to make changes.

Open finder.

Single-click the image or directory that needs to be prepped for Instagram.

`option + CMD + c` (this copies the path and the filename)

In terminal: 

`>>> python3 cropper.py`

You will be asked whether you want to process a directory or a single file. Directory can be selected by typing d, D, or directory. The default is a single file. 

`CMD + v` paste the path into the terminal.

If there are files without EXIF data in the directory, instaCropper will notify you and move on to the next file.

instaCropper will ask you to confirm that this is the correct photo. If it is not, instaCropper will apologize and move on.

You will be asked to confirm that this is the photo you'd like to modify each time.

Pillow does odd things with image orientation. If the photo is not the in the orientation you expect, type n. You'll be asked which direction the image needs to be rotated. You may type the entire word: right, left, flipped, or just the first letter of the transform you want to make. 

Enter how many pixels from the left edge you want to start the crop. For portrait images, instaCropper will give you the option to use that same distance on the right side.

Enter how many pixels from the top edge of the image you want to start cropping.For landscape images, instaCropper will ask if you want to use that same distance on the bottom.

instaCropper uses the distances entered and the size of the image to figure the dimensions of the crop square. 

instaCropper will ask you to confirm this is the crop you expected. If not, try again. 


I prefer to prefix my images with "insta_" so I can keep them grouped. You may want something else and you're welcome to type that here. You are also able to see the directory and original filename, which is essentially the destination for the cropped image. 
