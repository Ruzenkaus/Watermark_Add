from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
from tkinter import Tk, Button, filedialog, messagebox
import numpy as np


def add_watermark():

    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image = Image.open(file_path)



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

        font = ImageFont.truetype("arial.ttf", int(font_size / 4))

        draw.text((x+1, y-20), "some_text", fill=(0, ), font=font, anchor='ms')
        plt.subplot(1, 2, 1)
        plt.title('Watermarked')
        plt.imshow(watermark_image)
        plt.show()
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if save_path:
            watermark_image.save(save_path)
            print("Watermark is successfully added")
    else:
        messagebox.showerror('path not selected!')


main = Tk()

main.title('Adding watermark')

button = Button(text='Add watermark', command=add_watermark)
button.pack()

main.mainloop()