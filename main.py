# https://longqiu.taobao.com
# @file - By: LQ008 - Fri Oct 11 2024

"""

@file OMV-RT 对色块识别，并输出目标色块的中心坐标位置
有关色块识别 更多参数设置参考：https://docs.openmv.io/library/omv.image.html#image.Image.find_blobs

实验流程：连接好LQ-OMV-RT至电脑
        本例程以红色做简单示例，可以根据示例编写自己的程序
        1、LAB阈值设置，可以在IDE中打开一个 heloWorld 示例工程，从帧缓冲区提取编辑阈值
            然后复制到本程序的target_thresholds列表中
        2、运行程序后，让镜头对准到红色物体，如果身边没有红色，可以自己调整阈值改为其他颜色的色块识别

        注意：
            1、使用颜色识别，对环境光线变化有一定的要求，所以需要需要关闭自动曝光和白平衡自动增益
            2、由于初始化后关闭了自动曝光和白平衡自动增益，所以一定要放在使用场景下再运行程序，避免先后环境光不一样影响阈值判断

实验现象：
        程序运行后，摄像头初始化完成后，开始拍照，并对图像帧根据目标LAB阈值进行颜色识别，
        并打印出目标中心坐标，同时再IDE帧缓冲区显示框选 没目标色块
"""

# import image, time
import image
import sensor
from machine import UART,LED
# import os

SCC8660_W = 160
SCC8660_H = 120

LEDB = LED("LED_BLUE")                  # 板载RGB红色LED

#--------------------------------- 测试参数 ----------------------------------------#
a = 0
# regression_threshold = [(20, 84, -48, 35, -44, 14),
#                         (20, 84, -48, 35, -44, -4)]
regression_threshold = [(20, 84, -48, 35, -44, 14),
                        (20, 84, -48, 35, -44, -4),
                        (23, 57, -31, 20, -46, -2)]
#--------------------------------- 测试参数 ----------------------------------------#

#----------------------------------- 参数 ------------------------------------------#
WHITE_UP    = 120
WHITE_DOWN  = 0
RED_UP		=255;
RED_DOWN	=185;
BLUE_UP		=175;
BLUE_DOWN	=125;

# 赛道状态枚举
STRAIGHT   = 0
S_LEFT     = 1
S_RIGHT    = 2
B_LEFT_I   = 3
B_RIGHT_I  = 4
B_LEFT_O   = 5
B_RIGHT_O  = 6

track_statu=STRAIGHT
#----------------------------------- 参数 ------------------------------------------#

#----------------------------------- 初始化 ----------------------------------------#
# 摄像头
sensor.reset()
sensor.set_pixformat(sensor.RGB565)     # 设置图像格式为 RGB565.GRAYSCALE
sensor.set_framesize(sensor.QQVGA)      # 设置图像帧像素尺寸
sensor.skip_frames(time = 2000)         # 跳过1s，使新设置生效以及适应环境后关闭增益和白平衡自动设置
sensor.set_auto_gain(False)             # 关闭自动自动增益。默认开启的，在颜色识别中，一定要关闭白平衡。
sensor.set_auto_whitebal(False)         # 关闭白平衡。白平衡是默认开启的，在颜色识别一定要关闭。
sensor.set_brightness(3)
#串口
uart1 = UART(1, 115200, timeout_char=200)
#----------------------------------- 初始化 ----------------------------------------#

# clock = time.clock() # 追踪帧率

#---------------------------------- 工具函数 ---------------------------------------#
def min3v(v1, v2, v3):
    return min(v1, v2, v3)

def max3v(v1, v2, v3):
    return max(v1, v2, v3)
#---------------------------------- 工具函数 ---------------------------------------#

#--------------------------- 目标色块的LAB阈值元组列表 -------------------------------#
target_thresholds = [
                (7, 31, 3, 46, 2, 26)   # 红色目标，最多可添加32组
                ,(4, 44, 8, 120, 6, 110)
                ,(2, 33, 8, 96, -8, 62)
                ,(20, 57, 21, 56, -4, 42)
        ]
#--------------------------- 目标色块的LAB阈值元组列表 -------------------------------#

#-------------------------------- 自己编写的函数 ------------------------------------#
def rgb_to_hsl(rgb):
    r, g, b = rgb

    maxval = max3v(r, g, b)
    minval = min3v(r, g, b)
    difval = maxval - minval

    # 亮度
    l = (maxval + minval) * 240 // 255 // 2

    if maxval == minval:
        h = 0
        s = 0
    else:
        # 色调
        if maxval == r:
            if g >= b:
                h = 40 * (g - b) // difval
            else:
                h = 40 * (g - b) // difval + 240
        elif maxval == g:
            h = 40 * (b - r) // difval + 80
        elif maxval == b:
            h = 40 * (r - g) // difval + 160

        # 饱和度
        if l == 0:
            s = 0
        elif l <= 120:
            s = difval * 240 // (maxval + minval)
        else:
            s = difval * 240 // (480 - (maxval + minval))

    # 限定范围到0~240
    h = max(0, min(240, h))
    s = max(0, min(240, s))
    l = max(0, min(240, l))
    return {'h': h, 's': s, 'l': l}  # 返回一个字典

