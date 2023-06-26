from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np

image = Image.open('any_file_jpg')

image.show()
plt.imshow(image)


watermark_image = image.copy()

draw = ImageDraw.Draw(watermark_image)

w, h = image.size

x, y = int(w / 2), int(h / 2)

if x > y:
    font_size = y
elif y > x:
    font_size = x
else:
    font_size = x

font = ImageFont.truetype("arial.ttf", int(font_size / 6))

draw.text((x+1, y-20), "some_text", fill=(0, ), font=font, anchor='ms')
plt.subplot(1, 2, 1)
plt.title('Watermarked')
plt.imshow(watermark_image)
draw.text((x, y), "some_text", fill=(255,), font=font, anchor='ms')
plt.subplot(1, 2, 2)
plt.title("white text")
plt.imshow(watermark_image)
plt.show()