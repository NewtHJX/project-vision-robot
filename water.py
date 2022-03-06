import cv2

import numpy as np


def waterShed(sourceDir):
	# ��ȡͼƬ
	img = cv2.imread(sourceDir)
	# ԭͼ�Ҷȴ���,�����ͨ��ͼƬ
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	# ��ֵ������Otsu�㷨
	reval_O, dst_Otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)
	# ��ֵ������Triangle�㷨
	reval_T, dst_Tri = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_TRIANGLE)
	# �������ڳߴ�
	kernel = np.ones((3, 3), np.uint8)
	# ��̬ѧ����:������,���ͱ�Ե
	opening = cv2.morphologyEx(dst_Tri, cv2.MORPH_OPEN, kernel, iterations=2)
	# ���ʹ���������
	dilate_bg = cv2.dilate(opening, kernel, iterations=3)
	# ���㿪����ͼ������������ؾ���
	dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
	# ������
	norm = cv2.normalize(dist_transform, 0, 255, cv2.NORM_MINMAX)
	# ��ֵ�������ͼ��,��ȡͼ��ǰ��ͼ
	retval_D, dst_fg = cv2.threshold(dist_transform, 0.5*dist_transform.max(), 255, 0)
	# ǰ��ͼ��ʽת��
	dst_fg = np.uint8(dst_fg)
	# δ֪�������:������ȥǰ��
	unknown = cv2.subtract(dilate_bg, dst_fg)
	cv2.imshow("Difference value", unknown)
	cv2.imwrite('image_test0.png', unknown)
	# ������������
	retval_C, marks = cv2.connectedComponents(dst_fg)
	marks1 = np.uint8(marks)
	cv2.imshow('Connect marks', marks1)
	cv2.imwrite('image_test1.png', marks1)
	# ������ģ
	#marks = np.unicode(marks)
	marks = marks + 1
	marks[unknown==255] = 0
	marks1 = np.uint8(marks)
	cv2.imshow("marks undown", marks1)
	# ��ˮ���㷨�ָ�
	#marks = np.uint8(marks)
	marks = cv2.watershed(img, marks)
	# ���Ʒָ���
	img[marks == -1] = [255, 0, 255]
	cv2.imshow("Watershed", img)
	cv2.imwrite('image_test_water.png', img)
	cv2.waitKey(0)
sourceDir = "image2.jpg"
waterShed(sourceDir)
