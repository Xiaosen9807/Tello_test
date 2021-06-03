#图像处理

from PIL import Image
import numpy as np
im= Image.open('C://Users//Surface//Desktop//doge.jpg')
#im.show()
im=np.array(im)
print(im)
im.shape
im[100,100]
im_red=im[:,:,0]
Image.fromarray(im_red).show()







