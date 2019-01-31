# instaCropper
Python tool to rotate and crop photos for Instagram. As a social media manager for a theatre group I find that most talent will submit portrait size images (vert or horiz). Instagram hates those. 

While I -can- crop to size by hand... why when I can Python? The eventual idea is for this to batch-process horizontal and vertical images, and crop those equally well. 


# Use
instaCropper was built for OSX and Python3. 

Open finder

Click once on the image that needs to be prepped for Instagram

option + CMD + c (this copies the path and the filename)

In terminal: 

`>>> python3 cropper.py`

paste the path into the terminal

confirm that this is the photo

Pillow does odd things with image orientation. If the photo is not the in the orientation you expect, type n. You'll be asked which direction the image needs to be rotated. You must type the entire word: right, left, flipped

Enter how many pixels from the left edge you want to start the crop. InstaCropper will automatically figure the same distance from the right edge.

Enter how many pixels from the top edge of the image you want to start cropping. InstaCropper uses the distance calculated horizontally to figure the height of the crop square. 

InstaCropper will confirm this is what you expected. If not, try again. 


I prefer to prefix my images with "insta_" so I can keep them grouped. You may want something else and you're welcome to type that here. You are also able to see the directory and original filename, which is essentially the destination for the cropped image. 