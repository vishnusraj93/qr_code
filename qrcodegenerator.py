from tkinter import *
import pyqrcode
from PIL import ImageTk,Image
root = Tk()

def generate():
    link_name = name_entry.get()
    link = link_entry.get()
    file_name = link_name + ".png"
    url = pyqrcode.create(link)
    url.png(file_name,scale=6)
    image = ImageTk.PhotoImage(Image.open(file_name))
    image_label = Label(image=image)
    image_label.image = image
    canvas.create_window(155,380,window=image_label)

root.title("QR Code")
canvas = Canvas(root,width=300,height=530)
canvas.pack()
img = PhotoImage(file='C:\Images\g.png')
canvas.create_image(300,130,image=img,anchor='center')
icon = PhotoImage(file='C:\Images\qr.png')
root.iconphoto(False, icon)
app_label = Label(root,text="QR Code Generator",fg='#000000',bg='#fcfcfc',
                  font=("Ariel",20,'bold'))
canvas.create_window(155,50,window=app_label)
name_label = Label(root,text="Link Name",fg='#000000',bg='#fcfcfc',font=("Verdana",8))
link_label = Label(root,text="Link",fg='#000000',bg='#fcfcfc',font=("Verdana",8))
canvas.create_window(155,100,window=name_label)
canvas.create_window(155,160,window=link_label)
name_entry = Entry(root)
link_entry = Entry(root)
canvas.create_window(155,130,width = 185,window=name_entry)
canvas.create_window(155,190,width = 185,window=link_entry)
button = Button(text="Generate QR Code",command=generate)
canvas.create_window(155,230,window=button)

root.mainloop()


