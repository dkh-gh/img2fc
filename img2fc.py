import cv2 
import numpy as np 

img = cv2.imread(input('pic: '), 0)
maxScale = int(input('max size: '))
pixScale = .3

width = np.shape(img)[1]
height = np.shape(img)[0]

k = max(width, height) / maxScale

width = int(width / k)
height = int(height / k)

img = cv2.resize(img, (width, height))

out = open('img2fc.txt', 'w')
out.write('сдвиг-влево {}\n'.format(width/2*pixScale))
out.write('сдвиг-вверх {}\n'.format(height/2*pixScale))

for y in range(height):
  lastState = round(img[y][0]/256)
  lineLength = 1
  for x in range(width):
    if round(img[y][x]/256) != lastState or x >= width-1:
      if not lastState: out.write('вправо {}\n'.format(pixScale * lineLength))
      else: out.write('сдвиг-вправо {}\n'.format(pixScale * lineLength))
      lineLength = 1
      lastState = round(img[y][x]/256)
    else:
      lineLength += 1
      
  out.write('сдвиг-вниз {}\n'.format(pixScale))
  out.write('сдвиг-влево {}\n'.format(width * pixScale))
out.close()
