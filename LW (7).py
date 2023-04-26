from PIL import Image
import cv2

def z1():
    filename = "picone.jpg"
    with Image.open(filename) as img:
        img.load()
    img.show()
    width, heith = img.size
    format = img.format
    mode = img.mode
    print("ширина:", width)
    print("высота:", heith)
    print("формат:", format)
    print("цветовая модель: ", mode)

def z2():
    filename = "pictwo.jpg"
    with Image.open(filename) as img:
        img.load()
    newimg = img.resize((img.width // 3, img.height // 3))
    newimg.save("pictwo1.jpg")
    newimg = img.transpose(Image.FLIP_LEFT_RIGHT)
    newimg.save("pictwo2.jpg")
    newimg1 = img.transpose(Image.ROTATE_180)
    newimg1.save("pictwo3.jpg")

def z3():
    filename = "picone.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("bw1.jpg")

    filename = "pictwo.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("bw2.jpg")

    filename = "picthree.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("bw3.jpg")

    filename = "picfour.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("bw4.jpg")

    filename = "picfive.jpg"
    with Image.open(filename) as img:
        img.load()
    gray_img = img.convert("L")
    gray_img.save("bw5.jpg")

def z4():
    filename = "sobaken.jpg"
    with Image.open(filename) as img:
        img.load()
    watermark = Image.open("watermark.png")

    img.paste(watermark, (42, 40), watermark)
    img.save("img_with_watermark.png")


z4()
