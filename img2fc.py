import cv2 
import numpy as np 

img = cv2.imread(input('pic: '), 0)
maxScale = int(input('max size: '))

width = np.shape(img)[1]
height = np.shape(img)[0]

k = max(width, height) / maxScale

width = int(width / k)
height = int(height / k)

img = cv2.resize(img, (width, height))

out = open('img2fc.txt', 'w')
out.write('сдвиг-влево {}\n'.format(width/2*0.3))
out.write('сдвиг-вверх {}\n'.format(height/2*0.3))
for y in range(height):
  for x in range(width):
    if img[y][x] < 128: out.write('вправо 0.3\n')
    else: out.write('сдвиг-вправо 0.3\n')
  out.write('сдвиг-вниз 0.3\n')
  out.write('сдвиг-влево {}\n'.format(width * 0.3))
out.close()
