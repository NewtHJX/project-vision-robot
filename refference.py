import cv2
import numpy as np

def test1():
    imageDir = "image.jpg"
    #flag = 1
    src = cv2.imread(imageDir,0)#flag图片读取方式0灰度 1彩色
    cv2.namedWindow("test_windows",0)#0可以改变窗口大小 不写则不能改变
    cv2.imshow("test_windows",src)
    cv2.waitKey(0) #0一直显示，直到按下数字
    cv2.destroyAllWindows()

def test2():
    imageDir = "image.jpg"
    src = cv2.imread(imageDir,1)
    cv2.imshow("image",src)
    print(type(src))#<class 'numpy.ndarray'>
    print(src.shape)#(828, 903, 3)
    print(src.size)#2243052
    print(src.dtype)#uint8
    pixel_data = np.array(src)
    print(pixel_data)
    cv2.imwrite("image_ref.png",src)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


test1();
test2();

