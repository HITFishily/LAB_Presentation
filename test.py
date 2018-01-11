import os
import time
import random
# 900 800     进入淘宝
# 540 300     选择店铺
# 540 500     进入店铺
# 500 100     搜索框
# 370 1800    点亮收藏
# 250 960     左商品
# 750 960		右商品
# cmd1 = "adb shell input tap 900 200"
# cmd2 = "adb shell input tap 500 100"
# cmd3 = "adb shell input text \"julystudio\""

# os.system(cmd1)
# print(cmd1)
# time.sleep(10)
# os.system(cmd2)
# print(cmd2)
# time.sleep(5)
# os.system(cmd3)
# print(cmd3)
# time.sleep(3)

# os.system("adb shell input keyevent 66")

def openTaoBao():
	os.system("adb shell input keyevent 3")
	time.sleep(3)
	os.system("adb shell input keyevent 3")
	time.sleep(3)
	os.system("adb shell input tap 900 800")
	time.sleep(10)

def startFindGoods():
	os.system("adb shell input tap 500 100")
	time.sleep(5)

def inputNameOfGoods(name):
	cmd = "adb shell input text \"" + name + "\""
	os.system(cmd)
	time.sleep(3)
	os.system("adb shell input keyevent 66")
	time.sleep(4)

def intoShop():
	os.system("adb shell input tap 540 300")
	time.sleep(3)
	os.system("adb shell input tap 540 500")
	time.sleep(5)


def simulateSwipe():
	r = random.randint(30, 500)
	cmd = "adb shell input swipe 900 1200 300 500 " + str(r)
	os.system(cmd)
	time.sleep(10)
	r = random.randint(30, 500)
	cmd = "adb shell input swipe 900 1200 300 500 " + str(r)
	os.system(cmd)
	time.sleep(10)

def intoGoodAndFavor():
	r = random.randint(0,1)
	if r == 1:
		os.system("adb shell input tap 250 960")
		time.sleep(5)
	elif r == 0:
		os.system("adb shell input tap 750 960")
		time.sleep(5)
	os.system("adb shell input tap 370 1800")
	time.sleep(2)

def exitTaoBao():
	os.system("adb shell input keyevent 3")
	time.sleep(3)
	os.system("adb shell input keyevent 3")
	time.sleep(3)

	


openTaoBao()
startFindGoods()
inputNameOfGoods("julystudio")
intoShop()
simulateSwipe()
intoGoodAndFavor()
exitTaoBao()