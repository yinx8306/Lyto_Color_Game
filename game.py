

# import pyautogui
# print(pyautogui.size())#1440,900
# pyautogui.moveTo(1400, 900) 
# print(pyautogui.position())

import pyautogui
import numpy as np
import cv2
from PIL import ImageGrab
import autopy
import time
pyautogui.moveTo(544,424)
pyautogui.click()
def click_color_level1():
	
	start_x=903
	start_y=258
	img = ImageGrab.grab(bbox=(start_x,start_y,start_x+722,start_y+1442))
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

	step=200
	different_spot=[]
	start_time = time.time()
	for i in range(1,3):
		for j in range(1,3):
			origin_y=510*2-258
			origin_x=580*2-903
			first_color=frame[origin_y, origin_x]
			spot_color = frame[510*2-258+step*(j-1), 580*2-903+step*(i-1)]
			first_color_list=first_color.tolist()
			spot_color_list=spot_color.tolist()
			if spot_color_list!=first_color_list:
				
				# print(510*2-258+step*(j-1), 580*2-903+step*(i-1))
				y=(510*2+step*(j-1))/2
				x=(580*2+step*(i-1))/2
				different_spot+=(x,y)
				#print(different_spot)
	print("--- %s seconds ---" % (time.time() - start_time))			
	if len(different_spot)>2:
		pyautogui.moveTo((origin_x+903)/2,(origin_y+258)/2)
		pyautogui.click()

						
	if len(different_spot)==2:
		pyautogui.moveTo(x,y)
		pyautogui.click()
	time.sleep(0.1)
	
	print("--- %s seconds ---" % (time.time() - start_time))

click_color_level1()
click_color_level1()
click_color_level1()


def click_color_levelup(n):
	start_x=903
	start_y=258
	img = ImageGrab.grab(bbox=(start_x,start_y,start_x+722,start_y+1442))
	img_np = np.array(img)
	frame = cv2.cvtColor(img_np, cv2.COLOR_RGB2BGR)

	step=int(300/n)*2
	different_spot=[]
	start_time = time.time()
	for i in range(1,n+1):
		for j in range(1,n+1):
			origin_y=460*2-258-4*n
			origin_x=520*2-903-4*n

			first_color=frame[origin_y, origin_x]
			# print(first_color)
			first_color_list=first_color.tolist()
			spot_color = frame[origin_y+step*(j-1), origin_x+step*(i-1)]
			# print(spot_color)
			spot_color_list=spot_color.tolist()
			if spot_color_list!=first_color_list:
				# print('y')
				# print(510*2-258+step*(j-1), 580*2-903+step*(i-1))
				y=(origin_y+258+step*(j-1))/2
				x=(origin_x+903+step*(i-1))/2

				different_spot+=(x,y)

	# print(different_spot)

	print("--- %s seconds ---" % (time.time() - start_time))		
	if len(different_spot)>2:
		pyautogui.moveTo((origin_x+903)/2,(origin_y+258)/2)
		pyautogui.click()
		# print(pyautogui.position())
						
	if len(different_spot)==2:
		pyautogui.moveTo(different_spot[0],different_spot[1])
		pyautogui.click()
		# print(pyautogui.position())
	time.sleep(0.1)
	
	# frame = cv2.resize(frame, (361,721))
	# cv2.imshow("frame", frame)
	# cv2.waitKey(0)
	# cv2.destroyAllWindows()


click_color_levelup(3)
click_color_levelup(3)
click_color_levelup(3)
click_color_levelup(3)
click_color_levelup(3)
click_color_levelup(3)
# click_color_levelup(3)#10
# click_color_levelup(4)
# click_color_levelup(4)
# click_color_levelup(4)
# click_color_levelup(4)
# click_color_levelup(4)
# click_color_levelup(4)
# click_color_levelup(4)
# click_color_levelup(4)
# click_color_levelup(4)
# click_color_levelup(4)#20
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(5)
# click_color_levelup(6)#35
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)
# click_color_levelup(6)#47
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)#68
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)#85
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)
# click_color_levelup(7)#100
# click_color_levelup(7)
# click_color_levelup(7)


