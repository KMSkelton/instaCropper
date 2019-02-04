from PIL import Image
import os
from os import listdir
from os.path import isfile, join

def setup_crop(file_to_crop):
  og = Image.open(file_to_crop)
  og.show()
  correct = input('Is this is the correct image?')
  if correct == 'n':
    setup_crop()
  
  if og.width == og.height:
    print("This image is already a square")
  
  if og.width != og.height:
    orientation = input('Is this image in the correct orientation? ')
    if orientation == 'n':
      rotate_image(og, file_to_crop)
    else: 
      where_to_crop(og, file_to_crop)

def where_to_crop(og, file_to_crop):
  '''
  top, left, bottom and right refer to the pixel that creates the indicated side.
  Because I want to automatically create the box, right will create an edge that is based on the left side. 
  if the picture is portrait the width is less than the height; landscape is vise versa
  Let's give portrait dimensions of 800 x 1000 for ease of math.

  Starting the left at 100 means there are 700 pixels remaining in the image. We cannot start the
  right side at left-side plus width because that it outside of the image. So right must be at least
  width minus left-side; this is called the calculated_side. The calculated side is used both 
  horizontally and vertically (from the top) to create the square that instagram wants.
  To use the same crop on the other side of the same dimension, remove the crop again or don't account
  for the distance of the first crop. Not accounting for the distance is "less math". 

  '''

  width, height = og.size
  short_side = min(width, height)
  try: 
    left = int(input('Left start for crop. Default is 0: ')) 
  except ValueError:
    left = 0
  try:
    top = int(input('Top start for crop. Default is 0: '))
  except ValueError:
    top = 0
  if width < height:
    calculated_side = short_side - left 
  else:     
    calculated_side = short_side - top 
  right_crop_option = input("Do you want the same crop on the right side? (Default is no): ") or 'no'
  if right_crop_option == 'no' or right_crop_option == 'n':
    right = (calculated_side + left) # from above note: 700 + 100 = 800px or the right edge of the pic
  else:
    right = calculated_side # right crop will be at 700px from the left edge of the original pic
  bottom_crop_option = input("Do you want the same crop on the bottom side? (Default is no): ") or 'no'
  if bottom_crop_option == 'no' or bottom_crop_option == 'n':
    bottom = (calculated_side + top) # from above 
  else:
    bottom = calculated_side

  cropped_og = og.crop((left, top, right, bottom))
  cropped_og.show()

  save_or_trash = input('Does this look like what you wanted? ')
  if save_or_trash == 'n':
    where_to_crop(og, file_to_crop)
  else: 
    og = cropped_og
    save_cropped_file(og, file_to_crop)

def save_cropped_file(og, file_to_crop):
  file_path = os.path.dirname(os.path.abspath(file_to_crop))
  file_name = os.path.basename(file_to_crop)
  prefix = input('What prefix do you want for this file? (Default is "insta_": ') or "insta_"
  new_path = input('Would you like to save this in a new directory? (Default is yes) ') or 'yes'
  if new_path == 'y' or new_path == 'yes':
    added_path = input('What would you like to call this new subdirectory? (Default is "insta") ') or 'insta'
    os.makedirs(file_path + '/' + added_path, exist_ok=True)
    file_path = os.path.join(file_path, added_path)
    print(f'new file path is: {file_path}')
  og.save(f'{file_path}/{prefix}{file_name}')
  print("File save complete. You may need to refresh your directory to see the changes.")

def rotate_image(og, file_to_crop):
  dir = input('Does this need to be rotated right, left, or flipped? ') or 'none'
  if dir == 'r' or dir =='right':
    new_og = og.transpose(Image.ROTATE_270)
  elif dir ==  'l' or dir == 'left':
    new_og = og.transpose(Image.ROTATE_90)
  elif dir == 'f' or dir == 'flipped':
    new_og = og.transpose(Image.ROTATE_180)
  else:
    where_to_crop(og, file_to_crop)
  new_og.show()
  correct = input('Does this look correct?')
  if correct == 'n':
    rotate_image(og, file_to_crop)
  else:
    og = new_og
    where_to_crop(og, file_to_crop)

def batch_process(dir_to_crop):
  only_photos = [f for f in listdir(dir_to_crop) if isfile(join(dir_to_crop, f))]
  for photo in only_photos:
    to_crop = dir_to_crop + "/" + photo
    setup_crop(to_crop)

if __name__ == '__main__':
  batch_or_single = input('Are you processing a -directory- or a -single- file? ') or 'single'
  if batch_or_single == 'directory' or batch_or_single == 'd' or batch_or_single == 'D':
    dir_to_crop = input('Full directory path: ')
    batch_process(dir_to_crop)
  else:
    to_crop = input('Which photo needs cropping? Include extension: ')
    setup_crop(to_crop)