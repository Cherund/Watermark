from tkinter import *
from PIL import Image, ImageDraw, ImageFont


def watermark_create():
    path = image_path_entry.get()
    image = Image.open(path)
    watermark = watermark_entry.get()
    font = ImageFont.truetype("Arial", 100)
    d = ImageDraw.Draw(image)
    d.text((image.size[0]-d.textlength(watermark), image.size[1]-10), watermark, anchor="rd", font=font)
    image.show()
    image.save(f'{watermark}.jpg')


window = Tk()
window.title('Watermarking App')
window.config(padx=20, pady=20)


title_label = Label(text='Watermark creator', font=("Courier", 30), pady=20)
title_label.grid(row=0, column=0, columnspan=2)

image_path_label = Label(text='Enter full image path:', )
image_path_label.grid(row=1, column=0)

image_path_entry = Entry(width=40)
image_path_entry.grid(row=1, column=1)

watermark_label = Label(text='What text you want on your watermark?')
watermark_label.grid(row=2, column=0)

watermark_entry = Entry(width=40)
watermark_entry.grid(row=2, column=1)

create_image_button = Button(text='Create image with watermark', command=watermark_create)
create_image_button.grid(row=3, column=0, columnspan=2)

window.mainloop()
