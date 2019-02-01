from PIL import Image
import os
from os import listdir
from os.path import isfile, join

def setup_crop(file_to_crop):
  print(f'SETUP CROP to crop ===== {file_to_crop}')
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
  calculated_side = short_side - left - left
  right = (calculated_side + left)
  bottom = (calculated_side + top)

  cropped_og = og.crop((left, top, right, bottom))
  cropped_og.show()

  save_or_trash = input('Does this look like what you wanted? ')
  if save_or_trash == 'n':
    where_to_crop(og, file_to_crop)
  else: 
    og = cropped_og
    save_cropped_file(og, file_to_crop)

def save_cropped_file(og, file_to_crop):
  print(f'OG ====== {og}')
  print(f'save cropped to_crop == {file_to_crop}')
  file_path = os.path.dirname(os.path.abspath(file_to_crop))
  file_name = os.path.basename(file_to_crop)
  print(f'FILEPATH IS: {file_path}')
  print(f'FILE NAME IS: {file_name}')
  prefix = input('What prefix do you want for this file? (Default is "insta_": ') or "insta_"
  og.save(f'{file_path}/{prefix}{file_name}')
  print("File save complete.")

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
  correct = input('Does this look right?')
  if correct == 'n':
    rotate_image(og, file_to_crop)
  else:
    og = new_og
    where_to_crop(og, file_to_crop)

def batch_process(dir_to_crop):
  only_photos = [f for f in listdir(dir_to_crop) if isfile(join(dir_to_crop, f))]
  for photo in only_photos:
    print(f'photo info? {dir_to_crop}/{photo}')
    to_crop = dir_to_crop + "/" + photo
    print(f'BATCH PROCESS TO CROP  {to_crop}')
    setup_crop(to_crop)

if __name__ == '__main__':
  batch_or_single = input('Are you processing a -directory- or a -single- file? ') or 'single'
  if batch_or_single == 'directory' or batch_or_single == 'd' or batch_or_single == 'D':
    dir_to_crop = input('Full directory path: ')
    batch_process(dir_to_crop)
  else:
    to_crop = input('Which photo needs cropping? Include extension: ')
    setup_crop(to_crop)