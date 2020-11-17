import requests
import re
import base64
from fontTools.ttLib import TTFont  # 解析字体文件的包
from PIL import Image, ImageDraw, ImageFont  #绘制图片
import pytesseract   #文字识别库,这个包的安装还需要安装tesseract.exe，可以网上搜教程
import numpy

def funCover():
    fontPath='woff.woff'
    font=TTFont(fontPath)
    codeList=font.getGlyphOrder()[2:]
    #print(codeList)
    #print(codeList)
    im=Image.new("RGB",(1800,1000),(255,255,255))
    dr=ImageDraw.Draw(im)


    font=ImageFont.truetype(fontPath,40)

    count=15
    arrayList = numpy.array_split(codeList, count)  # 将列表切分成15份，以便于在图片上分行显示



    for t in range(count):
        newList = [i.replace("uni", "\\u") for i in arrayList[t]]
        text = "".join(newList)
        text = text.encode('utf-8').decode('unicode_escape')
        # text = text.encode('utf-8').decode('unicode_escape')
        dr.text((0, 50 * t), text, font=font, fill="#000000")
    im.save("sss.jpg")
    im = Image.open("sss.jpg")      #可以将图片保存到本地，以便于手动打开图片查看

    result = pytesseract.image_to_string(im, lang="chi_sim")
    result = result.replace(" ", "").replace("\n", "")
    codeList = [i.replace("uni", "&#x") + ";" for i in codeList]

    print(codeList,result)
    print(codeList)
    # return dict(zip(codeList, list(result)))

if __name__ == '__main__':
    funCover()


