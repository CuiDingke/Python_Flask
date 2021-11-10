from PIL import Image

im = Image.open('static/upload/qq.jpg')

im.rotate(45).show()
