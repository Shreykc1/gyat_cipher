from PIL import Image

img = Image.open('test.jpg')
pixels = list(img.getdata())

print(len(pixels))