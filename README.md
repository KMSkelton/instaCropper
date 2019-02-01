# instaCropper
Python tool to rotate and crop photos for instagram

# Use
instaCropper was built for OSX

Open finder

Click once on the image that needs to be prepped for Instagram

option + CMD + c (this copies the path and the filename)

In terminal: 

`>>> python3 cropper.py`

You will be asked whether you want to process a directory or a single file. Directory can be selected by typing d, D, or directory. The default is a single file. 

Paste the path into the terminal. For directories the path copy will not include a trailing /, do not add it. 

You will be asked to confirm that this is the photo you'd like to modify each time.

Pillow does odd things with image orientation. If the photo is not the in the orientation you expect, type n. You'll be asked which direction the image needs to be rotated. You may type the entire word: right, left, flipped, or just the first letter of the transform you want to make. 

Enter how many pixels from the left edge you want to start the crop. InstaCropper will automatically figure the same distance from the right edge.

Enter how many pixels from the top edge of the image you want to start cropping. InstaCropper uses the distance calculated horizontally to figure the height of the crop square. 

InstaCropper will confirm this is what you expected. If not, try again. 


I prefer to prefix my images with "insta_" so I can keep them grouped. You may want something else and you're welcome to type that here. You are also able to see the directory and original filename, which is essentially the destination for the cropped image. 