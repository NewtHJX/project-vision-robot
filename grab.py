import cv2

import numpy as np


def grab_cut(sourceDir):
	# ��ȡͼƬ
	img = cv2.imread(sourceDir)
	# ͼƬ���
	img_x = img.shape[1]
	# ͼƬ�߶�
	img_y = img.shape[0]
	# �ָ�ľ�������
	rect = (96,1, 359, 358)
	# ����ģʽ,����Ϊ1��,13x5��
	bgModel = np.zeros((1, 65), np.float64)
	# ǰ��ģʽ,����Ϊ1��,13x5��
	fgModel = np.zeros((1, 65), np.float64)
	# ͼ����ģ,ȡֵ��0,1,2,3
	mask = np.zeros(img.shape[:2], np.uint8)
	# grabCut����,GC_INIT_WITH_RECTģʽ
	cv2.grabCut(img, mask, rect, bgModel, fgModel, 4, cv2.GC_INIT_WITH_RECT)
	# grabCut����,GC_INIT_WITH_MASKģʽ
	# cv2.grabCut(img, mask, rect, bgModel, fgModel, 4, cv2.GC_INIT_WITH_MASK)
	# ������0,2���0,�������1
	mask2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
	# ���¼���ͼ����ɫ,��ӦԪ�����
	img = img*mask2[:, :, np.newaxis]
	cv2.imshow("Result", img)
	cv2.waitKey(0)
sourceDir = "image6.jpg"
grab_cut(sourceDir)