# 判断箱子是否在赛道内
def box_in_saidao(img, x, y, w, h, allow_percent):
    x1 = x
    x2 = x+w
    y2 = y+h

    row_blue_number = 0
    for col in range(x1, x2):
        col_blue_number = 0
        if row_blue_number >= w * allow_percent:	# 判断为出赛道
            return 0
        for row in range(y2 + 5, SCC8660_H*3//4):    # +5 是为了过滤掉底部可能将箱子框进来一些
            pixel = img[row*SCC8660_W+col]      # 获取像素
            hsl = rgb_to_hsl(pixel)         # 转换为HSL
            if not (WHITE_DOWN <= hsl['h'] <= WHITE_UP):
                col_blue_number += 1
            if col_blue_number >= 2:
                row_blue_number += 1
                break  # 下一列

    return 1


def find_max(blob_all):# 获取相同色块中的最大的色块
    max_size=0
    for blob in blob_all:
        if blob[2]*blob[3] > max_size:
            max_blob=blob
            max_size = blob[2]*blob[3]
    return max_blob


while True:

    #---------------------------参数初始化---------------------------#
    left_hough_line=None
    right_hough_line=None
    #---------------------------参数初始化---------------------------#

    # clock.tick()

    img = sensor.snapshot()                                         # 捕获一帧图像
    # 可能用到的img.find_blobs()参数:
    # thresholds:目标色块LAB阈值元组列表, 必须要设置的
    # roi=感兴区域四元组(x,y,w,h):如果为空则表示，对整个img帧图像进行搜索查找
    # x_stride=2, y_stride=1:在搜索blob时要跳过的x，y像素数,如果已知blob的大小，则可以借助其忽略小于目标的x,y像素数，以加快搜索速度
    # area_threshold=10:如果blob的边界框面积小于 area_threshold ，则过滤掉它。
    # pixels_threshold=10:如果blob的像素计数少于 pixels_threshold ，则过滤掉它。
    # merge=False: merge 如果为 True，则会合并所有未被过滤掉且其边界矩形相互交叉的斑点。
    # margin:可用于在交叉测试期间增加或减少斑点边界矩形的大小。例如，当 margin 为 1 时，边界矩形相距 1 像素的斑点将被合并。

    # 色块检测
    # 首先检测到的箱子需要在赛道上
    # area 为 300 时开始降速
    blobs = img.find_blobs(target_thresholds,pixels_threshold=25, area_threshold=50, merge=True)     #像素阈值25，面积阈值50，可接受的最小色块大小
    if blobs:                                                       # 找到追踪目标
        blob = find_max(blobs)                                      # 挑选最大的一个
        uart1.write(bytes([0xAA, 0xBB, 0x08, blob.cx(), blob.y()+blob.h(), blob.w(), blob.h(), 0xDD]))  # 串口发送数据
        # print("{}, {}, {}, {}".format(blob.cx(), blob.y()+blob.h(), blob.w(), blob.h()))
        print("area:{}".format(blob.w()*blob.h()))

    # 找圆
    left_circles = img.find_circles(roi=(0, blob.cy(), blob.x()+1, SCC8660_H), r_min=0, threshold=2000, r_step=1)
    right_circles = img.find_circles(roi=(blob.x()+blob.w()-1, blob.cy(), SCC8660_W, SCC8660_H), r_min=0, threshold=2000, r_step=1)

    # 线性回归拟合直线
    left_regression_line = img.get_regression(regression_threshold, roi=(0, blob.y(), blob.x()+1, SCC8660_H//2), x_stride=2, area_threshold=10, pixels_threshold=20)
    right_regression_line = img.get_regression(regression_threshold, roi=(blob.x()+blob.w()-1, blob.y(), SCC8660_W, SCC8660_H//2), x_stride=2, area_threshold=10, pixels_threshold=20)
    # 提取角度信息
    if(left_regression_line): left_regression_line_angle = left_regression_line.theta()
    if(right_regression_line): right_regression_line_angle = right_regression_line.theta()

    # 霍夫变换找直线
    # 分开左右找
    left_lines = img.find_lines(roi=(0, blob.y(), SCC8660_W//2, SCC8660_H//2), threshold=500, theta_margin=25, rho_margin=25)
    right_lines = img.find_lines(roi=(SCC8660_W//2, blob.y(), SCC8660_W//2, SCC8660_H//2), threshold=500, theta_margin=25, rho_margin=25)
    if(left_lines):
        # 限制角度筛选
        theta_filter_left_lines = [line for line in left_lines if 10 <= line.theta() <= 70]
        # 取更靠近中心的线
        if(theta_filter_left_lines): left_hough_line = max(theta_filter_left_lines, key=lambda l: l.theta())
        # 提取角度信息
        if(left_hough_line): left_hough_line_angle = left_hough_line.theta()
    if(right_lines):
        # 限制角度筛选
        theta_filter_right_lines = [line for line in right_lines if 110<=line.theta()<=170]
        # 取更靠近中心的线
        if(theta_filter_right_lines): right_hough_line = min(theta_filter_right_lines, key=lambda l: l.theta())
        # 提取角度信息
        if(right_hough_line): right_hough_line_angle = right_hough_line.theta()

    # 计算两条直线夹角
    # if(left_hough_line and right_hough_line):
    #     jiajiao = abs(left_hough_line.theta()-right_hough_line.theta())
    #     print("left:{}, right:{}".format(left_hough_line.theta(), right_hough_line.theta()))
    #     # print("夹角:{}".format(jiajiao))
    # else: jiajiao = 0

    # 边缘检测
    # edges = img.find_edges(image.EDGE_CANNY, threshold=(50, 100))

    # 拟合椭圆
    # ellipse = blob.enclosed_ellipse()
    # img.draw_ellipse(ellipse, color=(0, 255, 0))

    # 赛道状态判断
    # if(70<=jiajiao<=100):
    #     print("直道")
    #     print("夹角:{}".format(jiajiao))
    # else:
    #     print("NNNN")
    #     print("夹角:{}".format(jiajiao))

    #----------------------------统一画图----------------------------#
    # 目标检测方框
    img.draw_rectangle(blob.rect(),color=(0, 0, 0))            # 根据色块边界框 框选目标
    img.draw_cross(blob.cx(), blob.cy(),color=(0, 255, 255))      # 根据色块中心位置画十字
    # 线性回归直线
    if left_regression_line:
        img.draw_line(left_regression_line.line(), color=[255, 0, 0])
    if right_regression_line:
        img.draw_line(right_regression_line.line(), color=[255, 255, 0])
    # 霍夫变换直线
    if(left_hough_line): img.draw_line(left_hough_line.x1(), left_hough_line.y1(), left_hough_line.x2(), left_hough_line.y2(), [0, 0, 255])
    if(right_hough_line): img.draw_line(right_hough_line.x1(), right_hough_line.y1(), right_hough_line.x2(), right_hough_line.y2(), [0, 255, 0])
    # 画圆
    for circle in left_circles:
        img.draw_circle(circle.x(), circle.y(), circle.r(), color=(0, 0, 255))
    for circle in right_circles:
        img.draw_circle(circle.x(), circle.y(), circle.r(), color=(0, 255, 0))
    #----------------------------统一画图----------------------------#

    #--------------------------判断赛道状态--------------------------#
    track_statu = STRAIGHT
    # 缺少一条回归线或是一条霍夫线，那么就直接判断成弯道
    if((left_regression_line and (not right_regression_line)) or (left_hough_line and (not right_hough_line))):
        if(not (left_regression_line_angle<30 or left_regression_line_angle>85)): # or left_circles
            track_statu = B_RIGHT_I
    if(((not left_regression_line) and right_regression_line) or ((not left_hough_line) and right_hough_line)):
        if(not (right_regression_line_angle>150 or right_regression_line_angle<95)): # or right_circles
            track_statu = B_LEFT_I
    # 两条回归线都有，但是左边或者右边的回归线有一条 theta 角异常
    # 两条回归线都有，但是霍夫直线缺少一条
    # 两条回归线都有，但是左边或是右边有检测出圆形
    if((left_regression_line and right_regression_line) and (track_statu==STRAIGHT)):
        # 两条霍夫线都有
        if(left_hough_line and right_hough_line):
            if(left_hough_line_angle<15):
                track_statu = B_LEFT_I
            if(right_hough_line_angle>165):
                track_statu = B_RIGHT_I
        if((left_regression_line_angle<30 or left_regression_line_angle>85 or left_circles) and (track_statu==STRAIGHT)):
            track_statu = B_LEFT_I
        if((right_regression_line_angle>150 or right_regression_line_angle<95 or right_circles) and (track_statu==STRAIGHT)):
            track_statu = B_RIGHT_I
        # if((left_regression_line_angle>85 or (not left_hough_line))
        #     and (not right_circles)):
        #     track_statu = B_LEFT_I
        # if((right_regression_line_angle<95 or (not right_hough_line))
        #     and (not left_circles)):
        #     track_statu = B_RIGHT_I

    print("{}".format(left_regression_line_angle))
    print("{}".format(right_regression_line_angle))
    # print("{}".format(left_hough_line_angle))
    # print("{}".format(right_hough_line_angle))
    #--------------------------判断赛道状态--------------------------#

    LEDB.toggle()
    if(track_statu==STRAIGHT): print("直道")
    elif(track_statu==S_LEFT): print("小左弯")
    elif(track_statu==S_RIGHT): print("小右弯")
    elif(track_statu==B_LEFT_I): print("左弯弯弯弯弯弯弯弯弯弯弯弯弯弯弯弯弯")
    elif(track_statu==B_RIGHT_I): print("右弯wwwwwwwwwwwwwwwwwwwwwww")
    # print(f"fps:{clock.fps():.2f}")

e
