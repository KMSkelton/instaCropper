from PIL import Image
import os.path

def setup_crop(to_crop):
  og = Image.open(to_crop)
  og.show()
  correct = input('Is this is the correct image?')
  if correct == 'n':
    setup_crop()
  
  if og.width == og.height:
    print("This image is already a square")
  
  if og.width != og.height:
    orientation = input('Is this image in the correct orientation? ')
    if orientation == 'n':
      rotate_image(og)
    else: 
      where_to_crop(og)

def where_to_crop(og):
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
    where_to_crop(og)
  else: 
    og = cropped_og
    save_cropped_file(og)

def save_cropped_file(og):
  file_path = os.path.dirname(os.path.abspath(to_crop))
  file_name = os.path.basename(to_crop)
  print(f'FILEPATH IS: {file_path}')
  print(f'FILE NAME IS: {file_name}')
  prefix = input('What prefix do you want for this file? (Default is "insta_": ') or "insta_"
  og.save(f'{file_path}/{prefix}{file_name}')

def rotate_image(og):
  dir = input('Does this need to be rotated right, left, or flipped? ') or 'none'
  if dir == 'right':
    new_og = og.transpose(Image.ROTATE_270)
  elif dir == 'left':
    new_og = og.transpose(Image.ROTATE_90)
  elif dir == 'flipped':
    new_og = og.transpose(Image.ROTATE_180)
  else:
    where_to_crop(og)
  new_og.show()
  correct = input('Does this look right?')
  if correct == 'n':
    rotate_image(og)
  else:
    og = new_og
    where_to_crop(og)


if __name__ == '__main__':
  to_crop = input('Which photo needs cropping? Include extension: ')
  setup_crop(to_crop)