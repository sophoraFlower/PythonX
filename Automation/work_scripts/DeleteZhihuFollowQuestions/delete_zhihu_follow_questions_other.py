# coding=utf-8
import pyautogui
import time
from PIL import ImageGrab
import cv2


screenWidth, screenHeight = pyautogui.size()
print(screenWidth, screenHeight)
currentMouseX, currentMouseY = pyautogui.position()
print(screenWidth, screenHeight)
time.sleep(3)
# 浏览器显示在桌面
pyautogui.moveTo(565, 881)
pyautogui.click()

for i in range(700):
    time.sleep(3)
    # 在问题页
    pyautogui.moveTo(610, 16)
    pyautogui.click()
    time.sleep(1)
    bbox = (0, 0, 340, 900)
    im = ImageGrab.grab(bbox)
    im.save("./as.png")
    imgsr = cv2.imread("./as.png")
    imgtm = cv2.imread("./reference.png")
    # 获取模板图片的高和宽
    imgtmh1 = imgtm.shape[0]
    imgtmw1 = imgtm.shape[1]

    # 与模版比对
    res = cv2.matchTemplate(imgsr, imgtm, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    img = cv2.rectangle(imgsr, max_loc, (max_loc[0] + imgtmw1, max_loc[1] + imgtmh1), (0, 0, 255), 2)

    cv2.imshow('Image', img)
    print(max_loc[0] + imgtmw1, max_loc[1] + imgtmh1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    pyautogui.moveTo(275, 307, duration=2, tween=pyautogui.easeInOutQuad)
    # 取消关注
    pyautogui.click()
    time.sleep(1)
    # 关闭问题页
    pyautogui.moveTo(707, 17)
    pyautogui.click()
    time.sleep(1)
    # 刷新关注页
    pyautogui.moveTo(87, 53)
    pyautogui.click()
    time.sleep(2)
    # 进入问题页
    pyautogui.moveTo(374, 711)
    pyautogui.click()
