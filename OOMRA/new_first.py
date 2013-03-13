print 'hello world!'
import cv2.cv as cv
import sys
import numpy as np


#im = cv.LoadImage('ak.jpg','jpg')

#cv.ShowImage( 'ak.jpg',im)
#a=2

#b=np.sqrt(9)
#print b
#cv.NamedWindow('AhmadKhan')
#cv.ShowImage()

#im1=cv.LoadImageM('ak.jpg')


#cv.ShowImage('Ahmad', im1)
#a=2
#raw_input(a)

cv.NamedWindow("a_window",cv.CV_WINDOW_AUTOSIZE)
image=cv.LoadImage('test.png',cv.CV_LOAD_IMAGE_COLOR)
font=cv.InitFont(cv.CV_FONT_HERSHEY_SIMPLEX, 1,1,0,3,8)
#x= x position of text
#y = y position of text

x=y=50
#cv.PutText(frame, "Hello World!!!", (x,y), font, 255)
cv.ShowImage('a_window', image)
cv.WaitKey(10000)
#cv.SaveImage(image.png, image)